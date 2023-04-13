def display(stk):
    if stk==[]:
        print("stack is empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-top")
        for i in range(top-1,-1,-1):
            print(stk[i])

def push(stk, item):
    stk.append(item)

def pop(stk):
    if stk==[]:
        return 'under flow'
    else:
        item=stk.pop()
        return item
    
stack=[]
top=None
while True:
    print("\n STACK OPERATIONS")
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    print("4.EXIT")
    ch=int(input("enter your choice(1-4):"))
    if ch==1:
        item=int(input("ente element to add:"))
        push(stack,item)
    elif ch==2:
        item=pop(stack)
        if item=="under flow":
            print("under flow, stack is empty")
        else:
            print("popped item is",item)
    elif ch==3:
        display(stack)
    elif ch==4:
        break
    else:
        print("invalid choice")