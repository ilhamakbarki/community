from typing import Optional, Any, List, TypeVar, Type, Callable, cast


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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Detail:
    scan_time: Optional[str]
    desc: Optional[str]
    scan_type: Optional[str]
    scan_type_code: Optional[int]
    scan_network_name: Optional[str]
    scan_network_id: Optional[int]
    staff_name: Optional[str]
    staff_contact: Optional[str]
    scan_network_contact: Optional[str]
    scan_network_province: Optional[str]
    scan_network_city: Optional[str]
    scan_network_area: Optional[str]
    next_stop_name: Optional[str]
    next_network_province_name: Optional[str]
    next_network_city_name: Optional[str]
    next_network_area_name: Optional[str]
    sig_pic_url: Optional[str]
    electronic_signature_pic_url: Optional[str]
    longitude: Optional[int]
    latitude: Optional[int]
    otp: Optional[str]
    problem_pic_url: Optional[str]
    second_level_type_code: Optional[int]
    arrival_pic_url: Optional[str]

    def __init__(self, scan_time: Optional[str], desc: Optional[str], scan_type: Optional[str], scan_type_code: Optional[int], scan_network_name: Optional[str], scan_network_id: Optional[int], staff_name: Optional[str], staff_contact: Optional[str], scan_network_contact: Optional[str], scan_network_province: Optional[str], scan_network_city: Optional[str], scan_network_area: Optional[str], next_stop_name: Optional[str], next_network_province_name: Optional[str], next_network_city_name: Optional[str], next_network_area_name: Optional[str], sig_pic_url: Optional[str], electronic_signature_pic_url: Optional[str], longitude: Optional[int], latitude: Optional[int], otp: Optional[str], problem_pic_url: Optional[str], second_level_type_code: Optional[int], arrival_pic_url: Optional[str]) -> None:
        self.scan_time = scan_time
        self.desc = desc
        self.scan_type = scan_type
        self.scan_type_code = scan_type_code
        self.scan_network_name = scan_network_name
        self.scan_network_id = scan_network_id
        self.staff_name = staff_name
        self.staff_contact = staff_contact
        self.scan_network_contact = scan_network_contact
        self.scan_network_province = scan_network_province
        self.scan_network_city = scan_network_city
        self.scan_network_area = scan_network_area
        self.next_stop_name = next_stop_name
        self.next_network_province_name = next_network_province_name
        self.next_network_city_name = next_network_city_name
        self.next_network_area_name = next_network_area_name
        self.sig_pic_url = sig_pic_url
        self.electronic_signature_pic_url = electronic_signature_pic_url
        self.longitude = longitude
        self.latitude = latitude
        self.otp = otp
        self.problem_pic_url = problem_pic_url
        self.second_level_type_code = second_level_type_code
        self.arrival_pic_url = arrival_pic_url

    @staticmethod
    def from_dict(obj: Any) -> 'Detail':
        assert isinstance(obj, dict)
        scan_time = from_union([from_str, from_none], obj.get("scanTime"))
        desc = from_union([from_str, from_none], obj.get("desc"))
        scan_type = from_union([from_str, from_none], obj.get("scanType"))
        scan_type_code = from_union([from_none, lambda x: int(from_str(x))], obj.get("scanTypeCode"))
        scan_network_name = from_union([from_str, from_none], obj.get("scanNetworkName"))
        scan_network_id = from_union([from_int, from_none], obj.get("scanNetworkId"))
        staff_name = from_union([from_str, from_none], obj.get("staffName"))
        staff_contact = from_union([from_str, from_none], obj.get("staffContact"))
        scan_network_contact = from_union([from_str, from_none], obj.get("scanNetworkContact"))
        scan_network_province = from_union([from_str, from_none], obj.get("scanNetworkProvince"))
        scan_network_city = from_union([from_str, from_none], obj.get("scanNetworkCity"))
        scan_network_area = from_union([from_str, from_none], obj.get("scanNetworkArea"))
        next_stop_name = from_union([from_str, from_none], obj.get("nextStopName"))
        next_network_province_name = from_union([from_str, from_none], obj.get("nextNetworkProvinceName"))
        next_network_city_name = from_union([from_str, from_none], obj.get("nextNetworkCityName"))
        next_network_area_name = from_union([from_str, from_none], obj.get("nextNetworkAreaName"))
        sig_pic_url = from_union([from_str, from_none], obj.get("sigPicUrl"))
        electronic_signature_pic_url = from_union([from_str, from_none], obj.get("electronicSignaturePicUrl"))
        longitude = from_union([from_int, from_none], obj.get("longitude"))
        latitude = from_union([from_int, from_none], obj.get("latitude"))
        otp = from_union([from_str, from_none], obj.get("otp"))
        problem_pic_url = from_union([from_str, from_none], obj.get("problemPicUrl"))
        second_level_type_code = from_union([from_none, lambda x: int(from_str(x))], obj.get("secondLevelTypeCode"))
        arrival_pic_url = from_union([from_str, from_none], obj.get("arrivalPicUrl"))
        return Detail(scan_time, desc, scan_type, scan_type_code, scan_network_name, scan_network_id, staff_name, staff_contact, scan_network_contact, scan_network_province, scan_network_city, scan_network_area, next_stop_name, next_network_province_name, next_network_city_name, next_network_area_name, sig_pic_url, electronic_signature_pic_url, longitude, latitude, otp, problem_pic_url, second_level_type_code, arrival_pic_url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.scan_time is not None:
            result["scanTime"] = from_union([from_str, from_none], self.scan_time)
        if self.desc is not None:
            result["desc"] = from_union([from_str, from_none], self.desc)
        if self.scan_type is not None:
            result["scanType"] = from_union([from_str, from_none], self.scan_type)
        if self.scan_type_code is not None:
            result["scanTypeCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.scan_type_code)
        if self.scan_network_name is not None:
            result["scanNetworkName"] = from_union([from_str, from_none], self.scan_network_name)
        if self.scan_network_id is not None:
            result["scanNetworkId"] = from_union([from_int, from_none], self.scan_network_id)
        if self.staff_name is not None:
            result["staffName"] = from_union([from_str, from_none], self.staff_name)
        if self.staff_contact is not None:
            result["staffContact"] = from_union([from_str, from_none], self.staff_contact)
        if self.scan_network_contact is not None:
            result["scanNetworkContact"] = from_union([from_str, from_none], self.scan_network_contact)
        if self.scan_network_province is not None:
            result["scanNetworkProvince"] = from_union([from_str, from_none], self.scan_network_province)
        if self.scan_network_city is not None:
            result["scanNetworkCity"] = from_union([from_str, from_none], self.scan_network_city)
        if self.scan_network_area is not None:
            result["scanNetworkArea"] = from_union([from_str, from_none], self.scan_network_area)
        if self.next_stop_name is not None:
            result["nextStopName"] = from_union([from_str, from_none], self.next_stop_name)
        if self.next_network_province_name is not None:
            result["nextNetworkProvinceName"] = from_union([from_str, from_none], self.next_network_province_name)
        if self.next_network_city_name is not None:
            result["nextNetworkCityName"] = from_union([from_str, from_none], self.next_network_city_name)
        if self.next_network_area_name is not None:
            result["nextNetworkAreaName"] = from_union([from_str, from_none], self.next_network_area_name)
        if self.sig_pic_url is not None:
            result["sigPicUrl"] = from_union([from_str, from_none], self.sig_pic_url)
        if self.electronic_signature_pic_url is not None:
            result["electronicSignaturePicUrl"] = from_union([from_str, from_none], self.electronic_signature_pic_url)
        if self.longitude is not None:
            result["longitude"] = from_union([from_int, from_none], self.longitude)
        if self.latitude is not None:
            result["latitude"] = from_union([from_int, from_none], self.latitude)
        if self.otp is not None:
            result["otp"] = from_union([from_str, from_none], self.otp)
        if self.problem_pic_url is not None:
            result["problemPicUrl"] = from_union([from_str, from_none], self.problem_pic_url)
        if self.second_level_type_code is not None:
            result["secondLevelTypeCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.second_level_type_code)
        if self.arrival_pic_url is not None:
            result["arrivalPicUrl"] = from_union([from_str, from_none], self.arrival_pic_url)
        return result


class Datum:
    bill_code: Optional[str]
    details: Optional[List[Detail]]

    def __init__(self, bill_code: Optional[str], details: Optional[List[Detail]]) -> None:
        self.bill_code = bill_code
        self.details = details

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        bill_code = from_union([from_str, from_none], obj.get("billCode"))
        details = from_union([lambda x: from_list(Detail.from_dict, x), from_none], obj.get("details"))
        return Datum(bill_code, details)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bill_code is not None:
            result["billCode"] = from_union([from_str, from_none], self.bill_code)
        if self.details is not None:
            result["details"] = from_union([lambda x: from_list(lambda x: to_class(Detail, x), x), from_none], self.details)
        return result


class TrackingResponse:
    code: Optional[int]
    msg: Optional[str]
    data: Optional[List[Datum]]

    def __init__(self, code: Optional[int], msg: Optional[str], data: Optional[List[Datum]]) -> None:
        self.code = code
        self.msg = msg
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingResponse':
        assert isinstance(obj, dict)
        code = from_union([from_none, lambda x: int(from_str(x))], obj.get("code"))
        msg = from_union([from_str, from_none], obj.get("msg"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        return TrackingResponse(code, msg, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.code is not None:
            result["code"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.code)
        if self.msg is not None:
            result["msg"] = from_union([from_str, from_none], self.msg)
        if self.data is not None:
            result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        return result


def tracking_response_from_dict(s: Any) -> TrackingResponse:
    return TrackingResponse.from_dict(s)


def tracking_response_to_dict(x: TrackingResponse) -> Any:
    return to_class(TrackingResponse, x)
