import sqlite3

def SoldFone():
    con=sqlite3.connect("Sold.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Sold(id INTEGER PRIMARY KEY, UNIT text, PRICE integer)") #database table
    con.commit()
    con.close()
    
def add(UNIT, PRICE):
    con=sqlite3.connect("Sold.db")
    cur=con.cursor()
    cur.execute("INSERT INTO Sold VALUES(NULL, ?,?)",(UNIT, PRICE))
    con.commit()
    con.close()
    
def view():
    con=sqlite3.connect("Sold.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Sold")
    rows = cur.fetchall()
    con.close()
    return rows
    
def delete():
    con=sqlite3.connect("Sold.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Sold;",)
    con.commit()
    con.close
     
SoldFone()