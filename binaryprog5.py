# storing name and age of n people in a binary file in the form of dict

import pickle 
n = int(input("enter number of records:"))
d = {}
with open ('data1.dat','wb') as f:
    for i in range(n):
        name = input("enter name:")
        age = int(input("enter age:"))
        d[name] = age
    pickle.dump(d, f)

with open ('data1.dat','rb') as f1:
    d1 = pickle.load(f1)
    print("** data read from the file **")
    print(d1)

    