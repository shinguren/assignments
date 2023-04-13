# to send n numbers one by one in the binary file and then reading them

import pickle
n = int(input("enter number of records:"))

#storing
of=open("orig.txt","wb")
for i in range(n):
    num = int(input("enter any number:"))
    pickle.dump(num, of)
of.close()

#displaying
iff=open("orig.txt","rb")
print("**data read from the file**")
for i in range(n):
    num = pickle.load(iff)
    print(num, end="")
iff.close()
