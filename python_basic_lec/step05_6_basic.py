# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 언제 쓸까요?
# 가장 대표적으로 많이 쓰는 분야는 DB 연동

import contextlib
import time

@contextlib.contextmanager
def timer():
    """시간측정하는 context manager 관리 함수

    Yields:
        None
    """

    start = time.time()
    yield
    end = time.time()
    print("(시간측정(Elapsed): {:.2f} 초)".format(end - start))

def main():
    with timer():
        print("얼마 걸릴까요?")
        time.sleep(0.25)

if __name__ == "__main__":
    main()