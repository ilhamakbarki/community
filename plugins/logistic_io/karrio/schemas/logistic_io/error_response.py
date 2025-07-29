from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ErrorResponse:
    status: Optional[bool]
    message: Optional[str]

    def __init__(self, status: Optional[bool], message: Optional[str]) -> None:
        self.status = status
        self.message = message

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorResponse':
        assert isinstance(obj, dict)
        status = from_union([from_bool, from_none], obj.get("status"))
        message = from_union([from_str, from_none], obj.get("message"))
        return ErrorResponse(status, message)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.status is not None:
            result["status"] = from_union([from_bool, from_none], self.status)
        if self.message is not None:
            result["message"] = from_union([from_str, from_none], self.message)
        return result


def error_response_from_dict(s: Any) -> ErrorResponse:
    return ErrorResponse.from_dict(s)


def error_response_to_dict(x: ErrorResponse) -> Any:
    return to_class(ErrorResponse, x)
