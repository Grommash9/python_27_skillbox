import traceback
from typing import Callable, Any
import datetime


def overwrite(file):
    counter = 0
    with open(file, 'r') as file_to_read:
        for line in file_to_read:
            counter += 1
    if counter > 200:
        with open(file, 'w') as file_to_write:
            file_to_write.write('')


def error_writer(file: str, func_name: str, error: str) -> None:
    one_line_error = ''
    for letter in error:
        if not letter == '\n':
            one_line_error += letter
    with open(file, 'a') as errors_file:
        final_error_text = f'time: {str(datetime.datetime.now())}  func_name: {func_name} ERROR: {one_line_error}\n'
        errors_file.write(final_error_text)


def logging(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            func_to_call_name = func.__name__
            func_to_call = func(*args, **kwargs)
            return func_to_call
        except:
            error_writer(file='function_errors.log', func_name=func_to_call_name, error=traceback.format_exc())

    return wrapped_func


@logging
def valera_go(number: int) -> float:
    if not isinstance(number, int):
        raise ValueError('Функция валераГоу предназначена только для целых чисел')
    return 10 / number


@logging
def grisha_go(number: int) -> float:
    if not isinstance(number, int):
        raise ValueError('Функция валераГоу предназначена только для целых чисел')
    return 10 / number + 25



numbers_list = [1, 0, 2, 3, 4, 2.3, 0, 6, 2, 9, 0]
for numbers in numbers_list:
    print(valera_go(numbers))
    print(grisha_go(numbers))
