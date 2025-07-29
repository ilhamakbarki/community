"""Karrio Ajex tracking API implementation."""

# import karrio.schemas.ajex.tracking_request as ajex_req
import karrio.schemas.ajex.tracking_response as ajex_res

import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.ajex.error as error
import karrio.providers.ajex.utils as provider_utils
import karrio.providers.ajex.units as provider_units


def parse_tracking_response(
    _response: lib.Deserializable[typing.List[typing.Tuple[str, dict]]],
    settings: provider_utils.Settings,
) -> typing.Tuple[typing.List[models.TrackingDetails], typing.List[models.Message]]:
    responses = _response.deserialize()

    messages: typing.List[models.Message] = sum(
        [
            error.parse_error_response(response, settings, tracking_number=tracking_number)
            for tracking_number, response in responses
        ],
        start=[],
    )

    tracking_generated = [
        _extract_details(details, settings, tracking_number)
        for tracking_number, details in responses
        if details.get("responseCode") == "100"
    ]

    tracking_details = [detail for detail in tracking_generated if detail is not None]
    if not tracking_details:
        message_not_found = [models.Message(
            carrier_id=settings.carrier_id,
            carrier_name=settings.carrier_name,
            message="Tracking number not found",
        )]
        return [], message_not_found

    return tracking_details, messages


def _extract_details(
    data: dict,
    settings: provider_utils.Settings,
    tracking_number: str = None,
) -> models.TrackingDetails:
    tracking_details = ajex_res.tracking_response_from_dict(data)
    status = next(
        (
            status.name
            for status in list(provider_units.TrackingStatus)
            if tracking_details.order_details.final_status_code in status.value
        ),
        provider_units.TrackingStatus.in_transit.name,
    )

    shipping_date = lib.fdatetime(tracking_details.order_details.shippment_date.replace('Z', ''), "%Y-%m-%dT%H:%M:%S.%f")
    return models.TrackingDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        tracking_number=tracking_number,
        info=models.TrackingInfo(
            customer_name=tracking_details.order_details.receiver_details.name,
            order_date=shipping_date,
            package_weight=tracking_details.order_details.weight,
            shipping_date=shipping_date,
        ),
        events=[
            models.TrackingEvent(
                date=lib.fdate(event.action_time.replace('Z', ''), "%Y-%m-%dT%H:%M:%S.%f"),
                code=event.status,
                description=event.note,
                time=lib.ftime(event.action_time.replace('Z', ''), "%Y-%m-%dT%H:%M:%S.%f"),
                location=event.city_name,
            )
            for event in tracking_details.order_tracking_history
        ],
        delivered=status == "delivered",
        status=status,
    )


def tracking_request(
    payload: models.TrackingRequest,
    settings: provider_utils.Settings,
) -> lib.Serializable:
    request = payload.tracking_numbers
    return lib.Serializable(request, lib.to_dict)
