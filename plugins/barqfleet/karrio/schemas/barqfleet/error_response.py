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


class ErrorResponse:
    errors: Optional[str]
    code: Optional[int]

    def __init__(self, errors: Optional[str], code: Optional[int]) -> None:
        self.errors = errors
        self.code = code

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorResponse':
        assert isinstance(obj, dict)
        errors = from_union([from_str, from_none], obj.get("errors"))
        code = from_union([from_int, from_none], obj.get("code"))
        return ErrorResponse(errors, code)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.errors is not None:
            result["errors"] = from_union([from_str, from_none], self.errors)
        if self.code is not None:
            result["code"] = from_union([from_int, from_none], self.code)
        return result


def error_response_from_dict(s: Any) -> ErrorResponse:
    return ErrorResponse.from_dict(s)


def error_response_to_dict(x: ErrorResponse) -> Any:
    return to_class(ErrorResponse, x)
