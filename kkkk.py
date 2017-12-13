import psycopg2
print(" ")
def create():
    conn=psycopg2.connect("dbname='data1' user='postgres' password='123' host='localhost' port=''")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(item TEXT ,quantity INTEGER ,price REAL)")
    conn.commit()
    conn.close()

def insert(item ,quantity,price):
    conn=psycopg2.connect("dbname='data1' user='postgres' password='123' host='localhost' port=''")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (%s,%s,%s)",(item,quantity ,price))
    conn.commit()
    conn.close()

def show():
    conn=psycopg2.connect("dbname='data1' user='postgres' password='123' host='localhost' port=''")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='data1' user='postgres' password='123' host='localhost' port=''")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(price ,quantity,item):
    conn=psycopg2.connect("dbname='data1' user='postgres' password='123' host='localhost' port=''")
    cur=conn.cursor()
    cur.execute("UPDATE book SET price=%s,quantity=%s where item=%s",(price,quantity,item))
    conn.commit()
    conn.close()
create()
cont=1
while(cont==1):
    print("pick an option: ")

    option=int(input("1. insert 2. update 3.delete 4. show  5. exit: "))

    print("")

    if(option==1):
        a=input("enter the book name: ")
        b=int(input("enter the quantity: "))
        c=float(input("enter the price of this book: "))
        insert(a,b,c)

    elif(option==2):
        d=input("enter the book name: ")
        e=int(input("enter the new quantity: "))
        f=float(input("enter the new price of this book: "))
        update(f,e,d)

    elif(option==3):
        g=input("enter the book name: ")
        delete(g)
    elif(option==4):
        print(show())
    elif(option==5):
        cont=2
    else:
        print("wrong choice")
