def call(p=40, q=20):
    p=p+q
    q=p-q
    print(p,'@',q)
    return p

r=200
s=100
r=call(r,s)
print(r,'@',s)
s=call(s)
print(r,'@',s)