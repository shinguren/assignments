def demo1():
    z=50
    def demo2():
        global z
        z = 20
        print(z, end ='@')
    print(z, end='@')
    demo2()
    print(z, end='@')
demo1()
print(z)
