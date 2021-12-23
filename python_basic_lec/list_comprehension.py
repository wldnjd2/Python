# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-
# https://www.programiz.com/python-programming/list-comprehension

def lc_main():
    my_list = [[10], [20, 30]]
    flattend_list = [value for value_list in my_list for value in value_list]
    print(flattend_list)

def for_main():
    my_list = [[10], [20, 30]]
    flattend_list = []
    for value_list in my_list:
        for value in value_list:
            flattend_list.append(value)
    print(flattend_list)

if __name__ == "__main__":
    lc_main()
    for_main()