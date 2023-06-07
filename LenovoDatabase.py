import sqlite3

def LenovoData():
    con=sqlite3.connect("Lenovo.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Lenovo(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Lenovo.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Lenovo")
    rows = cur.fetchall()
    con.close()
    return rows

LenovoData()