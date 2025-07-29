from typing import List, Optional, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Errors:
    price_set: Optional[List[str]]
    declared_value: Optional[List[str]]

    def __init__(self, price_set: Optional[List[str]], declared_value: Optional[List[str]]) -> None:
        self.price_set = price_set
        self.declared_value = declared_value

    @staticmethod
    def from_dict(obj: Any) -> 'Errors':
        assert isinstance(obj, dict)
        price_set = from_union([lambda x: from_list(from_str, x), from_none], obj.get("price_set"))
        declared_value = from_union([lambda x: from_list(from_str, x), from_none], obj.get("declared_value"))
        return Errors(price_set, declared_value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.price_set is not None:
            result["price_set"] = from_union([lambda x: from_list(from_str, x), from_none], self.price_set)
        if self.declared_value is not None:
            result["declared_value"] = from_union([lambda x: from_list(from_str, x), from_none], self.declared_value)
        return result


class ErrorResponse:
    error: Optional[bool]
    message: Optional[str]
    errors: Optional[Errors]
    response: Optional[str]

    def __init__(self, error: Optional[bool], message: Optional[str], errors: Optional[Errors], response: Optional[str]) -> None:
        self.error = error
        self.message = message
        self.errors = errors
        self.response = response

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorResponse':
        assert isinstance(obj, dict)
        error = from_union([from_bool, from_none], obj.get("error"))
        message = from_union([from_str, from_none], obj.get("message"))
        errors = from_union([Errors.from_dict, from_none], obj.get("errors"))
        response = from_union([from_str, from_none], obj.get("response"))
        return ErrorResponse(error, message, errors, response)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.error is not None:
            result["error"] = from_union([from_bool, from_none], self.error)
        if self.message is not None:
            result["message"] = from_union([from_str, from_none], self.message)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: to_class(Errors, x), from_none], self.errors)
        if self.response is not None:
            result["response"] = from_union([from_str, from_none], self.response)
        return result


def error_response_from_dict(s: Any) -> ErrorResponse:
    return ErrorResponse.from_dict(s)


def error_response_to_dict(x: ErrorResponse) -> Any:
    return to_class(ErrorResponse, x)
