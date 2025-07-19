import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql')
my_cursor=conn.cursor()
my_cursor.execute("create database ramya")
my_cursor.execute("use ramya")
print("database is created and used")
my_cursor.close()
conn.close()
