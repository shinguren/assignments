def func4(mylist):
    print("\n inside called function")
    print("list is ", mylist)
    newlist=[3,5]
    mylist=newlist
    mylist.append(6)
    print("changed list inside the function",mylist)

list1=[1,4]
print("\n before calling list was", list1)
func4(list1)
print("\n after returning from function list is", list1) 