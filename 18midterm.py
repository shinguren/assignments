import csv
f1=open('teacher.csv','w')
cv=csv.writer(f1,delimiter =',')
while True:
    t_id=input("enter id :")
    t_name=input("enter name :")
    subj=input("enter subject :")
    ch=input("enter choice (y/n) :")
    rec=[t_id,t_name,subj]
    cv.writerow(rec)
    if ch in['N','n']:
        break
f1.close()

f2=open('teacher.csv','r')
cv=csv.reader(f2,delimiter=',')
for i in cv:
    print(i)