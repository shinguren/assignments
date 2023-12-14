cnt=0
f=open("data.dat","r")
data=f.read()
x=data.split()
for i in x:
    if i=="the":
        cnt=cnt+1
f.close()
print("number of times 'the' appears", cnt)
