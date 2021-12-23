# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# global x, nonlocal x, x등 자유롭게 활용하여 다음과 같이 출력하세요.
# 단 반드시, global x 또는 nonlocal x 등은 입력되어야 함
# 변수는 x만 사용합니다.
# 100, 70, 30, 70 순서대로 출력 됨

x = 100

# 문제 낼 것

def a():
    x = 70

def b():
    global x
    x = 70

def c():
    x = 30
    print(x)

if __name__ == "__main__":
    # result = []
    for function in [a, b, c]:
        function()
        print(x)
