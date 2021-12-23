# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 데코레이터 함수 만들기
def return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(func.__name__, type(result)))

        return result

    return wrapper

@return_type
def a(value):
    return value

if __name__ == "__main__":
    print(a(123))
    print(a([1, 2, 3]))
    print(a({"a": 42}))