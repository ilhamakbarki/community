from typing import Optional, List, Any, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ErrorResponse:
    status: Optional[str]
    message: Optional[str]
    error: Optional[str]
    errors: Optional[List[str]]

    def __init__(self, status: Optional[str], message: Optional[str], error: Optional[str], errors: Optional[List[str]]) -> None:
        self.status = status
        self.message = message
        self.error = error
        self.errors = errors

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorResponse':
        assert isinstance(obj, dict)
        status = from_union([from_str, from_none], obj.get("status"))
        message = from_union([from_str, from_none], obj.get("message"))
        error = from_union([from_str, from_none], obj.get("error"))
        errors = from_union([lambda x: from_list(from_str, x), from_none], obj.get("errors"))
        return ErrorResponse(status, message, error, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.message is not None:
            result["message"] = from_union([from_str, from_none], self.message)
        if self.error is not None:
            result["error"] = from_union([from_str, from_none], self.error)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(from_str, x), from_none], self.errors)
        return result


def error_response_from_dict(s: Any) -> ErrorResponse:
    return ErrorResponse.from_dict(s)


def error_response_to_dict(x: ErrorResponse) -> Any:
    return to_class(ErrorResponse, x)
