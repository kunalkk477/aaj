import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,uid INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,uid):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,uid))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")

    conn.close()
    return rows

def search(title="",author="",year="",uid=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or uid=?",(title,author,year,uid))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,uid):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,uid=? WHERE id=?",(title,author,year,uid,id))
    conn.commit()
    conn.close()




connect()
# print(view())
# def functiona():
#     a=input("enter title: ")
#     b=input("enter author: ")
#     c=input("enter year: ")
#     d=input("enter uid: ")
#     insert(a,b,c,d)
# def searcha():
#
# functiona()
# cont=1
# print(view())
# while(cont==1):
#     print("pick an option: ")
#
#     option=int(input("1. insert 2. update 3.delete 4. show  5. exit: "))
#
#     print("")
#
#     if(option==1):
#
#         a=input("enter the  book name:")
#         b=input("enter the author name: ")
#         c=int(input("year release: "))
#         d=int(input("unique id: "))
#         insert(a,b,c,d)
#
#     elif(option==2):
#         a=int(input("enter the id: "))
#         e=input("enter the new book name:")
#         b=input("enter the author name: ")
#         c=int(input("year release: "))
#         d=int(input("unique id: "))
#         update(a,e,b,c,d)
#
#     elif(option==3):
#         g=int(input("enter the book id: "))
#         delete(g)
#     elif(option==4):
#         print(view())
#     elif(option==5):
#         cont=2
#     else:
#         print("wrong choice")
