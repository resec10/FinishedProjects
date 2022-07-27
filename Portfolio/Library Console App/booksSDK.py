import sqlite3

def cursor():
    with sqlite3.connect("myDatabase.db").cursor().connection:
        sqlite3.connect("myDatabase.db").cursor().execute("CREATE TABLE IF NOT EXISTS Books (title TEXT, pages INTEGER)")
    return sqlite3.connect("myDatabase.db").cursor()

def add(title, pages):
    c=cursor()
    with c.connection:
        c.execute("INSERT INTO Books VALUES (?, ?)", [title, pages])
    c.connection.close()

def read():
    c=cursor()
    c.execute("SELECT * FROM Books")
    d=c.fetchall()
    c.connection.close()
    return d

def update(newTitle, newPages, rowid):
    c=cursor()
    with c.connection:
        c.execute("UPDATE Books SET title=?, pages=? WHERE rowid=?", [newTitle, newPages, rowid])
    c.connection.close()
    
def readingROWID():
    c=cursor()
    c.execute('SELECT *, rowid FROM Books')
    d=c.fetchall()
    c.connection.close()
    d=[f"{i[2]}) {i[0]} - {i[1]} pages long" for i in d]
    return d

def read2(rowid):
    c=cursor()
    c.execute("SELECT * FROM Books WHERE rowid=?", [rowid])
    d=c.fetchone()
    c.connection.close()
    d=f"{d[0]} ({d[1]} pages long)"
    return d

def readNEW():
    c=cursor()
    c.execute('SELECT * FROM Books')
    data=c.fetchall()
    c.connection.close()
    data=[list(i) for i in data]
    strs=[]
    for item in data:
        item[1]=str(item[1])
        strs.append(f"{item[0]} ({item[1]} pages long)")
    strs.insert(-1, 'and')
    nw=[strs.pop(-2), strs.pop(-1)]
    nw=" ".join(nw)
    strs=", ".join(strs)
    return (f" {strs} {nw}")

def delete(rowid):
    c=cursor()
    with c.connection:
        c.execute("DELETE FROM Books WHERE rowid=?", [rowid])
    c.connection.close()

