from typing import Callable, Any

#выводится с лишней запятой, но если её исправлять то будет куча костылей, как
# сделать печать кортежа без этой запятой я пока не знаю


def debug(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        args_tuple = tuple(element for element in args)
        kwargs_tuple = tuple(element for element in kwargs.items())
        total_agruments_tuple = args_tuple + kwargs_tuple
        print(f'Вызывается {func.__name__}{total_agruments_tuple}')
        func_to_call = func(*args, **kwargs)
        print(f'{func.__name__} вернула значение: {func_to_call}')
        return func_to_call

    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!\n".format(name=name, age=age)
    else:
        return "Привет, {name}!\n".format(name=name)


print(greeting('Том'))
print(greeting('Миша', age=100))
print(greeting(name='Катя', age=16))
