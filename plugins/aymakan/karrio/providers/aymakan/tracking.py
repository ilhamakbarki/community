"""Karrio Aymakan tracking API implementation."""

import karrio.schemas.aymakan.tracking_response as aymakan_res

import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.aymakan.error as error
import karrio.providers.aymakan.utils as provider_utils
import karrio.providers.aymakan.units as provider_units


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
    shipments = aymakan_res.TrackingResponse.from_dict(responses).data.shipments if responses.get("success") is True else None
    if shipments is None:
        return [], messages

    tracking_details = [
        _extract_details(details, settings)
        for details in shipments
    ]

    return tracking_details, messages


def _extract_details(
    data: aymakan_res.Shipment,
    settings: provider_utils.Settings,
) -> models.TrackingDetails:
    status = next(
        (
            status.name
            for status in list(provider_units.TrackingStatus)
            if data.status_label.lower() in status.value
        ),
        provider_units.TrackingStatus.in_transit.name,
    )

    return models.TrackingDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        tracking_number=data.tracking_number,
        events=[
            models.TrackingEvent(
                date=lib.fdate(event.created_at, "%Y-%m-%d %H:%M:%S"),
                description=event.description,
                code=event.status_code,
                time=lib.flocaltime(event.created_at, "%Y-%m-%d %H:%M:%S"),
            )
            for event in data.tracking_info
        ],
        estimated_delivery=lib.fdate(data.delivery_date, "%Y-%m-%d %H:%M:%S"),
        delivered=status == "delivered",
        status=status,
    )


def tracking_request(
    payload: models.TrackingRequest,
    settings: provider_utils.Settings,
) -> lib.Serializable:
    track_ids = ",".join(payload.tracking_numbers)
    request = dict(track_ids=track_ids)
    return lib.Serializable(request, lib.to_dict)
