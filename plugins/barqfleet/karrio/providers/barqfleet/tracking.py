"""Karrio Barqfleet tracking API implementation."""

# IMPLEMENTATION INSTRUCTIONS:
# 1. Uncomment the imports when the schema types are generated
# 2. Import the specific request and response types you need
# 3. Create a request instance with the appropriate request type
# 4. Extract tracking details and events from the response to populate TrackingDetails
#
# NOTE: JSON schema types are generated with "Type" suffix (e.g., TrackingRequestType),
# while XML schema types don't have this suffix (e.g., TrackingRequest).

# import karrio.schemas.barqfleet.tracking_request as barqfleet_req
import karrio.schemas.barqfleet.tracking_response as barqfleet_res

import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.barqfleet.error as error
import karrio.providers.barqfleet.utils as provider_utils
import karrio.providers.barqfleet.units as provider_units


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
        [],
    )

    tracking_generated = [
        _extract_details(details, settings, tracking_number)
        for tracking_number, details in responses
        if details.get("errors") is None
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
    tracking_details = barqfleet_res.tracking_response_from_dict(data)

    if tracking_details is None:
        return None

    status = next(
        (
            status.name
            for status in list(provider_units.TrackingStatus)
            if tracking_details[0].code in status.value
        ),
        provider_units.TrackingStatus.in_transit.name,
    )

    return models.TrackingDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        tracking_number=tracking_number,
        events=[
            models.TrackingEvent(
                code=event.code,
                description=event.response_id + " - " + event.courier,
                latitude=event.cooridnates.latitude,
                longitude=event.cooridnates.longitude,
            )
            for event in tracking_details
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
