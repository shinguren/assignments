import pickle
f=open("member.dat",'wb')
while True:
    admno=int(input("enter admission number:"))
    name= input("enter name:")
    per = float(input("enter percentage:"))
    pickle.dump([admno,name,per], f)
    c=input("do you want to add more records? (Y?N)")
    if c in ['n', "N"]:
        break

print("file created")


import pickle
with open("member.dat", "rb") as f:
    print("**contents of the file**")
    while True:
        try:
            R= pickle.load(f)
            print(R)
        except:
            break

        