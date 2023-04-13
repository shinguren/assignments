def prime(L):
    for i in L:
        x=0
        for j in range(1,i):
            if i%j==0:
                x+=1
        if x==1:
            print(i)


L=[3,4,5,6,7,8,9]
prime(L)