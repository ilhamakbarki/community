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


class ErrorResponse:
    code: Optional[str]
    msg: Optional[str]

    def __init__(self, code: Optional[str], msg: Optional[str]) -> None:
        self.code = code
        self.msg = msg

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorResponse':
        assert isinstance(obj, dict)
        code = from_union([from_str, from_none], obj.get("code"))
        msg = from_union([from_str, from_none], obj.get("msg"))
        return ErrorResponse(code, msg)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.code is not None:
            result["code"] = from_union([from_str, from_none], self.code)
        if self.msg is not None:
            result["msg"] = from_union([from_str, from_none], self.msg)
        return result


def error_response_from_dict(s: Any) -> ErrorResponse:
    return ErrorResponse.from_dict(s)


def error_response_to_dict(x: ErrorResponse) -> Any:
    return to_class(ErrorResponse, x)
