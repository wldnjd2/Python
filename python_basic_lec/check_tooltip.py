# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import inspect
import step01_3_basic

def check_tooltip(funct):
    """기본함수의 문서를 보여주는 함수를 만든다.

    Args:
        function (callable): 문서를 보여주고자 하는 임의의 함수

    Returns:
        str
    """
    docstring = inspect.getdoc(funct)
    borderline = '#' * 10
    return '{}\n{}\n{}'.format(borderline, docstring, borderline)

if __name__ == "__main__":
    print(check_tooltip(step01_3_basic.cnt_letter))
    print(check_tooltip(list))
    print(check_tooltip(range))