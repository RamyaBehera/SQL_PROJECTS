import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
def employee_login():
    emp_id = int(input("Enter Employee ID to login: "))
    my_cursor.execute("SELECT * FROM employee WHERE emp_id = %s", (emp_id,))
    employee = my_cursor.fetchone()

    if not employee:
        print("Employee ID not found.")
        return

    print(f"\nWelcome {employee[1]} {employee[2]}")
    print("1. Update stock for delivered product")
    print("2. Add a new product")
    print("3. Delete a product")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        update_delivered_product()
    elif choice == "2":
        add_product()
    elif choice == "3":
        delete_product()
    else:
        print("Invalid choice.")
