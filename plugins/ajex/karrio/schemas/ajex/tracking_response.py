from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


class ErDetails:
    postal_code: None
    city: Optional[str]
    name: Optional[str]
    full_address: Optional[str]

    def __init__(self, postal_code: None, city: Optional[str], name: Optional[str], full_address: Optional[str]) -> None:
        self.postal_code = postal_code
        self.city = city
        self.name = name
        self.full_address = full_address

    @staticmethod
    def from_dict(obj: Any) -> 'ErDetails':
        assert isinstance(obj, dict)
        postal_code = from_none(obj.get("postalCode"))
        city = from_union([from_str, from_none], obj.get("city"))
        name = from_union([from_str, from_none], obj.get("name"))
        full_address = from_union([from_str, from_none], obj.get("fullAddress"))
        return ErDetails(postal_code, city, name, full_address)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.postal_code is not None:
            result["postalCode"] = from_none(self.postal_code)
        if self.city is not None:
            result["city"] = from_union([from_str, from_none], self.city)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.full_address is not None:
            result["fullAddress"] = from_union([from_str, from_none], self.full_address)
        return result


class OrderDetails:
    final_status_code: Optional[int]
    final_status: Optional[str]
    product_name: Optional[str]
    weight: Optional[float]
    actual_amount: Optional[float]
    shippment_date: Optional[str]
    delivery_date: None
    sender_details: Optional[ErDetails]
    receiver_details: Optional[ErDetails]

    def __init__(self, final_status_code: Optional[int], final_status: Optional[str], product_name: Optional[str], weight: Optional[float], actual_amount: Optional[float], shippment_date: Optional[str], delivery_date: None, sender_details: Optional[ErDetails], receiver_details: Optional[ErDetails]) -> None:
        self.final_status_code = final_status_code
        self.final_status = final_status
        self.product_name = product_name
        self.weight = weight
        self.actual_amount = actual_amount
        self.shippment_date = shippment_date
        self.delivery_date = delivery_date
        self.sender_details = sender_details
        self.receiver_details = receiver_details

    @staticmethod
    def from_dict(obj: Any) -> 'OrderDetails':
        assert isinstance(obj, dict)
        final_status_code = from_union([from_int, from_none], obj.get("finalStatusCode"))
        final_status = from_union([from_str, from_none], obj.get("finalStatus"))
        product_name = from_union([from_str, from_none], obj.get("productName"))
        weight = from_union([from_float, from_none], obj.get("weight"))
        actual_amount = from_union([from_float, from_none], obj.get("actualAmount"))
        shippment_date = from_union([from_str, from_none], obj.get("shippmentDate"))
        delivery_date = from_none(obj.get("deliveryDate"))
        sender_details = from_union([ErDetails.from_dict, from_none], obj.get("senderDetails"))
        receiver_details = from_union([ErDetails.from_dict, from_none], obj.get("receiverDetails"))
        return OrderDetails(final_status_code, final_status, product_name, weight, actual_amount, shippment_date, delivery_date, sender_details, receiver_details)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.final_status_code is not None:
            result["finalStatusCode"] = from_union([from_int, from_none], self.final_status_code)
        if self.final_status is not None:
            result["finalStatus"] = from_union([from_str, from_none], self.final_status)
        if self.product_name is not None:
            result["productName"] = from_union([from_str, from_none], self.product_name)
        if self.weight is not None:
            result["weight"] = from_union([to_float, from_none], self.weight)
        if self.actual_amount is not None:
            result["actualAmount"] = from_union([to_float, from_none], self.actual_amount)
        if self.shippment_date is not None:
            result["shippmentDate"] = from_union([from_str, from_none], self.shippment_date)
        if self.delivery_date is not None:
            result["deliveryDate"] = from_none(self.delivery_date)
        if self.sender_details is not None:
            result["senderDetails"] = from_union([lambda x: to_class(ErDetails, x), from_none], self.sender_details)
        if self.receiver_details is not None:
            result["receiverDetails"] = from_union([lambda x: to_class(ErDetails, x), from_none], self.receiver_details)
        return result


class Payment:
    method: Optional[str]
    status: Optional[bool]
    time: Optional[str]
    time_zone: Optional[str]

    def __init__(self, method: Optional[str], status: Optional[bool], time: Optional[str], time_zone: Optional[str]) -> None:
        self.method = method
        self.status = status
        self.time = time
        self.time_zone = time_zone

    @staticmethod
    def from_dict(obj: Any) -> 'Payment':
        assert isinstance(obj, dict)
        method = from_union([from_str, from_none], obj.get("method"))
        status = from_union([from_bool, from_none], obj.get("status"))
        time = from_union([from_str, from_none], obj.get("time"))
        time_zone = from_union([from_str, from_none], obj.get("timeZone"))
        return Payment(method, status, time, time_zone)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.method is not None:
            result["method"] = from_union([from_str, from_none], self.method)
        if self.status is not None:
            result["status"] = from_union([from_bool, from_none], self.status)
        if self.time is not None:
            result["time"] = from_union([from_str, from_none], self.time)
        if self.time_zone is not None:
            result["timeZone"] = from_union([from_str, from_none], self.time_zone)
        return result


class OrderTrackingHistory:
    action_time: Optional[str]
    status: Optional[str]
    status_code: Optional[int]
    note: Optional[str]
    city_name: None
    time_zone: Optional[str]
    payment: Optional[Payment]

    def __init__(self, action_time: Optional[str], status: Optional[str], status_code: Optional[int], note: Optional[str], city_name: None, time_zone: Optional[str], payment: Optional[Payment]) -> None:
        self.action_time = action_time
        self.status = status
        self.status_code = status_code
        self.note = note
        self.city_name = city_name
        self.time_zone = time_zone
        self.payment = payment

    @staticmethod
    def from_dict(obj: Any) -> 'OrderTrackingHistory':
        assert isinstance(obj, dict)
        action_time = from_union([from_str, from_none], obj.get("actionTime"))
        status = from_union([from_str, from_none], obj.get("status"))
        status_code = from_union([from_int, from_none], obj.get("statusCode"))
        note = from_union([from_str, from_none], obj.get("note"))
        city_name = from_none(obj.get("cityName"))
        time_zone = from_union([from_str, from_none], obj.get("timeZone"))
        payment = from_union([Payment.from_dict, from_none], obj.get("payment"))
        return OrderTrackingHistory(action_time, status, status_code, note, city_name, time_zone, payment)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.action_time is not None:
            result["actionTime"] = from_union([from_str, from_none], self.action_time)
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.status_code is not None:
            result["statusCode"] = from_union([from_int, from_none], self.status_code)
        if self.note is not None:
            result["note"] = from_union([from_str, from_none], self.note)
        if self.city_name is not None:
            result["cityName"] = from_none(self.city_name)
        if self.time_zone is not None:
            result["timeZone"] = from_union([from_str, from_none], self.time_zone)
        if self.payment is not None:
            result["payment"] = from_union([lambda x: to_class(Payment, x), from_none], self.payment)
        return result


class TrackingResponse:
    response_code: Optional[int]
    response_message: Optional[str]
    waybill_number: Optional[str]
    order_details: Optional[OrderDetails]
    order_tracking_history: Optional[List[OrderTrackingHistory]]

    def __init__(self, response_code: Optional[int], response_message: Optional[str], waybill_number: Optional[str], order_details: Optional[OrderDetails], order_tracking_history: Optional[List[OrderTrackingHistory]]) -> None:
        self.response_code = response_code
        self.response_message = response_message
        self.waybill_number = waybill_number
        self.order_details = order_details
        self.order_tracking_history = order_tracking_history

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingResponse':
        assert isinstance(obj, dict)
        response_code = from_union([from_none, lambda x: int(from_str(x))], obj.get("responseCode"))
        response_message = from_union([from_str, from_none], obj.get("responseMessage"))
        waybill_number = from_union([from_str, from_none], obj.get("waybillNumber"))
        order_details = from_union([OrderDetails.from_dict, from_none], obj.get("orderDetails"))
        order_tracking_history = from_union([lambda x: from_list(OrderTrackingHistory.from_dict, x), from_none], obj.get("orderTrackingHistory"))
        return TrackingResponse(response_code, response_message, waybill_number, order_details, order_tracking_history)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.response_code is not None:
            result["responseCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.response_code)
        if self.response_message is not None:
            result["responseMessage"] = from_union([from_str, from_none], self.response_message)
        if self.waybill_number is not None:
            result["waybillNumber"] = from_union([from_str, from_none], self.waybill_number)
        if self.order_details is not None:
            result["orderDetails"] = from_union([lambda x: to_class(OrderDetails, x), from_none], self.order_details)
        if self.order_tracking_history is not None:
            result["orderTrackingHistory"] = from_union([lambda x: from_list(lambda x: to_class(OrderTrackingHistory, x), x), from_none], self.order_tracking_history)
        return result


def tracking_response_from_dict(s: Any) -> TrackingResponse:
    return TrackingResponse.from_dict(s)


def tracking_response_to_dict(x: TrackingResponse) -> Any:
    return to_class(TrackingResponse, x)
