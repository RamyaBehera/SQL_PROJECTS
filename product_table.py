import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
my_cursor.execute("CREATE TABLE product(product_no INT,product_id INT PRIMARY KEY,product_price DECIMAL(10,2),product_stock INT)")
print("product table is created")
my_cursor.close()
conn.close()
