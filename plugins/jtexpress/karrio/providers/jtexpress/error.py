"""Karrio J&T Express error parser."""

import typing
import karrio.lib as lib
import karrio.core.models as models
import karrio.providers.jtexpress.utils as provider_utils


def parse_error_response(
    responses: typing.Union[typing.List[dict], dict],
    settings: provider_utils.Settings,
    **kwargs,
) -> typing.List[models.Message]:
    results = responses if isinstance(responses, list) else [responses]
    errors: typing.List[dict] = [
        error for error in results if error.get("code") != "1"
    ]

    return [
        models.Message(
            carrier_id=settings.carrier_id,
            carrier_name=settings.carrier_name,
            code=error.get("code"),
            message=error.get("msg"),
            details={**kwargs},
        )
        for error in errors
    ]
