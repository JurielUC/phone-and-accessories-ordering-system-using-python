import sqlite3

def IPhoneData():
    con=sqlite3.connect("IPhone.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS IPhone(UNIT text, PRICE text)")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("IPhone.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM IPhone")
    rows = cur.fetchall()
    con.close()
    return rows

IPhoneData()