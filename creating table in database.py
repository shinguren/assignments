import mysql.connector as m
con=m.connect(host="local host", user="root", passwd="tiger", database="school" )
cur=con.cursor()
cur.execute("INSERT INTO student VALUES(111, 'Amar', 12, 'D', 95.8)")
cur.execute("INSERT INTO student VALUES(112, 'Chinglen', 12, 'E', 92.9)")
cur.execute("INSERT INTO student VALUES(121, 'Mitali', 12, 'B', 100)")
con.commit()
print("record inserted")
