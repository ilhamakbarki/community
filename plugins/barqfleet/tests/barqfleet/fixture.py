"""Barqfleet carrier tests fixtures."""

import karrio.sdk as karrio


gateway = karrio.gateway["barqfleet"].create(
    dict(
        id="123456789",
        test_mode=True,
        carrier_id="barqfleet",
        account_number="123456789",
        api_key="TEST_API_KEY",
    )
)