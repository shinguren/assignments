import mysql.connector as m
con=m.connect(host="localhost", user="root", passwd="tiger", database="school")
cur=con.cursor()
cur.execute("SELECT * FROM student")
records=cur.fetchall()
for x in records:
    print(x)