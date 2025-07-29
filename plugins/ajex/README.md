# karrio.ajex

This package is a Ajex extension of the [karrio](https://pypi.org/project/karrio) multi carrier shipping SDK.

## Requirements

`Python 3.11+`

## Installation

```bash
pip install karrio.ajex
```

## Usage

```python
import karrio.sdk as karrio
from karrio.mappers.ajex.settings import Settings


# Initialize a carrier gateway
ajex = karrio.gateway["ajex"].create(
    Settings(
        ...
    )
)
```

Check the [Karrio Mutli-carrier SDK docs](https://docs.karrio.io) for Shipping API requests
