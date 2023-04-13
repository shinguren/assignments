def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print('sum',add(10,20,30,40))