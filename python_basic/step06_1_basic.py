# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 함수를 객체로 사용하는 방식

# function as variable
def my_fun():
    print("안녕")

if __name__ == "__main__":
    x = my_fun
    print(type(x))
    print(x())

    print_function = print
    print(print_function("파이썬 좋음"))