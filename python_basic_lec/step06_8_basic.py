# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# func 이름이 들어간 덧셈 뺄셈믈 추가해본다.
# func 안에 func을 추가한다.
def math_functions(func_name):
    if func_name == "add":
        def add(a, b):
            return a + b
        return add
    elif func_name == "subtract":
        def subtract(a, b):
            return a - b
        return subtract
    elif func_name == "multiple":
        def multiple(a, b):
            return a * b
        return multiple
    elif func_name == "divide":
        def divide(a, b):
            return a // b
        return divide
    else:
        print("그 외에는 잘 모르겠습니다.")

if __name__ == "__main__":
    x = 100
    y = 2

    add = math_functions("add")
    print("100 + 2 = {}".format(add(x, y)))

    subtract = math_functions("subtract")
    print("100 - 2 = {}".format(subtract(x, y)))

    subtract = math_functions("multiple")
    print("100 * 2 = {}".format(subtract(x, y)))

    divide = math_functions("divide")
    print("100 / 2 = {}".format(divide(x, y))) # 정수 출력
