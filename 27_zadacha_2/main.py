import time
from typing import Callable, Any


def sleep(func: Callable) -> Callable:

    def wrapped_func() -> Any:
        time.sleep(10)
        func_to_call = func()

        return func_to_call

    return wrapped_func


@sleep
def two_plus_two() -> int:
    return 4


@sleep
def five_plus_two() -> int:
    return 7


print(two_plus_two())
print(five_plus_two())
