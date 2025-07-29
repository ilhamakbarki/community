from karrio.core.metadata import PluginMetadata

from karrio.mappers.jtexpress.mapper import Mapper
from karrio.mappers.jtexpress.proxy import Proxy
from karrio.mappers.jtexpress.settings import Settings
import karrio.providers.jtexpress.units as units
import karrio.providers.jtexpress.utils as utils


# This METADATA object is used by Karrio to discover and register this plugin
# when loaded through Python entrypoints or local plugin directories.
# The entrypoint is defined in pyproject.toml under [project.entry-points."karrio.plugins"]
METADATA = PluginMetadata(
    id="jtexpress",
    label="J&T Express",
    description="J&T Express shipping integration for Karrio",
    # Integrations
    Mapper=Mapper,
    Proxy=Proxy,
    Settings=Settings,
    # Data Units
    is_hub=False,
    # options=units.ShippingOption,
    # services=units.ShippingService,
    connection_configs=utils.ConnectionConfig,
    # Extra info
    website="",
    documentation="",
)
