import mysql.connector
#connect(*kwargs)

conn=mysql.connector.connect(host='localhost',database='cricket', user='root',password='Sai@1998')
print(conn)

#cursor method is used forasking the database connection to provide you with a cursor object that you can then use to perform operations on the database

cursor=conn.cursor()
print(cursor)          #CMySQLCursor: (Nothing executed yet)

create="create table employee(empno int,ename varchar(40),eage int,ecity varchar(40))"

cursor.execute(create)

print("table created")

cursor.close()

conn.close()


