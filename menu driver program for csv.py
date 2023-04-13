import csv
def add():
    f=open("data.csv",'w', newline='')
    cv = csv.writer(f, delimiter=',')
    while True:
        print("\n")
        admno = int(input("enter admno:"))
        name = input("enter name:")
        clas = int(input("enter class:"))
        per = int(input("enter percentaage:"))

        record = [admno, name, clas, per]
        cv.writerow(record)

        ch = input("add more records? (y/n)")
        if ch=="n" or ch =="N":
            break
        f.close()

def display():
    f=open('data.csv','r')
    cv=csv.reader(f, delimiter=',')
    print("\n\n ** student records **")
    print("admno \t name \t class \t percentage")
    for c in cv:
        for data in c:
            print(data, end='\t')
        print()
    f.close()

def search():
    f = open('data.csv','r')
    cv=csv.reader(f, delimiter=',')
    print("\n\n ** student records with %> 75 **")
    print("admno \t name \t class \t percentage ")
    for c in cv:
        if int(c[3])> 75:
            for data in c:
                print(data, end='\t')
        print()

def count():
    f = open('data.csv','r')
    cv =csv.reader(f, delimiter =',')
    cnt=0
    for c in cv:
        for char in c[1]:
            if char == 'a':
                cnt+=1
    print("\n\n ** count of a in name field **")
    print("number of times 'a' appears:", cnt)

def menu():
    while True:
        print("\n\n **menu**")
        print("1: Add")
        print("2: Display all")
        print("3: Search")
        print("4: Count")
        print("0: Exit")

        ch = int(input("enter choice:"))
        if ch == 1:
            add()
        elif ch==2:
            display()
        elif ch==2:
            search()
        elif ch==4:
            count()
        elif ch==0:
            break
    
menu()