
import base64
import datetime
import karrio.lib as lib
import karrio.core as core
import karrio.core.errors as errors


class Settings(core.Settings):
    """Ajex connection settings."""

    # Add carrier specific api connection properties here
    username: str
    password: str
    account_country_code: str = None
    id: str

    @property
    def carrier_name(self):
        return "ajex"

    @property
    def server_url(self):
        return (
            "https://apps-sit.aj-ex.com"
            if self.test_mode
            else "https://apps-sit.aj-ex.com"
        )

    # """uncomment the following code block to expose a carrier tracking url."""
    # @property
    # def tracking_url(self):
    #     return "https://www.carrier.com/tracking?tracking-id={}"

    @property
    def access_token(self):
        cache_key = f"{self.carrier_name}|{self.username}|{self.password}"
        now = datetime.datetime.now() + datetime.timedelta(minutes=5)

        auth = self.connection_cache.get(cache_key) or {}
        token = auth.get("access_token")
        expiry = lib.to_date(auth.get("expiry"), current_format="%Y-%m-%d %H:%M:%S")
        if token is not None and expiry is not None and expiry > now:
            return token
        else:
            self.connection_cache.set(cache_key, lambda: login(self))
            new_auth = self.connection_cache.get(cache_key)
            return new_auth["access_token"]

    @property
    def generate_header(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "user-agent": "Karrio/1.0",
        }

def login(settings: Settings):
    import karrio.providers.ajex.error as error

    result = lib.request(
        url=f"{settings.server_url}/authentication-service/api/auth/login",
        method="POST",
        headers={
            "Content-Type": "application/json",
            "user-agent": "Karrio/1.0",
        },
        data=lib.to_json(
            dict(
                username=settings.username,
                password=settings.password,
            )
        ),
    )

    response = lib.to_dict(result)
    messages = error.parse_error_response(response, settings) if response.get("accessToken") is None else []
    if any(messages):
        raise errors.ParsedMessagesError(messages=messages)
    token = response.get("accessToken")
    expiry = datetime.datetime.now() + datetime.timedelta(minutes=30)
    return {
        "access_token": token,
        "expiry": lib.fdatetime(expiry),
    }

class ConnectionConfig(lib.Enum):
    shipping_options = lib.OptionEnum("shipping_options", list)
    shipping_services = lib.OptionEnum("shipping_services", list)
    label_type = lib.OptionEnum("label_type", str, "PDF")  # Example of label type config with PDF default
