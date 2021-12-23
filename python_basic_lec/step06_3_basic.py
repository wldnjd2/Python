# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def my_fun():
    return 42

# 함수를 arguments로 사용하기도 함
def docstring_exist(func):
    """입력된 함수 내 docstring이 있는지 확인하는 함수

    Args:
        func (callable): A function

    Returns:
        bool
    """

    return func.__doc__ is not None # True or False 값 반환

def no_docstring():
    return 10

def yes_docstring():
    """value 값을 반환합니다.
    """
    return 10

if __name__ == "__main__":
    x = my_fun
    print(my_fun())
    print("-----")
    print(docstring_exist(no_docstring))
    print(docstring_exist(yes_docstring))