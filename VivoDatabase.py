import sqlite3

def VivoData():
    con=sqlite3.connect("Vivo.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Vivo(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Vivo.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Vivo")
    rows = cur.fetchall()
    con.close()
    return rows

VivoData()