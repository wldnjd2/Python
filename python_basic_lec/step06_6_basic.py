# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-
# Defining a function inside another function

def a(x, y):
    def within_range(z):
        return z > 5 and z < 8

    if within_range(x) and within_range(y):
        print(x * y)

if __name__ == "__main__":
    print(a(6,6))
