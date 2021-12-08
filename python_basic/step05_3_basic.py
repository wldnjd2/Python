# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# context manager 작성
import contextlib

@contextlib.contextmanager
def my_context():
    print("안녕하세요 처음 인사드립니다.")
    yield 10
    print("이제 그만 끝내요.")

def main():
    with my_context() as temp:
        print("temp 인사말 {}".format(temp))

if __name__ == "__main__":
    main()

