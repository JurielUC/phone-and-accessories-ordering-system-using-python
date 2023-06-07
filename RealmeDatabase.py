import sqlite3

def RealmeData():
    con=sqlite3.connect("Realme.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Realme(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Realme.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Realme")
    rows = cur.fetchall()
    con.close()
    return rows

RealmeData()