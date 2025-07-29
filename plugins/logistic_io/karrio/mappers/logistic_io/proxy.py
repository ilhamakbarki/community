"""Karrio Logistic IO client proxy."""

import karrio.lib as lib
import karrio.api.proxy as proxy
import karrio.mappers.logistic_io.settings as provider_settings

class Proxy(proxy.Proxy):
    settings: provider_settings.Settings
    def get_tracking(self, request: lib.Serializable) -> lib.Deserializable[str]:
        cp_awb = request.serialize()["cp_awb"]
        default_header = self.settings.generate_header
        response = lib.request(
            url=f"{self.settings.server_url}/auth/api/v1/awb/track-order-updates?cp_awb={cp_awb}",
            trace=self.trace_as("json"),
            method="GET",
            headers=default_header,
        )
        return lib.Deserializable(response, lib.to_dict)
