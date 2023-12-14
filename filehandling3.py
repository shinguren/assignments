vowels=['aeiouAEIOU']
cnt=0
cntdigit=0
cntspecial=0
f=open("data.txt",'r')
data=f.readlines()
for i in data:
    if i.isalpha():
        if i in vowels:
              cnt +=1
    elif i.isdigit():
        cntdigit+=1
    else:
        cntspecial+= 1
f.close()
print("number of times vowels appeared:",cnt)
print("number of times digits appeared:", cntdigit)
print("number of times special char appeared ", cntspecial)