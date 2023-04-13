def upperlower():
    s=input("enter string:")
    upper,lower=0,0
    for i in s:
        if i.isupper():
           upper+=1
        elif i.islower():
           lower+=1
        else:
           pass
    print ("original string : ", s)
    print ("number of uppercase letters:", upper)
    print ("number of lowercase letters:", lower)

upperlower()