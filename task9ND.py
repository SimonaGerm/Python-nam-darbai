"""Create a decorator called debug that will display information about the
function name, the parameters passed, and the result returned when
calling the function."""
import inspect

def debug(deb_func):
    def wrapper (*args, **kwargs):
        return f'Function {deb_func.__name__}({inspect.signature(deb_func)}) returned {deb_func(*args, **kwargs)}'
    return wrapper


@debug
def func(a, b, c):
    return a + b * c


print(func(3, b=2, c=4))

# Kaip išspausdinti paduotus parametrus, ne default?