f1=open("data.txt","r")
data=f1.readlines()
count=0
for i in data:
    if i[0]=='A':
        count=count+1
print("number of times 'A' appears in the starting of the line:", count)
print("lines starting with 'A':",i)