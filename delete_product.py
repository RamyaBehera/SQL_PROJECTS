import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
def delete_product():
    product_id = input("enter the Product id to delete: ")
    my_cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
    product = my_cursor.fetchone()

    if product is None:
        print("Product id does not exist.")
    else:
        my_cursor.execute("DELETE FROM product WHERE product_id = %s", (product_id,))
        conn.commit()
        print("Product deleted successfully.")
delete_product()
my_cursor.close()
conn.close()
