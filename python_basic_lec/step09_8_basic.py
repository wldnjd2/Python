# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# (2) 추가
from functools import wraps

# 메타데이터
def print_hello(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        """안녕을 출력하는 데커레이션 함수입니다.""" # (1) 추가
        print('안녕')
        return func(*args, **kwargs)
    return wrapper


# Decorate print_sum() with the add_hello() decorator
@print_hello
def print_add(a, b):
    """덧셈을 출력하는 함수입니다. """
    print(a + b)

if __name__ == "__main__":
    print_add(10, 20)
    print_sum_docstring = print_add.__doc__
    print(print_sum_docstring)
