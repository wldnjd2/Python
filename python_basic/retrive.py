# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import step01_3_basic
import inspect

docstring = inspect.getdoc(step01_3_basic.cnt_letter)

if __name__ == "__main__":
    border = '#' * 28
    print('{}\n{}\n{}'.format(border, docstring, border))
