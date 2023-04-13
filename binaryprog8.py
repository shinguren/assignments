import pickle
x = int(input("enter admission number to search:"))
flag = 0
with open ("member.dat","rb") as f:
    R = pickle.load(f)
    for rec in R:
        if rec[0] == x:
            flag = 1
            print(rec)

if flag == 0:
    print("record not found")
    