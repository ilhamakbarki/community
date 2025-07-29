"""Karrio Logistic IO tracking API implementation."""

# import karrio.schemas.logistic_io.tracking_request as logistic_io_req
import karrio.schemas.logistic_io.tracking_response as logistic_io_res

import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.logistic_io.error as error
import karrio.providers.logistic_io.utils as provider_utils
import karrio.providers.logistic_io.units as provider_units


def parse_tracking_response(
    _response: lib.Deserializable[typing.List[typing.Tuple[str, dict]]],
    settings: provider_utils.Settings,
) -> typing.Tuple[typing.List[models.TrackingDetails], typing.List[models.Message]]:
    responses = _response.deserialize()

    messages: typing.List[models.Message] = sum(
        [
            error.parse_error_response(responses, settings)
        ],
        start=[],
    )
    shipments = logistic_io_res.TrackingResponse.from_dict(responses).data if responses.get("status") == True else None
    if shipments is None:
        return [], messages

    tracking_generated = [
        _extract_details(details, settings)
        for details in shipments
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
    data: logistic_io_res.Datum,
    settings: provider_utils.Settings,
) -> models.TrackingDetails:
    status = next(
        (
            status.name
            for status in list(provider_units.TrackingStatus)
            if data.order_details.current_stage.stage.lower() in status.value
        ),
        provider_units.TrackingStatus.in_transit.name,
    )

    return models.TrackingDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        tracking_number=data.cp_awb,
        info=models.TrackingInfo(
            customer_name=data.customer_details.name,
            order_id=data.referance_awb,
            order_date=lib.fdatetime(data.order_details.created_date.replace('Z', ''), "%Y-%m-%dT%H:%M:%S.%f"),
            shipment_package_count=data.box_count,
            note="Brand reference number : " + data.order_details.brand_reference_number,
        ),
        events=[
            models.TrackingEvent(
                date=lib.fdate(event.date.replace('Z', ''), "%Y-%m-%dT%H:%M:%S.%f"),
                description=event.status_remark,
                code=event.alpha_status_code,
                time=lib.ftime(event.date.replace('Z', ''), "%Y-%m-%dT%H:%M:%S.%f"),
            )
            for event in data.tracking_history.updates
        ],
        delivered=status == "delivered",
        status=status,
    )


def tracking_request(
    payload: models.TrackingRequest,
    settings: provider_utils.Settings,
) -> lib.Serializable:
    track_ids = ",".join(payload.tracking_numbers)
    request = dict(cp_awb=track_ids)
    return lib.Serializable(request, lib.to_dict)
