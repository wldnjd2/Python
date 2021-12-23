# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 05_1 참조 context manager 사용하여 read_only_file 열기
import contextlib
import step05_6_basic
import time

@contextlib.contextmanager
def openReadOnly(fileName):
    """
    Args:
        fileName (str): 파일 경로를 문자열로 지정한다.

    Yields:
        file 객체
    """
    read_file = open(fileName, mode = "r")

    yield read_file

    read_file.close()

def main(fileName):
    with openReadOnly(fileName) as file:
        text = file.read()

    n = 0
    for word in text.split():
        if word in ['오미크론', '코로나']:
            n += 1

    print('오미크론 및 코로나 단어가 나오는 개수는 {} 이다.'.format(n))

if __name__ == "__main__":
    fileName = "data/news_article.txt"
    with step05_6_basic.timer():
        main(fileName)
        time.sleep(0.25)

