# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 시간 측정 함수 만들기
# time Decorator 만들기

import time

def timer(func):
    """함수 실행 시 얼마나 오래 걸리는지 확인"""

    def wrapper(*args, **kwargs):
        # 현재시간
        time_start = time.time()
        # decorated 함수 불러오기
        result = func(*args, **kwargs)
        time_total = time.time() - time_start
        print("{} took {}s".format(func.__name__, time_total))
        return result
    return wrapper

@timer
def check_time(num):
    time.sleep(num)

if __name__ == "__main__":
    check_time(3)

