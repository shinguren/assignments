def print_value(a):
    print("inside function N=",a)
    a=a+2
    print("after change a=",a)

N=3
print("calling function with",N)
print_value(N)
print("after returning from function N=",N)