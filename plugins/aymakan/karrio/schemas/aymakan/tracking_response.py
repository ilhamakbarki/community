from typing import Optional, Any, List, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class TrackingInfo:
    status_code: Optional[str]
    description: Optional[str]
    description_ar: Optional[str]
    created_at: Optional[str]

    def __init__(self, status_code: Optional[str], description: Optional[str], description_ar: Optional[str], created_at: Optional[str]) -> None:
        self.status_code = status_code
        self.description = description
        self.description_ar = description_ar
        self.created_at = created_at

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingInfo':
        assert isinstance(obj, dict)
        status_code = from_union([from_str, from_none], obj.get("status_code"))
        description = from_union([from_str, from_none], obj.get("description"))
        description_ar = from_union([from_none, from_str], obj.get("description_ar"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        return TrackingInfo(status_code, description, description_ar, created_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.status_code is not None:
            result["status_code"] = from_union([from_str, from_none], self.status_code)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.description_ar is not None:
            result["description_ar"] = from_union([from_none, from_str], self.description_ar)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        return result


class Shipment:
    reference: Optional[int]
    tracking_number: Optional[int]
    customer_tracking: None
    customer_name: Optional[str]
    requested_by: Optional[str]
    cod_amount: Optional[str]
    declared_value: None
    declared_value_currency: None
    currency: Optional[str]
    delivery_name: Optional[str]
    delivery_email: None
    delivery_city: Optional[str]
    delivery_address: Optional[str]
    delivery_region: None
    delivery_postcode: None
    delivery_country: Optional[str]
    delivery_phone: Optional[int]
    delivery_description: None
    collection_name: Optional[str]
    collection_email: None
    collection_city: Optional[str]
    collection_address: None
    collection_region: None
    collection_postcode: None
    collection_country: Optional[str]
    collection_phone: Optional[int]
    collection_description: None
    submission_date: Optional[str]
    pickup_date: Optional[str]
    received_at: None
    delivery_date: Optional[str]
    weight: Optional[str]
    pieces: Optional[int]
    items_count: Optional[int]
    status: Optional[str]
    status_label: Optional[str]
    reason_en: None
    reason_ar: None
    created_at: Optional[str]
    id_customer: Optional[int]
    is_reverse_pickup: Optional[int]
    tracking_info: Optional[List[TrackingInfo]]

    def __init__(self, reference: Optional[int], tracking_number: Optional[int], customer_tracking: None, customer_name: Optional[str], requested_by: Optional[str], cod_amount: Optional[str], declared_value: None, declared_value_currency: None, currency: Optional[str], delivery_name: Optional[str], delivery_email: None, delivery_city: Optional[str], delivery_address: Optional[str], delivery_region: None, delivery_postcode: None, delivery_country: Optional[str], delivery_phone: Optional[int], delivery_description: None, collection_name: Optional[str], collection_email: None, collection_city: Optional[str], collection_address: None, collection_region: None, collection_postcode: None, collection_country: Optional[str], collection_phone: Optional[int], collection_description: None, submission_date: Optional[str], pickup_date: Optional[str], received_at: None, delivery_date: Optional[str], weight: Optional[str], pieces: Optional[int], items_count: Optional[int], status: Optional[str], status_label: Optional[str], reason_en: None, reason_ar: None, created_at: Optional[str], id_customer: Optional[int], is_reverse_pickup: Optional[int], tracking_info: Optional[List[TrackingInfo]]) -> None:
        self.reference = reference
        self.tracking_number = tracking_number
        self.customer_tracking = customer_tracking
        self.customer_name = customer_name
        self.requested_by = requested_by
        self.cod_amount = cod_amount
        self.declared_value = declared_value
        self.declared_value_currency = declared_value_currency
        self.currency = currency
        self.delivery_name = delivery_name
        self.delivery_email = delivery_email
        self.delivery_city = delivery_city
        self.delivery_address = delivery_address
        self.delivery_region = delivery_region
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
        self.reason_en = reason_en
        self.reason_ar = reason_ar
        self.created_at = created_at
        self.id_customer = id_customer
        self.is_reverse_pickup = is_reverse_pickup
        self.tracking_info = tracking_info

    @staticmethod
    def from_dict(obj: Any) -> 'Shipment':
        assert isinstance(obj, dict)
        reference = from_union([from_none, lambda x: int(from_str(x))], obj.get("reference"))
        tracking_number = from_union([from_none, lambda x: int(from_str(x))], obj.get("tracking_number"))
        customer_tracking = from_none(obj.get("customer_tracking"))
        customer_name = from_union([from_str, from_none], obj.get("customer_name"))
        requested_by = from_union([from_str, from_none], obj.get("requested_by"))
        cod_amount = from_union([from_str, from_none], obj.get("cod_amount"))
        declared_value = from_none(obj.get("declared_value"))
        declared_value_currency = from_none(obj.get("declared_value_currency"))
        currency = from_union([from_str, from_none], obj.get("currency"))
        delivery_name = from_union([from_str, from_none], obj.get("delivery_name"))
        delivery_email = from_none(obj.get("delivery_email"))
        delivery_city = from_union([from_str, from_none], obj.get("delivery_city"))
        delivery_address = from_union([from_str, from_none], obj.get("delivery_address"))
        delivery_region = from_none(obj.get("delivery_region"))
        delivery_postcode = from_none(obj.get("delivery_postcode"))
        delivery_country = from_union([from_str, from_none], obj.get("delivery_country"))
        delivery_phone = from_union([from_none, lambda x: int(from_str(x))], obj.get("delivery_phone"))
        delivery_description = from_none(obj.get("delivery_description"))
        collection_name = from_union([from_str, from_none], obj.get("collection_name"))
        collection_email = from_none(obj.get("collection_email"))
        collection_city = from_union([from_str, from_none], obj.get("collection_city"))
        collection_address = from_none(obj.get("collection_address"))
        collection_region = from_none(obj.get("collection_region"))
        collection_postcode = from_none(obj.get("collection_postcode"))
        collection_country = from_union([from_str, from_none], obj.get("collection_country"))
        collection_phone = from_union([from_none, lambda x: int(from_str(x))], obj.get("collection_phone"))
        collection_description = from_none(obj.get("collection_description"))
        submission_date = from_union([from_str, from_none], obj.get("submission_date"))
        pickup_date = from_union([from_str, from_none], obj.get("pickup_date"))
        received_at = from_none(obj.get("received_at"))
        delivery_date = from_union([from_str, from_none], obj.get("delivery_date"))
        weight = from_union([from_str, from_none], obj.get("weight"))
        pieces = from_union([from_int, from_none], obj.get("pieces"))
        items_count = from_union([from_int, from_none], obj.get("items_count"))
        status = from_union([from_str, from_none], obj.get("status"))
        status_label = from_union([from_str, from_none], obj.get("status_label"))
        reason_en = from_none(obj.get("reason_en"))
        reason_ar = from_none(obj.get("reason_ar"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        id_customer = from_union([from_int, from_none], obj.get("id_customer"))
        is_reverse_pickup = from_union([from_int, from_none], obj.get("is_reverse_pickup"))
        tracking_info = from_union([lambda x: from_list(TrackingInfo.from_dict, x), from_none], obj.get("tracking_info"))
        return Shipment(reference, tracking_number, customer_tracking, customer_name, requested_by, cod_amount, declared_value, declared_value_currency, currency, delivery_name, delivery_email, delivery_city, delivery_address, delivery_region, delivery_postcode, delivery_country, delivery_phone, delivery_description, collection_name, collection_email, collection_city, collection_address, collection_region, collection_postcode, collection_country, collection_phone, collection_description, submission_date, pickup_date, received_at, delivery_date, weight, pieces, items_count, status, status_label, reason_en, reason_ar, created_at, id_customer, is_reverse_pickup, tracking_info)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.reference is not None:
            result["reference"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.reference)
        if self.tracking_number is not None:
            result["tracking_number"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.tracking_number)
        if self.customer_tracking is not None:
            result["customer_tracking"] = from_none(self.customer_tracking)
        if self.customer_name is not None:
            result["customer_name"] = from_union([from_str, from_none], self.customer_name)
        if self.requested_by is not None:
            result["requested_by"] = from_union([from_str, from_none], self.requested_by)
        if self.cod_amount is not None:
            result["cod_amount"] = from_union([from_str, from_none], self.cod_amount)
        if self.declared_value is not None:
            result["declared_value"] = from_none(self.declared_value)
        if self.declared_value_currency is not None:
            result["declared_value_currency"] = from_none(self.declared_value_currency)
        if self.currency is not None:
            result["currency"] = from_union([from_str, from_none], self.currency)
        if self.delivery_name is not None:
            result["delivery_name"] = from_union([from_str, from_none], self.delivery_name)
        if self.delivery_email is not None:
            result["delivery_email"] = from_none(self.delivery_email)
        if self.delivery_city is not None:
            result["delivery_city"] = from_union([from_str, from_none], self.delivery_city)
        if self.delivery_address is not None:
            result["delivery_address"] = from_union([from_str, from_none], self.delivery_address)
        if self.delivery_region is not None:
            result["delivery_region"] = from_none(self.delivery_region)
        if self.delivery_postcode is not None:
            result["delivery_postcode"] = from_none(self.delivery_postcode)
        if self.delivery_country is not None:
            result["delivery_country"] = from_union([from_str, from_none], self.delivery_country)
        if self.delivery_phone is not None:
            result["delivery_phone"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.delivery_phone)
        if self.delivery_description is not None:
            result["delivery_description"] = from_none(self.delivery_description)
        if self.collection_name is not None:
            result["collection_name"] = from_union([from_str, from_none], self.collection_name)
        if self.collection_email is not None:
            result["collection_email"] = from_none(self.collection_email)
        if self.collection_city is not None:
            result["collection_city"] = from_union([from_str, from_none], self.collection_city)
        if self.collection_address is not None:
            result["collection_address"] = from_none(self.collection_address)
        if self.collection_region is not None:
            result["collection_region"] = from_none(self.collection_region)
        if self.collection_postcode is not None:
            result["collection_postcode"] = from_none(self.collection_postcode)
        if self.collection_country is not None:
            result["collection_country"] = from_union([from_str, from_none], self.collection_country)
        if self.collection_phone is not None:
            result["collection_phone"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.collection_phone)
        if self.collection_description is not None:
            result["collection_description"] = from_none(self.collection_description)
        if self.submission_date is not None:
            result["submission_date"] = from_union([from_str, from_none], self.submission_date)
        if self.pickup_date is not None:
            result["pickup_date"] = from_union([from_str, from_none], self.pickup_date)
        if self.received_at is not None:
            result["received_at"] = from_none(self.received_at)
        if self.delivery_date is not None:
            result["delivery_date"] = from_union([from_str, from_none], self.delivery_date)
        if self.weight is not None:
            result["weight"] = from_union([from_str, from_none], self.weight)
        if self.pieces is not None:
            result["pieces"] = from_union([from_int, from_none], self.pieces)
        if self.items_count is not None:
            result["items_count"] = from_union([from_int, from_none], self.items_count)
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.status_label is not None:
            result["status_label"] = from_union([from_str, from_none], self.status_label)
        if self.reason_en is not None:
            result["reason_en"] = from_none(self.reason_en)
        if self.reason_ar is not None:
            result["reason_ar"] = from_none(self.reason_ar)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.id_customer is not None:
            result["id_customer"] = from_union([from_int, from_none], self.id_customer)
        if self.is_reverse_pickup is not None:
            result["is_reverse_pickup"] = from_union([from_int, from_none], self.is_reverse_pickup)
        if self.tracking_info is not None:
            result["tracking_info"] = from_union([lambda x: from_list(lambda x: to_class(TrackingInfo, x), x), from_none], self.tracking_info)
        return result


class Data:
    shipments: Optional[List[Shipment]]

    def __init__(self, shipments: Optional[List[Shipment]]) -> None:
        self.shipments = shipments

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        shipments = from_union([lambda x: from_list(Shipment.from_dict, x), from_none], obj.get("shipments"))
        return Data(shipments)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.shipments is not None:
            result["shipments"] = from_union([lambda x: from_list(lambda x: to_class(Shipment, x), x), from_none], self.shipments)
        return result


class TrackingResponse:
    success: Optional[bool]
    data: Optional[Data]

    def __init__(self, success: Optional[bool], data: Optional[Data]) -> None:
        self.success = success
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingResponse':
        assert isinstance(obj, dict)
        success = from_union([from_bool, from_none], obj.get("success"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return TrackingResponse(success, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.success is not None:
            result["success"] = from_union([from_bool, from_none], self.success)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def tracking_response_from_dict(s: Any) -> TrackingResponse:
    return TrackingResponse.from_dict(s)


def tracking_response_to_dict(x: TrackingResponse) -> Any:
    return to_class(TrackingResponse, x)
