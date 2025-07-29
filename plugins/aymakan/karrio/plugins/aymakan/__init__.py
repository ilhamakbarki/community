from karrio.core.metadata import PluginMetadata

from karrio.mappers.aymakan.mapper import Mapper
from karrio.mappers.aymakan.proxy import Proxy
from karrio.mappers.aymakan.settings import Settings
import karrio.providers.aymakan.units as units
import karrio.providers.aymakan.utils as utils


# This METADATA object is used by Karrio to discover and register this plugin
# when loaded through Python entrypoints or local plugin directories.
# The entrypoint is defined in pyproject.toml under [project.entry-points."karrio.plugins"]
METADATA = PluginMetadata(
    id="aymakan",
    label="Aymakan",
    description="Aymakan shipping integration for Karrio",
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
