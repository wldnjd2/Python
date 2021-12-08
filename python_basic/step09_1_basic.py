# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Decorator를 이해하기 위해서는 앞에서 계속 설명해왔던 4가지 개념을 이해해야 함
"""
1. 객체로서의 함수
2. Nested 함수
3. Nonlocal Variable
4. Closures
"""

"""
@two_args
def add(a, b):
    return a + b

if __name__ == "__main__":
    multiply(1, 5)
"""

def add(a, b):
    return a + b

"""
def two_args(func): # 그저 함수
    return func
"""

"""
def two_args(func):
    # 새로운 함수
    def wrapper(a, b):

        # 수정전의 함수 반환
        return func(a, b)

    # 새로운 함수 반환
    return wrapper
"""

def two_args(func):
    # 새로운 함수
    def wrapper(a, b):

        # 수정전의 함수 반환
        return func(a * 2, b * 2)

    # 새로운 함수 반환
    return wrapper

if __name__ == "__main__":
    new_add = two_args(add)
    print(new_add(1, 2))


