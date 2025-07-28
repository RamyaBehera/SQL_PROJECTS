import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ramya@sql',database='ramya')
my_cursor=conn.cursor()
my_cursor.execute("SELECT cust_id FROM customer")
result = my_cursor.fetchall()
id_list = []
for row in result:
    id_list.append(row[0])
print("existing Customer IDs:", id_list)
if 5 in id_list:
    print("customer with id 5 already exists")
else:
    print("customer id 5 is new")
my_cursor.close()
conn.close()
