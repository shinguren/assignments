def calc_interest(p,r,t):
    return(p*r*t/100)

P=int(input("enter principal amount:"))
R=float(input("enter rate of interest:"))
T=int(input("enter time period:"))
si= calc_interest(P,R,T)
print("simple interest is", si)