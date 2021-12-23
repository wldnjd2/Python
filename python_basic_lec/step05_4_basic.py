# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 언제 쓸까요?
# 가장 대표적으로 많이 쓰는 분야는 DB 연동
# 코드 참조
import sqlite3

def db_create():
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE stocks
                   (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    con.commit()
    con.close()

if __name__ == "__main__":
    db_create()