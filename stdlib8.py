import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',passwd='datadata',database='mysql')

print(conn)

cursor = conn.cursor()
cursor.execute("select * from Dept")
records = cursor.fetchall()

for row in records:
    print("for dept id ",row[0]," is at Location = " ,row[2])

