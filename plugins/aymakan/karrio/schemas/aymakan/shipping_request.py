from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ShippingRequest:
    requested_by: Optional[str]
    declared_value: Optional[int]
    declared_value_currency: Optional[str]
    reference: Optional[str]
    is_cod: Optional[int]
    cod_amount: Optional[int]
    currency: Optional[str]
    delivery_name: Optional[str]
    delivery_email: Optional[str]
    delivery_city: Optional[str]
    delivery_address: Optional[str]
    delivery_neighbourhood: Optional[str]
    delivery_postcode: Optional[int]
    delivery_country: Optional[str]
    delivery_phone: Optional[int]
    delivery_description: Optional[str]
    collection_name: Optional[str]
    collection_email: Optional[str]
    collection_city: Optional[str]
    collection_address: Optional[str]
    collection_neighbourhood: Optional[str]
    collection_postcode: Optional[int]
    collection_country: Optional[str]
    collection_phone: Optional[int]
    collection_description: Optional[str]
    weight: Optional[int]
    pieces: Optional[int]
    items_count: Optional[int]

    def __init__(self, requested_by: Optional[str], declared_value: Optional[int], declared_value_currency: Optional[str], reference: Optional[str], is_cod: Optional[int], cod_amount: Optional[int], currency: Optional[str], delivery_name: Optional[str], delivery_email: Optional[str], delivery_city: Optional[str], delivery_address: Optional[str], delivery_neighbourhood: Optional[str], delivery_postcode: Optional[int], delivery_country: Optional[str], delivery_phone: Optional[int], delivery_description: Optional[str], collection_name: Optional[str], collection_email: Optional[str], collection_city: Optional[str], collection_address: Optional[str], collection_neighbourhood: Optional[str], collection_postcode: Optional[int], collection_country: Optional[str], collection_phone: Optional[int], collection_description: Optional[str], weight: Optional[int], pieces: Optional[int], items_count: Optional[int]) -> None:
        self.requested_by = requested_by
        self.declared_value = declared_value
        self.declared_value_currency = declared_value_currency
        self.reference = reference
        self.is_cod = is_cod
        self.cod_amount = cod_amount
        self.currency = currency
        self.delivery_name = delivery_name
        self.delivery_email = delivery_email
        self.delivery_city = delivery_city
        self.delivery_address = delivery_address
        self.delivery_neighbourhood = delivery_neighbourhood
        self.delivery_postcode = delivery_postcode
        self.delivery_country = delivery_country
        self.delivery_phone = delivery_phone
        self.delivery_description = delivery_description
        self.collection_name = collection_name
        self.collection_email = collection_email
        self.collection_city = collection_city
        self.collection_address = collection_address
        self.collection_neighbourhood = collection_neighbourhood
        self.collection_postcode = collection_postcode
        self.collection_country = collection_country
        self.collection_phone = collection_phone
        self.collection_description = collection_description
        self.weight = weight
        self.pieces = pieces
        self.items_count = items_count

    @staticmethod
    def from_dict(obj: Any) -> 'ShippingRequest':
        assert isinstance(obj, dict)
        requested_by = from_union([from_str, from_none], obj.get("requested_by"))
        declared_value = from_union([from_int, from_none], obj.get("declared_value"))
        declared_value_currency = from_union([from_str, from_none], obj.get("declared_value_currency"))
        reference = from_union([from_str, from_none], obj.get("reference"))
        is_cod = from_union([from_int, from_none], obj.get("is_cod"))
        cod_amount = from_union([from_int, from_none], obj.get("cod_amount"))
        currency = from_union([from_str, from_none], obj.get("currency"))
        delivery_name = from_union([from_str, from_none], obj.get("delivery_name"))
        delivery_email = from_union([from_str, from_none], obj.get("delivery_email"))
        delivery_city = from_union([from_str, from_none], obj.get("delivery_city"))
        delivery_address = from_union([from_str, from_none], obj.get("delivery_address"))
        delivery_neighbourhood = from_union([from_str, from_none], obj.get("delivery_neighbourhood"))
        delivery_postcode = from_union([from_int, from_none], obj.get("delivery_postcode"))
        delivery_country = from_union([from_str, from_none], obj.get("delivery_country"))
        delivery_phone = from_union([from_int, from_none], obj.get("delivery_phone"))
        delivery_description = from_union([from_str, from_none], obj.get("delivery_description"))
        collection_name = from_union([from_str, from_none], obj.get("collection_name"))
        collection_email = from_union([from_str, from_none], obj.get("collection_email"))
        collection_city = from_union([from_str, from_none], obj.get("collection_city"))
        collection_address = from_union([from_str, from_none], obj.get("collection_address"))
        collection_neighbourhood = from_union([from_str, from_none], obj.get("collection_neighbourhood"))
        collection_postcode = from_union([from_int, from_none], obj.get("collection_postcode"))
        collection_country = from_union([from_str, from_none], obj.get("collection_country"))
        collection_phone = from_union([from_int, from_none], obj.get("collection_phone"))
        collection_description = from_union([from_str, from_none], obj.get("collection_description"))
        weight = from_union([from_int, from_none], obj.get("weight"))
        pieces = from_union([from_int, from_none], obj.get("pieces"))
        items_count = from_union([from_int, from_none], obj.get("items_count"))
        return ShippingRequest(requested_by, declared_value, declared_value_currency, reference, is_cod, cod_amount, currency, delivery_name, delivery_email, delivery_city, delivery_address, delivery_neighbourhood, delivery_postcode, delivery_country, delivery_phone, delivery_description, collection_name, collection_email, collection_city, collection_address, collection_neighbourhood, collection_postcode, collection_country, collection_phone, collection_description, weight, pieces, items_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.requested_by is not None:
            result["requested_by"] = from_union([from_str, from_none], self.requested_by)
        if self.declared_value is not None:
            result["declared_value"] = from_union([from_int, from_none], self.declared_value)
        if self.declared_value_currency is not None:
            result["declared_value_currency"] = from_union([from_str, from_none], self.declared_value_currency)
        if self.reference is not None:
            result["reference"] = from_union([from_str, from_none], self.reference)
        if self.is_cod is not None:
            result["is_cod"] = from_union([from_int, from_none], self.is_cod)
        if self.cod_amount is not None:
            result["cod_amount"] = from_union([from_int, from_none], self.cod_amount)
        if self.currency is not None:
            result["currency"] = from_union([from_str, from_none], self.currency)
        if self.delivery_name is not None:
            result["delivery_name"] = from_union([from_str, from_none], self.delivery_name)
        if self.delivery_email is not None:
            result["delivery_email"] = from_union([from_str, from_none], self.delivery_email)
        if self.delivery_city is not None:
            result["delivery_city"] = from_union([from_str, from_none], self.delivery_city)
        if self.delivery_address is not None:
            result["delivery_address"] = from_union([from_str, from_none], self.delivery_address)
        if self.delivery_neighbourhood is not None:
            result["delivery_neighbourhood"] = from_union([from_str, from_none], self.delivery_neighbourhood)
        if self.delivery_postcode is not None:
            result["delivery_postcode"] = from_union([from_int, from_none], self.delivery_postcode)
        if self.delivery_country is not None:
            result["delivery_country"] = from_union([from_str, from_none], self.delivery_country)
        if self.delivery_phone is not None:
            result["delivery_phone"] = from_union([from_int, from_none], self.delivery_phone)
        if self.delivery_description is not None:
            result["delivery_description"] = from_union([from_str, from_none], self.delivery_description)
        if self.collection_name is not None:
            result["collection_name"] = from_union([from_str, from_none], self.collection_name)
        if self.collection_email is not None:
            result["collection_email"] = from_union([from_str, from_none], self.collection_email)
        if self.collection_city is not None:
            result["collection_city"] = from_union([from_str, from_none], self.collection_city)
        if self.collection_address is not None:
            result["collection_address"] = from_union([from_str, from_none], self.collection_address)
        if self.collection_neighbourhood is not None:
            result["collection_neighbourhood"] = from_union([from_str, from_none], self.collection_neighbourhood)
        if self.collection_postcode is not None:
            result["collection_postcode"] = from_union([from_int, from_none], self.collection_postcode)
        if self.collection_country is not None:
            result["collection_country"] = from_union([from_str, from_none], self.collection_country)
        if self.collection_phone is not None:
            result["collection_phone"] = from_union([from_int, from_none], self.collection_phone)
        if self.collection_description is not None:
            result["collection_description"] = from_union([from_str, from_none], self.collection_description)
        if self.weight is not None:
            result["weight"] = from_union([from_int, from_none], self.weight)
        if self.pieces is not None:
            result["pieces"] = from_union([from_int, from_none], self.pieces)
        if self.items_count is not None:
            result["items_count"] = from_union([from_int, from_none], self.items_count)
        return result


def shipping_request_from_dict(s: Any) -> ShippingRequest:
    return ShippingRequest.from_dict(s)


def shipping_request_to_dict(x: ShippingRequest) -> Any:
    return to_class(ShippingRequest, x)
