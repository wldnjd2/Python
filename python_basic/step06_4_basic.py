# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Defining a function inside another function
def a():
    x = [3, 6, 9]

    def b(y):
        print(y)

    for value in x:
        b(x)

if __name__ == "__main__":
    print(a())