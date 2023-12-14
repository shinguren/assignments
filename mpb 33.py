import csv
def add_rec():
    f1= open("emp.csv","w")
    cvw=csv.writer(f1)
    while True:
        empno=int(input("enter employee number:"))
        empname=input("enter employee name:")
        des=input("enter designation:")
        ph= int(input("enter phone number:"))
        sal= int(input("enter salary:"))
        lst=[empno, empname, des, ph, sal]
        cvw.writerow(lst)
        ch=input("enter more?")
        if ch == 'N' or ch == 'n':
            break
    print("data successfully added")
    f1.close()

add_rec()