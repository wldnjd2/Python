# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def whatsInside():
    def please_print_me(s):
        print(s)
        # return 1
    return please_print_me

if __name__ == "__main__":
    new_func = whatsInside()
    print(new_func("Hope this prints print()"))

