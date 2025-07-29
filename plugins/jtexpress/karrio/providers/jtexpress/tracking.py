"""Karrio J&T Express tracking API implementation."""

import karrio.schemas.jtexpress.tracking_request as jtexpress_req
import karrio.schemas.jtexpress.tracking_response as jtexpress_res

import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.jtexpress.error as error
import karrio.providers.jtexpress.utils as provider_utils
import karrio.providers.jtexpress.units as provider_units


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

    shipments = jtexpress_res.TrackingResponse.from_dict(responses).data if responses.get("code") == "1" else None
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
    data: jtexpress_res.Datum,
    settings: provider_utils.Settings,
) -> models.TrackingDetails:
    if data.details is None:
        return None

    status = next(
        (
            status.name
            for status in list(provider_units.TrackingStatus)
            if data.details[0].scan_type.lower() in status.value
        ),
        provider_units.TrackingStatus.in_transit.name,
    )

    return models.TrackingDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        tracking_number=data.bill_code,
        events=[
            models.TrackingEvent(
                date=lib.fdate(event.scan_time, "%Y-%m-%d %H:%M:%S"),
                description=event.desc,
                code=event.scan_type,
                latitude=event.latitude,
                longitude=event.longitude,
                time=lib.ftime(event.scan_time, "%Y-%m-%d %H:%M:%S"),
                location="%s,%s,%s" % (event.scan_network_province, event.scan_network_city, event.scan_network_area),
            )
            for event in data.details
        ],
        delivered=status == "delivered",
        status=status,
    )


def tracking_request(
    payload: models.TrackingRequest,
    settings: provider_utils.Settings,
) -> lib.Serializable:
    track_ids = ",".join(payload.tracking_numbers)
    request = jtexpress_req.TrackingRequest(
        bill_codes=track_ids
    )

    return lib.Serializable(request, lib.to_dict)
