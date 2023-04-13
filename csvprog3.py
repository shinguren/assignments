# sending multiple records all at once

import csv
f3=open('data.csv','w')
cv=csv.writer(f3, delimiter=',')
rec=[]
while True:
    ino = int(input("enter item number:"))
    iname = input("enter item name:")
    qty = int(input("enter quantity:"))
    rec.append([ino,iname,qty])

    ch= input("enter more records? (y?n):")
    if ch in ['n', 'N']:
        break
    cv.wrterow(rec)
print("file created")