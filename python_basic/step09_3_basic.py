# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Decorator 문법
def two_args(func):
    def wrapper(a, b):
        return func(a * 3, b * 3)

    return wrapper

@two_args
def multiple(a, b):
    return a * b

if __name__ == "__main__":
    print(multiple(2, 3))