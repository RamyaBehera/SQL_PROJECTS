import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
my_cursor.execute("CREATE TABLE customer(cust_id INT PRIMARY KEY,first_name VARCHAR(50),last_name VARCHAR(50),phone VARCHAR(20),address VARCHAR(50),products VARCHAR(50))")
print("table is created")
my_cursor.close()
conn.close()
