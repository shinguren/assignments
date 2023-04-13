# to search for a specific record in a csv file 

import csv 
try:
    flag=0
    with open('data1.csv','r')as cf:
        cv = csv.reader(cf, delimiter=',')
        x = int(input("enter item number to search:"))
        for c in cv:
            if int(c[0])== x:
                flag=1
                print(c)

except FileNotFoundError:
    print("file not found")

if flag==0:
    print("record not found")
    