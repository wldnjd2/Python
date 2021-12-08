# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# NonLocal Keyword
x = 1000
def a():
    x = 10

    def b():
        nonlocal x # 주석처리 할 것
        x = 100
        print(x)

    b()
    print(x)

if __name__ == "__main__":
    print(a())
    print(x)