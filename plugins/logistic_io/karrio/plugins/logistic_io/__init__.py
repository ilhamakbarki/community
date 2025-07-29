from karrio.core.metadata import PluginMetadata

from karrio.mappers.logistic_io.mapper import Mapper
from karrio.mappers.logistic_io.proxy import Proxy
from karrio.mappers.logistic_io.settings import Settings
import karrio.providers.logistic_io.units as units
import karrio.providers.logistic_io.utils as utils


# This METADATA object is used by Karrio to discover and register this plugin
# when loaded through Python entrypoints or local plugin directories.
# The entrypoint is defined in pyproject.toml under [project.entry-points."karrio.plugins"]
METADATA = PluginMetadata(
    id="logistic_io",
    label="Logistic IO",
    description="Logistic IO shipping integration for Karrio",
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
