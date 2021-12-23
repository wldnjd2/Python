# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import inspect

def print_args(func):
    sig = inspect.signature(func) # 객체는 콜러블 객체의 호출 서명과 반환 값 어노테이션을 나타냅니다.
    print(sig)

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs).arguments # 반복문 돌리기 위해 딕셔너리 형태로 묶어줌
        str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
        print('{} was called with {}'.format(func.__name__, str_args))
        return func(*args, **kwargs)
    return wrapper

@print_args
def my_function(a, b, c):
  print(a + b + c)


if __name__ == "__main__":
    # my_function = print_args(my_function) # 데코레이터 안할 시
    print(my_function(1, 2, 3))