# import mysql.connector
# #connect(*kwargs)

# conn=mysql.connector.connect(host='localhost',database='cricket', user='root',password='Sai@1998')
# cursor=conn.cursor()

# query='(empno,ename,eage,ecity)values(%s,%s,%s,%s)'
# values=[
#     (101,'sai kiran',28,'hyd'),
#     (102,'sai kumar',30,'ogl'),
#     (103,'sai ram',26,'nlr'),
# ]

# cursor.executemany(query,values)

# conn.commit()

# print("record inserted")

# cursor.close()

# conn.close()


#fetchall method

import mysql.connector
#connect(*kwargs)

conn=mysql.connector.connect(host='localhost',database='cricket', user='root',password='Sai@1998')
cursor=conn.cursor()

query='SELECT * FROM employee'

cursor.execute(query)
print(cursor.fetchall())

conn.commit()

cursor.close()

conn.close()