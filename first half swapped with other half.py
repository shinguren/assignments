def half(List):
    if len(List)%2==0:
        start=0
    else:
        start=1
    L=len(List)//2
    for i in range(L):
        temp=List[i]
        List[i]=List[i+L+start]
        List[i+L+start]=temp
    
List=[1,2,3,4,5,6,7,8,9,10]
half(List)
print(List)

