from opcode import stack_effect


stack=[1,2,3,4,5]
print("original stack is", stack)
a=int(input("enter the element:"))
stack.append(a)
print("stack is now",stack)
A=stack.pop()
print("deleted statment is",A)
print("stack is now", stack)
i=len(stack)-1
print("value obtained after peep:",stack[i])
