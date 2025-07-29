"""Karrio J&T Express client proxy."""

import karrio.lib as lib
import karrio.api.proxy as proxy
import karrio.mappers.jtexpress.settings as provider_settings


class Proxy(proxy.Proxy):
    settings: provider_settings.Settings
    def get_tracking(self, request: lib.Serializable) -> lib.Deserializable[str]:
        payload = lib.to_json(request.serialize())
        response = lib.request(
            url=f"{self.settings.server_url}/webopenplatformapi/api/logistics/trace",
            trace=self.trace_as("json"),
            method="POST",
            headers=self.settings.generate_header(payload),
            data=lib.to_query_string({
                "bizContent": payload,
            }),
        )
        return lib.Deserializable(response, lib.to_dict)
