import mysql.connector

conn = mysql.connector.connect()
try:
    conn = mysql.connector.connect(host='localhost',user='root',passwd='datadata',database='mysql')
    cursor = conn.cursor()
    select_query = "select * from Emp where edid = %s"
    records_to_fetch = [12]
    cursor.execute(select_query,records_to_fetch)
    record = cursor.fetchall()
    print(record)
    try:
        #delete_query = "delete from Emp where edid = 12"
        #cursor.execute(delete_query)
        delete_query = "delete from Emp where edid = %s"
        records_to_delete = [(12,),(13,)]
        cursor.execute(delete_query,records_to_delete)
        print(cursor.rowcount," records deleted successfully.")
        conn.commit()
    except mysql.connector.Error as error:
        print("Failed to delete record {}".format(error))

    cursor.execute(select_query,records_to_fetch)
    records = cursor.fetchall()
    if len(records)== 0:
        print(len(records),"records found based on query.")
    else:
        print(len(records), "records found based on query.")
except mysql.connector.Error as error:
    print("Failed to delete record {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Connection closed successfully.")
    else:
        print("Unexpected error in connection.")
