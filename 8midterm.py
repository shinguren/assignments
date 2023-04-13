def funjoin(S):
    T =""
    for I in S:
        if I.isdigit():
            T=T+1
    return T

x= "PYTHON 3.9"
y=funjoin(x)
print(x,y, sep="*")    