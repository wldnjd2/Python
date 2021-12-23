# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def check_closure(arg1, arg2):
    def inside_func():
        print("arg1 was {}".format(arg1))
        print("arg1 was {}".format(arg2))
    return inside_func

if __name__ == "__main__":
    my_func = check_closure(10, 100)

    # Closure 에 결측치 있는지 확인
    print(my_func.__closure__ is not None)

    # 2개의 변수가 존재하는지 확인
    print(len(my_func.__closure__) == 2)

    # closure value 확인
    closure_values = [
        my_func.__closure__[i].cell_contents for i in range(2)
    ]

    print(closure_values == [2, 10])