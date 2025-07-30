import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
def get_booked_products(cust_id):
    my_cursor.execute("SELECT products FROM customer WHERE cust_id = %s", (cust_id,))
    result = my_cursor.fetchone()
    if result is None:
        print("customer id not found.")
        return [] 
    products = result[0]
    if not products or products.strip() == "":
        return []
    return products.split("_")
cust_id = int(input("enter Customer id for book product"))
booked_products = get_booked_products(cust_id)
if booked_products:
    print("Booked Product IDs:")
    for pid in booked_products:
        print(pid)
else:
    print("customer does not exist")
my_cursor.close()
conn.close()
