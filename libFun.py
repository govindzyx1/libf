import sqlite3
con=sqlite3.connect("e:\\pyprg\\mydb7.db")
cur=con.cursor()
con.execute('''create table if not exists libr(name text not null,auth text not null,category text not null)''')
con.execute('''create table if not exists member(name text not null,custId integer primary key,phno integer)''')

def showOption():
    print("1 Liberary Membership:")
    print("2 Add Book:")
    print("3 Book Taken:")
    print("4 Book Submit: ")
    print("5 Show Liberary Detail:")
    print("6 Show Member Detail:")
    x = int(input("your option:"))
    return x

def libMember():
    name = input("Enter your name :")
    custId = int(input("Enter your id :"))
    phno = int(input("Enter your Mobile No. :"))
    con.execute('''insert into member(name,custId,phno) values('%s',%d,%d)'''%(name,custId,phno))
    print("\n\n\n Membership created")
    con.commit()

def showLib():
    cur=con.cursor()
    rec=cur.execute('''select * from libr''');
    for row in rec:
        print(row[0],row[1],row[2])

def showMem():
    cur=con.cursor()
    rec=cur.execute('''select * from member''');
    for row in rec:
        print(row[0],row[1],row[2])

def addBook():
    cur=con.cursor()
    name = input("Enter book name :")
    auth = input("Enter Author Book :")
    category = input("Enter category of Book :")
    con.execute('''insert into libr(name,auth,category) values('%s','%s','%s')'''%(name,auth,category))
    print("\n\n\n Book added!!")
    con.commit()

def bookTaken():
    cur=con.cursor()
    name = input("Enter book name: ")
    auth = input("Enter Author Book :")
    category = input("Enter category of Book :")
    cur.execute("""select name from libr WHERE category = '%s'""" %category)
    a=cur.fetchone()
    n=a[0]-category
    cur.execute("""update libr SET name = '%s', auth= '%s', category='%s' WHERE name = '%s'"""%(name,auth,category))
    print(n)
    con.commit()

def bookSubmit():
    cur=con.cursor()
    name = input("Enter book name: ")
    auth = input("Enter Author Book :")
    category = input("Enter category of Book :")
    cur.execute("""select name from libr WHERE category = '%s'""" %category)
    a=cur.fetchone()
    n=a[0]+category
    cur.execute("""update libr SET name = '%s', auth= '%s', category='%s' WHERE name = '%s'"""%(name,auth,category))
    print(n)
    con.commit()
