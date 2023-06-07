import sqlite3

def HuaweiData():
    con=sqlite3.connect("Huawei.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Huawei(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Huawei.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Huawei")
    rows = cur.fetchall()
    con.close()
    return rows

HuaweiData()