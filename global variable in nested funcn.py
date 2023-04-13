
def fun1():
    x=100
    def fun2():
        global x
        x=200
        print("before calling fun2:"+str(x))
        print("calling fun2 now:")
        fun2()
        print("after calling fun2:",+str(x))
        fun1()
        print("x in main:"+str(x))

fun1()