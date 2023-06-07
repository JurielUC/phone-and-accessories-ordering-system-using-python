import sqlite3

def OnePlusData():
    con=sqlite3.connect("OnePlus.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS OnePlus(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("OnePlus.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM OnePlus")
    rows = cur.fetchall()
    con.close()
    return rows

OnePlusData()