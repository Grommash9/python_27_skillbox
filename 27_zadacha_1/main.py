from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:

    def wrapped_func() -> Any:
        x = input('Как дела?')
        func_to_call = func()

        return func_to_call

    return wrapped_func


@how_are_you
def two_plus_two() -> int:
    return 4


@how_are_you
def five_plus_two() -> int:
    return 7


print(two_plus_two())
print(five_plus_two())
