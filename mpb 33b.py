import csv
def countrec():
    f1=("emp.csv","r")
    cvr=csv.reader(f1)
    cnt=0
    for i in cvr:
        if int(i[4])>50000:
            cnt+=1
        else:
            print("no records founds")
