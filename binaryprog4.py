# storing in the form of a dictionary

import pickle
with open('data1.dat','wb')as f:
    roll = int(input("enter roll number:"))
    name = input("enter your name")
    d = {'roll':roll, 'name': name}
    pickle.dump(d, f)

with open ('data1.dat','rb')as f1:
    d1 = pickle.load(f1)
    print("**data read from the file**")
    print(d1)