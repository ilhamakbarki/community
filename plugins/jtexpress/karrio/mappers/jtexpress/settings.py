"""Karrio J&T Express client settings."""

import attr
import karrio.providers.jtexpress.utils as provider_utils


@attr.s(auto_attribs=True)
class Settings(provider_utils.Settings):
    """J&T Express connection settings."""

    # Add carrier specific API connection properties here
    account_number: str
    private_key: str

    # generic properties
    id: str = None
    test_mode: bool = False
    carrier_id: str = "jtexpress"
    account_country_code: str = None
    metadata: dict = {}
    config: dict = {}
