"""Karrio Barqfleet client proxy."""

import typing
import karrio.lib as lib
import karrio.api.proxy as proxy
import karrio.mappers.barqfleet.settings as provider_settings
import karrio.providers.barqfleet.error as provider_error

class Proxy(proxy.Proxy):
    settings: provider_settings.Settings
    def get_tracking(self, request: lib.Serializable) -> lib.Deserializable[str]:
        default_header = self.settings.generate_header
        def _get_tracking(order_id: str):
            return order_id, lib.request(
                url=f"{self.settings.server_url}/api/v1/merchants/orders/{order_id}/tracking",
                trace=self.trace_as("json"),
                method="GET",
                headers=default_header,
                on_error=provider_error.parse_http_response,
            )

        responses: typing.List[typing.Tuple[str, str]] = lib.run_concurently(
            _get_tracking, request.serialize()
        )
        return lib.Deserializable(
            responses,
            lambda res: [
                (num, lib.to_dict(track)) for num, track in res if any(track.strip())
            ],
        )
