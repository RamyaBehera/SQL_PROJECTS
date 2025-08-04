import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
def view_products():
    my_cursor.execute("SELECT * FROM product")
    for row in my_cursor.fetchall():
        print(row)
view_products()
my_cursor.close()
conn.close()
