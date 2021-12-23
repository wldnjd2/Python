# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Closure: Nonlocal Variables은 반환되는 함수에 붙여서 나오게 됨
def parent(arg_1, arg_2):
    nonlocal_value = 100
    nonlocal_my_dict = {"A": 0}

    def child():
        print(2 * nonlocal_value)
        print(nonlocal_my_dict["A"])
        print(arg_1 + arg_2)

    return child

if __name__ == "__main__":
    new_function = parent(100, 200)
    print([cell.cell_contents for cell in new_function.__closure__]) # 리스트로 반환
    for cell in new_function.__closure__:                            # 단일 객체로 반환
        print(cell.cell_contents)
