import sqlite3

def NokiaData():
    con=sqlite3.connect("Nokia.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Nokia(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Nokia.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Nokia")
    rows = cur.fetchall()
    con.close()
    return rows

NokiaData()