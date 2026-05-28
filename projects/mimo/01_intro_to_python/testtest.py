# Every Python keyword used at least once (Python 3.12+)

import math
from os import path as p

GLOBAL_VAR = 100

class Example:
    class_var = "hello"

    def __init__(self, value):
        self.value = value

    async def async_method(self):
        return self.value

    def generator(self):
        yield self.value

    @staticmethod
    def static():
        return None


async def async_func():
    return await Example(5).async_method()


def outer():
    nonlocal_var = "outer"

    def inner():
        nonlocal nonlocal_var
        nonlocal_var = "changed"
        return nonlocal_var

    return inner()


def keyword_demo():
    global GLOBAL_VAR

    assert GLOBAL_VAR == 100

    if GLOBAL_VAR > 50:
        pass
    elif GLOBAL_VAR < 50:
        pass
    else:
        pass

    for i in range(3):
        if i == 1:
            continue
        if i == 2:
            break

    while False:
        pass

    try:
        x = 1 / 1
    except ZeroDivisionError:
        raise
    finally:
        del x

    with open(__file__, "r") as f:
        data = f.read()

    return data


lambda_func = lambda x: x * 2

a = True
b = False

result = a and not b or False

numbers = [1, 2, 3]

squares = [n * n for n in numbers]

match numbers:
    case [1, 2, 3]:
        matched = True
    case _:
        matched = False

obj = Example(10)

is_instance = isinstance(obj, Example)
contains = 2 in numbers

try:
    exec("temp = 5")
except Exception:
    temp = None

# walrus operator
if (n := 5) > 0:
    value = n

# type alias
type MyType = int | str

# using yield from
def delegator():
    yield from obj.generator()

# None keyword
nothing = None

print("Done")
