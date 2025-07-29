
import base64
import datetime
import karrio.lib as lib
import karrio.core as core
import karrio.core.errors as errors
import hashlib


class Settings(core.Settings):
    """J&T Express connection settings."""

    # Add carrier specific api connection properties here
    account_number: str = None
    private_key: str

    @property
    def carrier_name(self):
        return "jtexpress"

    @property
    def server_url(self):
        return (
            "https://demoopenapi.jtjms-sa.com"
            if self.test_mode
            else "https://openapi.jtjms-sa.com"
        )

    # """uncomment the following code block to expose a carrier tracking url."""
    # @property
    # def tracking_url(self):
    #     return "https://www.carrier.com/tracking?tracking-id={}"

    def generate_header(self, data:str):
        pair = "%s%s" % (data, self.private_key)
        md5_hash = hashlib.md5(pair.encode()).digest()
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "apiAccount": self.account_number,
            "digest": base64.b64encode(md5_hash).decode("ascii"),
            "user-agent": "Karrio/1.0",
            "timestamp": int(datetime.datetime.utcnow().timestamp())
        }
        return header

    @property
    def connection_config(self) -> lib.units.Options:
        return lib.to_connection_config(
            self.config or {},
            option_type=ConnectionConfig,
        )

class ConnectionConfig(lib.Enum):
    shipping_options = lib.OptionEnum("shipping_options", list)
    shipping_services = lib.OptionEnum("shipping_services", list)
    label_type = lib.OptionEnum("label_type", str, "PDF")  # Example of label type config with PDF default
