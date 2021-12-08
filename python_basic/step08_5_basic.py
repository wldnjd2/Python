# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def print_msg():
    print('print_msg 함수입니다. ')

def new_func(func):
    def call_func():
        func()
    return call_func


new_func = new_func(print_msg)

# 삭제
del(print_msg)

if __name__ == "__main__":
    print(new_func())