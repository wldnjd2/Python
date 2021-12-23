# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-
# Closures

def a():
    a = 5
    def b():
        print(a)
    return b

if __name__ == "__main__":
    func = a()
    func()
    print(type(func.__closure__))
    print(len(func.__closure__))
    print(func.__closure__[0].cell_contents)

