import mysql.connector

conn = mysql.connector.connect()
try:
    conn = mysql.connector.connect(host='localhost',user='root',passwd='datadata',database='mysql')
    cursor = conn.cursor()
    create_query = "create table Emp(eid int,ename varchar(10),salary int,edid int, primary key (eid), foreign key (edid) references Dept(did))"
    result = cursor.execute(create_query)
    print("Table created successfully")
except mysql.connector.Error as error:
    print("Failed to create table {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Connection closed successfully.")
    else:
        print("Unexpected error in connection.")
