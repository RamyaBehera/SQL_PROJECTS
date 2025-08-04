import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
def add_product():
    print("Enter New Product Details")
    product_no = int(input("Product No"))
    product_id = input("Product id")
    product_price = float(input("Product Price"))
    product_stock = int(input("Product Stock"))
    sql = "INSERT INTO product(product_no, product_id, product_price, product_stock) VALUES (%s, %s, %s, %s)"
    val = (product_no, product_id, product_price, product_stock)
    try:
        my_cursor.execute(sql, val)
        conn.commit()
        print("new product added successfully")
    except mysql.connector.Error as err:
        print("Error:", err)
add_product()
my_cursor.close()
conn.close()
