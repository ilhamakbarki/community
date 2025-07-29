from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class CustomerDetails:
    name: Optional[str]
    phone: Optional[int]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]

    def __init__(self, name: Optional[str], phone: Optional[int], address: Optional[str], city: Optional[str], state: Optional[str], country: Optional[str], postal_code: Optional[str]) -> None:
        self.name = name
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code

    @staticmethod
    def from_dict(obj: Any) -> 'CustomerDetails':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        phone = from_union([from_none, lambda x: int(from_str(x))], obj.get("phone"))
        address = from_union([from_str, from_none], obj.get("address"))
        city = from_union([from_str, from_none], obj.get("city"))
        state = from_union([from_str, from_none], obj.get("state"))
        country = from_union([from_str, from_none], obj.get("country"))
        postal_code = from_union([from_str, from_none], obj.get("postal_code"))
        return CustomerDetails(name, phone, address, city, state, country, postal_code)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.phone is not None:
            result["phone"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.phone)
        if self.address is not None:
            result["address"] = from_union([from_str, from_none], self.address)
        if self.city is not None:
            result["city"] = from_union([from_str, from_none], self.city)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.country is not None:
            result["country"] = from_union([from_str, from_none], self.country)
        if self.postal_code is not None:
            result["postal_code"] = from_union([from_str, from_none], self.postal_code)
        return result


class CurrentStage:
    stage: Optional[str]
    date: Optional[str]
    alpha_status_code: Optional[int]

    def __init__(self, stage: Optional[str], date: Optional[str], alpha_status_code: Optional[int]) -> None:
        self.stage = stage
        self.date = date
        self.alpha_status_code = alpha_status_code

    @staticmethod
    def from_dict(obj: Any) -> 'CurrentStage':
        assert isinstance(obj, dict)
        stage = from_union([from_str, from_none], obj.get("stage"))
        date = from_union([from_str, from_none], obj.get("date"))
        alpha_status_code = from_union([from_int, from_none], obj.get("alpha_status_code"))
        return CurrentStage(stage, date, alpha_status_code)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.stage is not None:
            result["stage"] = from_union([from_str, from_none], self.stage)
        if self.date is not None:
            result["date"] = from_union([from_str, from_none], self.date)
        if self.alpha_status_code is not None:
            result["alpha_status_code"] = from_union([from_int, from_none], self.alpha_status_code)
        return result


class OrderDetails:
    brand_reference_number: Optional[str]
    created_date: Optional[str]
    delivery_date: None
    current_stage: Optional[CurrentStage]

    def __init__(self, brand_reference_number: Optional[str], created_date: Optional[str], delivery_date: None, current_stage: Optional[CurrentStage]) -> None:
        self.brand_reference_number = brand_reference_number
        self.created_date = created_date
        self.delivery_date = delivery_date
        self.current_stage = current_stage

    @staticmethod
    def from_dict(obj: Any) -> 'OrderDetails':
        assert isinstance(obj, dict)
        brand_reference_number = from_union([from_str, from_none], obj.get("brand_reference_number"))
        created_date = from_union([from_str, from_none], obj.get("created_date"))
        delivery_date = from_none(obj.get("delivery_date"))
        current_stage = from_union([CurrentStage.from_dict, from_none], obj.get("current-stage"))
        return OrderDetails(brand_reference_number, created_date, delivery_date, current_stage)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.brand_reference_number is not None:
            result["brand_reference_number"] = from_union([from_str, from_none], self.brand_reference_number)
        if self.created_date is not None:
            result["created_date"] = from_union([from_str, from_none], self.created_date)
        if self.delivery_date is not None:
            result["delivery_date"] = from_none(self.delivery_date)
        if self.current_stage is not None:
            result["current-stage"] = from_union([lambda x: to_class(CurrentStage, x), from_none], self.current_stage)
        return result


class Update:
    status: Optional[str]
    alpha_status_code: Optional[int]
    date: Optional[str]
    created_date: Optional[str]
    scanned_location: Optional[str]
    status_remark: Optional[str]
    additional_remark: Optional[str]

    def __init__(self, status: Optional[str], alpha_status_code: Optional[int], date: Optional[str], created_date: Optional[str], scanned_location: Optional[str], status_remark: Optional[str], additional_remark: Optional[str]) -> None:
        self.status = status
        self.alpha_status_code = alpha_status_code
        self.date = date
        self.created_date = created_date
        self.scanned_location = scanned_location
        self.status_remark = status_remark
        self.additional_remark = additional_remark

    @staticmethod
    def from_dict(obj: Any) -> 'Update':
        assert isinstance(obj, dict)
        status = from_union([from_str, from_none], obj.get("status"))
        alpha_status_code = from_union([from_int, from_none], obj.get("alpha_status_code"))
        date = from_union([from_str, from_none], obj.get("date"))
        created_date = from_union([from_str, from_none], obj.get("created_date"))
        scanned_location = from_union([from_none, from_str], obj.get("scanned_location"))
        status_remark = from_union([from_str, from_none], obj.get("status_remark"))
        additional_remark = from_union([from_none, from_str], obj.get("additional_remark"))
        return Update(status, alpha_status_code, date, created_date, scanned_location, status_remark, additional_remark)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.alpha_status_code is not None:
            result["alpha_status_code"] = from_union([from_int, from_none], self.alpha_status_code)
        if self.date is not None:
            result["date"] = from_union([from_str, from_none], self.date)
        if self.created_date is not None:
            result["created_date"] = from_union([from_str, from_none], self.created_date)
        if self.scanned_location is not None:
            result["scanned_location"] = from_union([from_none, from_str], self.scanned_location)
        if self.status_remark is not None:
            result["status_remark"] = from_union([from_str, from_none], self.status_remark)
        if self.additional_remark is not None:
            result["additional_remark"] = from_union([from_none, from_str], self.additional_remark)
        return result


class TrackingHistory:
    updates: Optional[List[Update]]

    def __init__(self, updates: Optional[List[Update]]) -> None:
        self.updates = updates

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingHistory':
        assert isinstance(obj, dict)
        updates = from_union([lambda x: from_list(Update.from_dict, x), from_none], obj.get("updates"))
        return TrackingHistory(updates)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.updates is not None:
            result["updates"] = from_union([lambda x: from_list(lambda x: to_class(Update, x), x), from_none], self.updates)
        return result


class Datum:
    referance_awb: Optional[str]
    cp_awb: Optional[str]
    is_mps: Optional[bool]
    box_count: None
    allocated_courier_partner: Optional[str]
    customer_details: Optional[CustomerDetails]
    order_details: Optional[OrderDetails]
    tracking_history: Optional[TrackingHistory]

    def __init__(self, referance_awb: Optional[str], cp_awb: Optional[str], is_mps: Optional[bool], box_count: None, allocated_courier_partner: Optional[str], customer_details: Optional[CustomerDetails], order_details: Optional[OrderDetails], tracking_history: Optional[TrackingHistory]) -> None:
        self.referance_awb = referance_awb
        self.cp_awb = cp_awb
        self.is_mps = is_mps
        self.box_count = box_count
        self.allocated_courier_partner = allocated_courier_partner
        self.customer_details = customer_details
        self.order_details = order_details
        self.tracking_history = tracking_history

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        referance_awb = from_union([from_str, from_none], obj.get("referance_awb"))
        cp_awb = from_union([from_str, from_none], obj.get("cp_awb"))
        is_mps = from_union([from_bool, from_none], obj.get("is_mps"))
        box_count = from_none(obj.get("box_count"))
        allocated_courier_partner = from_union([from_str, from_none], obj.get("allocated_courier_partner"))
        customer_details = from_union([CustomerDetails.from_dict, from_none], obj.get("customer_details"))
        order_details = from_union([OrderDetails.from_dict, from_none], obj.get("order_details"))
        tracking_history = from_union([TrackingHistory.from_dict, from_none], obj.get("tracking_history"))
        return Datum(referance_awb, cp_awb, is_mps, box_count, allocated_courier_partner, customer_details, order_details, tracking_history)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.referance_awb is not None:
            result["referance_awb"] = from_union([from_str, from_none], self.referance_awb)
        if self.cp_awb is not None:
            result["cp_awb"] = from_union([from_str, from_none], self.cp_awb)
        if self.is_mps is not None:
            result["is_mps"] = from_union([from_bool, from_none], self.is_mps)
        if self.box_count is not None:
            result["box_count"] = from_none(self.box_count)
        if self.allocated_courier_partner is not None:
            result["allocated_courier_partner"] = from_union([from_str, from_none], self.allocated_courier_partner)
        if self.customer_details is not None:
            result["customer_details"] = from_union([lambda x: to_class(CustomerDetails, x), from_none], self.customer_details)
        if self.order_details is not None:
            result["order_details"] = from_union([lambda x: to_class(OrderDetails, x), from_none], self.order_details)
        if self.tracking_history is not None:
            result["tracking_history"] = from_union([lambda x: to_class(TrackingHistory, x), from_none], self.tracking_history)
        return result


class TrackingResponse:
    status: Optional[bool]
    data: Optional[List[Datum]]

    def __init__(self, status: Optional[bool], data: Optional[List[Datum]]) -> None:
        self.status = status
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingResponse':
        assert isinstance(obj, dict)
        status = from_union([from_bool, from_none], obj.get("status"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        return TrackingResponse(status, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.status is not None:
            result["status"] = from_union([from_bool, from_none], self.status)
        if self.data is not None:
            result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        return result


def tracking_response_from_dict(s: Any) -> TrackingResponse:
    return TrackingResponse.from_dict(s)


def tracking_response_to_dict(x: TrackingResponse) -> Any:
    return to_class(TrackingResponse, x)
