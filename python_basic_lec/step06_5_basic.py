# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Defining a function inside another function
def a(x, y):
    if x > 5 and x < 8 and y > 5 and y < 8:
        print(x * y)
    else:
        print("다른 값을 입력하세요!")
        # raise ValueError("X is {}, Y is {}".format(x, y))

if __name__ == "__main__":
    print(a(5, 4))