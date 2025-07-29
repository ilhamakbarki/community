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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class TrackingRequest:
    bill_codes: Optional[str]

    def __init__(self, bill_codes: Optional[str]) -> None:
        self.bill_codes = bill_codes

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingRequest':
        assert isinstance(obj, dict)
        bill_codes = from_union([from_str, from_none], obj.get("billCodes"))
        return TrackingRequest(bill_codes)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bill_codes is not None:
            result["billCodes"] = from_union([from_str, from_none], self.bill_codes)
        return result


def tracking_request_from_dict(s: Any) -> TrackingRequest:
    return TrackingRequest.from_dict(s)


def tracking_request_to_dict(x: TrackingRequest) -> Any:
    return to_class(TrackingRequest, x)
