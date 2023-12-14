import csv
f=open("data.csv","w")
obj=csv.writer(f, delimiter=',')
n=int(input("enter number of entries:"))
for i in range(n):
    itno=int(input("enter item number:"))
    itna=input("enter item name:")
    qty=int(input("number of quantity:"))
    record=[itno, itna, qty]
    obj.writerow(record)
f.close()    




     