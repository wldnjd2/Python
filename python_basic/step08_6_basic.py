# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 과제, 함수를 활용하여 제곱 곱셈 함수 만들기
def multiple_a(a):
    def multiple_b(b):
        return a * b
    return multiple_b

if __name__ == "__main__":
    m1 = multiple_a(1)
    m2 = multiple_a(2)
    m3 = multiple_a(3)

    print(m1(3))
    print(m1(5))
    print(m1(7))

