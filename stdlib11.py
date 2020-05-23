import mysql.connector

def create_connection(host,user,passwd,db):
    conn = mysql.connector.connect()
    try:
        conn = mysql.connector.connect(host=host,user=user,passwd=passwd,database=db)
        print("Connection created successfully {}".format(conn.connection_id))
        return conn
    except mysql.connector.Error as error:
        print("Failed to create table {}".format(error))

        '''
    finally:
        if (conn.is_connected()):
            conn.close()
            print("Connection closed successfully.")
        else:
            print("Unexpected error in connection.")
            '''


#create_connection('localhost','root','datadata','mysql')

def insert_employee(eid,ename,salary,edid):
    record = (eid,ename,salary,edid)
    conn = create_connection('localhost', 'root', 'datadata', 'mysql')
    if conn.is_connected:
        try:
            cursor = conn.cursor()
            create_query = "insert into Emp(eid,ename,salary,edid) values(%s,%s,%s,%s)"
            cursor.execute(create_query,record)
            conn.commit()
            print(cursor.rowcount, " records inserted successfully.")
        except mysql.connector.Error as error:
            print("Failed to insert record {}".format(error))
        finally:
            if (conn.is_connected()):
                conn.close()
                print("Connection closed successfully.")
            else:
                print("Unexpected error in connection.")

'''
eid = int(input("Please enter employee id "))
ename = input("Please enter employee name ")
salary = input("Please enter employee salary ")
edid = input("Please enter employee department ")
insert_employee(eid,ename,salary,edid)


'''
insert_employee(101,'suraj',4000,12)
insert_employee(104,'raj',4000,12)
insert_employee(105,'tom',4000,13)


