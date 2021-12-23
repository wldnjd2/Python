# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 언제 쓸까요?
# 가장 대표적으로 많이 쓰는 분야는 DB 연동
import contextlib
import sqlite3

@contextlib.contextmanager
def db_connect(url):

    db = sqlite3.connect(url)
    yield db
    db.close()

def main(url):
    with db_connect(url) as con:
        cur = con.cursor()
        for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)

if __name__ == "__main__":
    url = "example.db"
    main(url)
