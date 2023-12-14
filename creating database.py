import mysql.connector as m
conn= m.connect (host="localhost", user="root", passwd="shinguren")
cursor=conn.cursor()
cursor.execute("CREATE DATABASE school")
print("DATABASE CREATED")