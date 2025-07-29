# karrio.barqfleet

This package is a Barqfleet extension of the [karrio](https://pypi.org/project/karrio) multi carrier shipping SDK.

## Requirements

`Python 3.11+`

## Installation

```bash
pip install karrio.barqfleet
```

## Usage

```python
import karrio.sdk as karrio
from karrio.mappers.barqfleet.settings import Settings


# Initialize a carrier gateway
barqfleet = karrio.gateway["barqfleet"].create(
    Settings(
        ...
    )
)
```

Check the [Karrio Mutli-carrier SDK docs](https://docs.karrio.io) for Shipping API requests
