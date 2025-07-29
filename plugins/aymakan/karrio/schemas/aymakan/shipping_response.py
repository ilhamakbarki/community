from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class Shipping:
    reference: None
    tracking_number: Optional[str]
    customer_tracking: None
    customer_name: Optional[str]
    requested_by: Optional[str]
    price_set_amount: None
    price_set_amount_incl_tax: None
    tax_amount: None
    tax_rate: None
    cod_amount: Optional[int]
    declared_value: Optional[int]
    declared_value_currency: Optional[str]
    currency: Optional[str]
    delivery_name: Optional[str]
    delivery_email: Optional[str]
    delivery_city: Optional[str]
    delivery_address: Optional[str]
    delivery_neighbourhood: Optional[str]
    delivery_postcode: Optional[int]
    delivery_country: Optional[str]
    delivery_phone: Optional[int]
    delivery_description: None
    collection_name: Optional[str]
    collection_email: Optional[str]
    collection_city: Optional[str]
    collection_address: Optional[str]
    collection_region: None
    collection_postcode: Optional[int]
    collection_country: Optional[str]
    collection_phone: Optional[int]
    collection_description: None
    submission_date: Optional[str]
    pickup_date: None
    received_at: None
    delivery_date: None
    weight: Optional[int]
    pieces: Optional[int]
    items_count: Optional[int]
    status: Optional[str]
    status_label: Optional[str]
    created_at: Optional[str]
    is_reverse_pickup: Optional[int]
    label: Optional[str]
    pdf_label: Optional[str]

    def __init__(self, reference: None, tracking_number: Optional[str], customer_tracking: None, customer_name: Optional[str], requested_by: Optional[str], price_set_amount: None, price_set_amount_incl_tax: None, tax_amount: None, tax_rate: None, cod_amount: Optional[int], declared_value: Optional[int], declared_value_currency: Optional[str], currency: Optional[str], delivery_name: Optional[str], delivery_email: Optional[str], delivery_city: Optional[str], delivery_address: Optional[str], delivery_neighbourhood: Optional[str], delivery_postcode: Optional[int], delivery_country: Optional[str], delivery_phone: Optional[int], delivery_description: None, collection_name: Optional[str], collection_email: Optional[str], collection_city: Optional[str], collection_address: Optional[str], collection_region: None, collection_postcode: Optional[int], collection_country: Optional[str], collection_phone: Optional[int], collection_description: None, submission_date: Optional[str], pickup_date: None, received_at: None, delivery_date: None, weight: Optional[int], pieces: Optional[int], items_count: Optional[int], status: Optional[str], status_label: Optional[str], created_at: Optional[str], is_reverse_pickup: Optional[int], label: Optional[str], pdf_label: Optional[str]) -> None:
        self.reference = reference
        self.tracking_number = tracking_number
        self.customer_tracking = customer_tracking
        self.customer_name = customer_name
        self.requested_by = requested_by
        self.price_set_amount = price_set_amount
        self.price_set_amount_incl_tax = price_set_amount_incl_tax
        self.tax_amount = tax_amount
        self.tax_rate = tax_rate
        self.cod_amount = cod_amount
        self.declared_value = declared_value
        self.declared_value_currency = declared_value_currency
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
        self.collection_region = collection_region
        self.collection_postcode = collection_postcode
        self.collection_country = collection_country
        self.collection_phone = collection_phone
        self.collection_description = collection_description
        self.submission_date = submission_date
        self.pickup_date = pickup_date
        self.received_at = received_at
        self.delivery_date = delivery_date
        self.weight = weight
        self.pieces = pieces
        self.items_count = items_count
        self.status = status
        self.status_label = status_label
        self.created_at = created_at
        self.is_reverse_pickup = is_reverse_pickup
        self.label = label
        self.pdf_label = pdf_label

    @staticmethod
    def from_dict(obj: Any) -> 'Shipping':
        assert isinstance(obj, dict)
        reference = from_none(obj.get("reference"))
        tracking_number = from_union([from_str, from_none], obj.get("tracking_number"))
        customer_tracking = from_none(obj.get("customer_tracking"))
        customer_name = from_union([from_str, from_none], obj.get("customer_name"))
        requested_by = from_union([from_str, from_none], obj.get("requested_by"))
        price_set_amount = from_none(obj.get("price_set_amount"))
        price_set_amount_incl_tax = from_none(obj.get("price_set_amount_incl_tax"))
        tax_amount = from_none(obj.get("tax_amount"))
        tax_rate = from_none(obj.get("tax_rate"))
        cod_amount = from_union([from_int, from_none], obj.get("cod_amount"))
        declared_value = from_union([from_int, from_none], obj.get("declared_value"))
        declared_value_currency = from_union([from_str, from_none], obj.get("declared_value_currency"))
        currency = from_union([from_str, from_none], obj.get("currency"))
        delivery_name = from_union([from_str, from_none], obj.get("delivery_name"))
        delivery_email = from_union([from_str, from_none], obj.get("delivery_email"))
        delivery_city = from_union([from_str, from_none], obj.get("delivery_city"))
        delivery_address = from_union([from_str, from_none], obj.get("delivery_address"))
        delivery_neighbourhood = from_union([from_str, from_none], obj.get("delivery_neighbourhood"))
        delivery_postcode = from_union([from_int, from_none], obj.get("delivery_postcode"))
        delivery_country = from_union([from_str, from_none], obj.get("delivery_country"))
        delivery_phone = from_union([from_int, from_none], obj.get("delivery_phone"))
        delivery_description = from_none(obj.get("delivery_description"))
        collection_name = from_union([from_str, from_none], obj.get("collection_name"))
        collection_email = from_union([from_str, from_none], obj.get("collection_email"))
        collection_city = from_union([from_str, from_none], obj.get("collection_city"))
        collection_address = from_union([from_str, from_none], obj.get("collection_address"))
        collection_region = from_none(obj.get("collection_region"))
        collection_postcode = from_union([from_int, from_none], obj.get("collection_postcode"))
        collection_country = from_union([from_str, from_none], obj.get("collection_country"))
        collection_phone = from_union([from_int, from_none], obj.get("collection_phone"))
        collection_description = from_none(obj.get("collection_description"))
        submission_date = from_union([from_str, from_none], obj.get("submission_date"))
        pickup_date = from_none(obj.get("pickup_date"))
        received_at = from_none(obj.get("received_at"))
        delivery_date = from_none(obj.get("delivery_date"))
        weight = from_union([from_int, from_none], obj.get("weight"))
        pieces = from_union([from_int, from_none], obj.get("pieces"))
        items_count = from_union([from_int, from_none], obj.get("items_count"))
        status = from_union([from_str, from_none], obj.get("status"))
        status_label = from_union([from_str, from_none], obj.get("status_label"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        is_reverse_pickup = from_union([from_int, from_none], obj.get("is_reverse_pickup"))
        label = from_union([from_str, from_none], obj.get("label"))
        pdf_label = from_union([from_str, from_none], obj.get("pdf_label"))
        return Shipping(reference, tracking_number, customer_tracking, customer_name, requested_by, price_set_amount, price_set_amount_incl_tax, tax_amount, tax_rate, cod_amount, declared_value, declared_value_currency, currency, delivery_name, delivery_email, delivery_city, delivery_address, delivery_neighbourhood, delivery_postcode, delivery_country, delivery_phone, delivery_description, collection_name, collection_email, collection_city, collection_address, collection_region, collection_postcode, collection_country, collection_phone, collection_description, submission_date, pickup_date, received_at, delivery_date, weight, pieces, items_count, status, status_label, created_at, is_reverse_pickup, label, pdf_label)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.reference is not None:
            result["reference"] = from_none(self.reference)
        if self.tracking_number is not None:
            result["tracking_number"] = from_union([from_str, from_none], self.tracking_number)
        if self.customer_tracking is not None:
            result["customer_tracking"] = from_none(self.customer_tracking)
        if self.customer_name is not None:
            result["customer_name"] = from_union([from_str, from_none], self.customer_name)
        if self.requested_by is not None:
            result["requested_by"] = from_union([from_str, from_none], self.requested_by)
        if self.price_set_amount is not None:
            result["price_set_amount"] = from_none(self.price_set_amount)
        if self.price_set_amount_incl_tax is not None:
            result["price_set_amount_incl_tax"] = from_none(self.price_set_amount_incl_tax)
        if self.tax_amount is not None:
            result["tax_amount"] = from_none(self.tax_amount)
        if self.tax_rate is not None:
            result["tax_rate"] = from_none(self.tax_rate)
        if self.cod_amount is not None:
            result["cod_amount"] = from_union([from_int, from_none], self.cod_amount)
        if self.declared_value is not None:
            result["declared_value"] = from_union([from_int, from_none], self.declared_value)
        if self.declared_value_currency is not None:
            result["declared_value_currency"] = from_union([from_str, from_none], self.declared_value_currency)
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
            result["delivery_description"] = from_none(self.delivery_description)
        if self.collection_name is not None:
            result["collection_name"] = from_union([from_str, from_none], self.collection_name)
        if self.collection_email is not None:
            result["collection_email"] = from_union([from_str, from_none], self.collection_email)
        if self.collection_city is not None:
            result["collection_city"] = from_union([from_str, from_none], self.collection_city)
        if self.collection_address is not None:
            result["collection_address"] = from_union([from_str, from_none], self.collection_address)
        if self.collection_region is not None:
            result["collection_region"] = from_none(self.collection_region)
        if self.collection_postcode is not None:
            result["collection_postcode"] = from_union([from_int, from_none], self.collection_postcode)
        if self.collection_country is not None:
            result["collection_country"] = from_union([from_str, from_none], self.collection_country)
        if self.collection_phone is not None:
            result["collection_phone"] = from_union([from_int, from_none], self.collection_phone)
        if self.collection_description is not None:
            result["collection_description"] = from_none(self.collection_description)
        if self.submission_date is not None:
            result["submission_date"] = from_union([from_str, from_none], self.submission_date)
        if self.pickup_date is not None:
            result["pickup_date"] = from_none(self.pickup_date)
        if self.received_at is not None:
            result["received_at"] = from_none(self.received_at)
        if self.delivery_date is not None:
            result["delivery_date"] = from_none(self.delivery_date)
        if self.weight is not None:
            result["weight"] = from_union([from_int, from_none], self.weight)
        if self.pieces is not None:
            result["pieces"] = from_union([from_int, from_none], self.pieces)
        if self.items_count is not None:
            result["items_count"] = from_union([from_int, from_none], self.items_count)
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.status_label is not None:
            result["status_label"] = from_union([from_str, from_none], self.status_label)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.is_reverse_pickup is not None:
            result["is_reverse_pickup"] = from_union([from_int, from_none], self.is_reverse_pickup)
        if self.label is not None:
            result["label"] = from_union([from_str, from_none], self.label)
        if self.pdf_label is not None:
            result["pdf_label"] = from_union([from_str, from_none], self.pdf_label)
        return result


class Data:
    shipping: Optional[Shipping]

    def __init__(self, shipping: Optional[Shipping]) -> None:
        self.shipping = shipping

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        shipping = from_union([Shipping.from_dict, from_none], obj.get("shipping"))
        return Data(shipping)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.shipping is not None:
            result["shipping"] = from_union([lambda x: to_class(Shipping, x), from_none], self.shipping)
        return result


class ShippingResponse:
    success: Optional[bool]
    data: Optional[Data]

    def __init__(self, success: Optional[bool], data: Optional[Data]) -> None:
        self.success = success
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'ShippingResponse':
        assert isinstance(obj, dict)
        success = from_union([from_bool, from_none], obj.get("success"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return ShippingResponse(success, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.success is not None:
            result["success"] = from_union([from_bool, from_none], self.success)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def shipping_response_from_dict(s: Any) -> ShippingResponse:
    return ShippingResponse.from_dict(s)


def shipping_response_to_dict(x: ShippingResponse) -> Any:
    return to_class(ShippingResponse, x)
