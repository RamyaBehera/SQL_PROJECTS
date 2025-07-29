import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
def create_customer_account():
    cust_id = int(input("enter customer id "))
    my_cursor.execute("SELECT cust_id FROM customer WHERE cust_id = %s", (cust_id,))
    existing = my_cursor.fetchone()
    if existing:
        print("customer with this id already exist")
    else:
        first_name=input("enter first name")
        last_name=input("enter last name")
        phone=input("enter Phone number")
        address=input("enter address")
        products=input("enter products booked")
        sql = """
        INSERT INTO customer(cust_id, first_name, last_name, phone, address, products)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (cust_id, first_name, last_name, phone, address, products)
        my_cursor.execute(sql, values)
        conn.commit()
        print("New customer account created successfully")
create_customer_account()
my_cursor.close()
conn.close()
