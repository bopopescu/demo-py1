import mysql.connector

conn = mysql.connector.connect()
try:
    conn = mysql.connector.connect(host='localhost',user='root',passwd='datadata',database='mysql')
    cursor = conn.cursor()
    create_query = "insert into Emp(eid,ename,salary,edid) values(101,'Rajesh',5000,11)"
    cursor.execute(create_query)
    conn.commit()
    print(cursor.rowcount ," records inserted successfully.")
except mysql.connector.Error as error:
    print("Failed to insert record {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Connection closed successfully.")
    else:
        print("Unexpected error in connection.")
