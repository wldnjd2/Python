# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Builtin > Global > NonLocal > Local

x = 100

def a():
    x = 42
    print(x)

if __name__ == "__main__":
    print(a()) # 차이점 확인
    print(x) # 차이점 확인
