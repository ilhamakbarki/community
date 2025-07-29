"""Karrio Logistic IO error parser."""

import typing
import karrio.lib as lib
import karrio.core.models as models
import karrio.providers.logistic_io.utils as provider_utils


def parse_error_response(
    responses: typing.Union[typing.List[dict], dict],
    settings: provider_utils.Settings,
    **kwargs,
) -> typing.List[models.Message]:
    results = responses if isinstance(responses, list) else [responses]
    errors: typing.List[dict] = [
        error for error in results if error.get("status") == False
    ]

    return [
        models.Message(
            carrier_id=settings.carrier_id,
            carrier_name=settings.carrier_name,
            message=error.get("message"),
            details={**kwargs},
        )
        for error in errors
    ]
