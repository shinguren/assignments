def add(*args, avg):
    sum=0
    for I in args:
        sum+= I
    avg=sum/4
    return sum, avg

s, avg=add(10,20,30,40,avg=0)
print("sum=",s,"avg=",avg)