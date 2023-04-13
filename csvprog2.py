# to send multiple records in a csv file

import csv
f2=open('data2.csv','w')
cv=csv.writer(f2, delimiter=',')
while True:
    ino = int(input("enter item number:"))
    iname = input("enter item name:")
    qty = int(input("enter quantity"))
    rec=[ino,iname,qty]
    cv.writerow(rec)
    ch=input("enter more records?: (y/n)")
    if ch in ['n','N']:
        break
print("file created successfully")