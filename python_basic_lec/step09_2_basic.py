# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 기존 문법
def two_args(func):
    def wrapper(a, b):
        return func(a * 3, b * 3)

    return wrapper

def multiple(a, b):
    return a * b

if __name__ == "__main__":
    new_multiple = two_args(multiple)
    print(new_multiple(2, 3))

