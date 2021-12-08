# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Counter
# 특정 함수가 몇번 불러왔는지 확인하는 함수
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@counter
def a():
    print("임의의 함수 호출")

if __name__ == "__main__":

    a()
    a()
    a()
    print("a() 함수는 현재 {} 번 호출됨".format(a.count))