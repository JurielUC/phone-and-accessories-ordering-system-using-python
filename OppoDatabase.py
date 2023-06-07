import sqlite3

def OppoData():
    con=sqlite3.connect("Oppo.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Oppo(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Oppo.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Oppo")
    rows = cur.fetchall()
    con.close()
    return rows

OppoData()