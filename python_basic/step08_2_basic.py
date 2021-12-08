# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

x = 100
def a(value):
    def b():
        print(value)
    return b

if __name__ == "__main__":
    my_func = a(x)
    print(my_func())

    del(x) # x = 100을 삭제한 것
    print(my_func())

    print(len(my_func.__closure__))
    print(my_func.__closure__[0].cell_contents)


"""
개념정리: Nested Functions
- 하나의 function 안에 또다른 function이 있는 것. 

# outer function
def parent():
    # nested function
    def child():
        pass 
    return child
    
개념정리: Definitions - Nonlocal Variables
- Nonlocal Variables: Variables defined in the parent function that are used by the child function

def parent(arg_1, arg_2)
    # child() 함수 관점에서는 value & my_dict은 nonlocal variables
    value = 22
    my_dict = {"A": 100}
    
    def child()
        print(2 * value)
        print(my_dict["A"])
        print(arg_1 + arg_2)
    return child
"""