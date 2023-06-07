import sqlite3

def HonorData():
    con=sqlite3.connect("Honor.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Honor(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Honor.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Honor")
    rows = cur.fetchall()
    con.close()
    return rows

HonorData()