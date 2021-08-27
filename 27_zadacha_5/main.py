from typing import Callable, Any

counter_records = dict()


def counter(func: Callable) -> Callable:

    def wrapped_func(*args, **kwargs) -> Any:
        func_to_call = func(*args, **kwargs)
        func_name = func.__name__
        if func_name in counter_records:
            counter_records[func_name] += 1
        else:
            counter_records[func_name] = 1
        print(f'На данный момент функция {func_name} была вызвана уже {counter_records[func_name]} раз')

        return func_to_call

    return wrapped_func


@counter
def two_plus_two() -> int:
    return 4


@counter
def valera_go(number) -> int:
    return number * 2


for x in range(10):
    two_plus_two()
    valera_go(2)

for y in range(20):
    valera_go(2)

for keys, values in counter_records.items():
    print(keys, values)
