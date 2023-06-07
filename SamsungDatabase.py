import sqlite3

def SamsungData():
    con=sqlite3.connect("Samsung.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Samsung(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Samsung.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Samsung")
    rows = cur.fetchall()
    con.close()
    return rows

SamsungData()