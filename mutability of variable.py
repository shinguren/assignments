def print_value(L):
    print("inside function list is",L)
    L[0]=L[0]+2
    L[1]=L[1]+1
    print("after change list is",L)

N=[3,5]
print("before calling function list is",N)
print_value(N)
print("after returning from function list is", N)