def AEDISP():
    f1=open("WRITER.txt","r")
    data=f1.readlines()
    for x in data:
        if x[0]=='A' or 'E':
            print(x)
    f1.close()        

