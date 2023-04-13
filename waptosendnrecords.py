f1=open("records1","w")
n=int(input("enter number of entries:"))
for i in range(n):
    roll=input("enter roll number:")
    name=input("enter name:")
    f1.write(roll)
    f1.write('\t')
    f1.write(name)
    f1.write('\n')
f1.close