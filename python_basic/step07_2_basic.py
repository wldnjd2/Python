# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Builtin > Global > NonLocal > Local
# global 키워드에 배웁니다.
x = 100
def a():
    global x
    x = 10
    print(x)

if __name__ == "__main__":
    print(a())
    print(x)