from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


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


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Cooridnates:
    latitude: Optional[float]
    longitude: Optional[float]

    def __init__(self, latitude: Optional[float], longitude: Optional[float]) -> None:
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def from_dict(obj: Any) -> 'Cooridnates':
        assert isinstance(obj, dict)
        latitude = from_union([from_float, from_none], obj.get("latitude"))
        longitude = from_union([from_float, from_none], obj.get("longitude"))
        return Cooridnates(latitude, longitude)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.latitude is not None:
            result["latitude"] = from_union([to_float, from_none], self.latitude)
        if self.longitude is not None:
            result["longitude"] = from_union([to_float, from_none], self.longitude)
        return result


class TrackingResponseElement:
    code: Optional[int]
    response_id: Optional[str]
    courier: Optional[str]
    cooridnates: Optional[Cooridnates]

    def __init__(self, code: Optional[int], response_id: Optional[str], courier: Optional[str], cooridnates: Optional[Cooridnates]) -> None:
        self.code = code
        self.response_id = response_id
        self.courier = courier
        self.cooridnates = cooridnates

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingResponseElement':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        response_id = from_union([from_str, from_none], obj.get("response_id"))
        courier = from_union([from_str, from_none], obj.get("courier"))
        cooridnates = from_union([Cooridnates.from_dict, from_none], obj.get("cooridnates"))
        return TrackingResponseElement(code, response_id, courier, cooridnates)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.code is not None:
            result["code"] = from_union([from_int, from_none], self.code)
        if self.response_id is not None:
            result["response_id"] = from_union([from_str, from_none], self.response_id)
        if self.courier is not None:
            result["courier"] = from_union([from_str, from_none], self.courier)
        if self.cooridnates is not None:
            result["cooridnates"] = from_union([lambda x: to_class(Cooridnates, x), from_none], self.cooridnates)
        return result


def tracking_response_from_dict(s: Any) -> List[TrackingResponseElement]:
    return from_list(TrackingResponseElement.from_dict, s)


def tracking_response_to_dict(x: List[TrackingResponseElement]) -> Any:
    return from_list(lambda x: to_class(TrackingResponseElement, x), x)
