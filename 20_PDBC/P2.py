# import mysql.connector
# #connect(*kwargs)

# conn=mysql.connector.connect(host='localhost',database='cricket', user='root',password='Sai@1998')
# cursor=conn.cursor()

# query='INSERT INTO employee(empno,ename,eage,ecity)values(%s,%s,%s,%s)'
# values=(101,'sai kiran',28,'hyd')

# cursor.execute(query,values)

# conn.commit()

# print("record inserted")

# cursor.close()

# conn.close()


#Task2
# import mysql.connector
# #connect(*kwargs)

# conn=mysql.connector.connect(host='localhost',database='cricket', user='root',password='Sai@1998')
# cursor=conn.cursor()

# query= 'UPDATE employee set ename=%s where empno=%s'
# values=("venkat sai",101)

# cursor.execute(query,values)

# conn.commit()

# print("record inserted")

# cursor.close()

# conn.close()



#task 3
import mysql.connector
#connect(*kwargs)

conn=mysql.connector.connect(host='localhost',database='cricket', user='root',password='Sai@1998')
cursor=conn.cursor()

query= 'DELETE from employee where ecity=%s'

values=('hyd',)

cursor.execute(query,values)

conn.commit()

print("record deleted")

cursor.close()

conn.close()