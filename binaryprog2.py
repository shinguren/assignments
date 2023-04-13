import pickle
f1 = open('emp.dat','rb')
e = pickle.load(f1)
print("* data in file *")
for x in e:
    print(x)
f1.close()