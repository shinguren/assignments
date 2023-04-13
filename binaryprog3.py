# sending different types of data in a binary file

import pickle
f1 = open("records", "wb")
myint = 42
mystring = "hello, world!"
mylist = ["dog", "cat"]
mydict = {"name": "Bob", "job": "astronaut"}

pickle.dump(myint, f1)
pickle.dump(mystring, f1)
pickle.dump(mylist,f1)
pickle.dump(mydict, f1)

print("** file created **")
f1.close()

f1=open("records","rb")
myint = pickle.load(f1)
mystring = pickle.load(f1)
mylist = pickle.load(f1)
mydict = pickle.load(f1)

print("myint =", myint)
print("mystring= ", mystring)
print("mylist=", mylist)
print("mydict=",mydict)
f1.close()