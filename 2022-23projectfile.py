import math as m
import random
import time

# BILL

def bill():
    print("                             Pacific D21\n                           Dwarka Sector-21,\n                             New Delhi")
    print("------------------------------------|---------------------------------\n         |1.| Cosmetics|            |        |2 .| Provision|\n____________________________________|_________________________________\n\
1. Creme -             Rs150/pc     | 1. Wheat Flour -     Rs39/kg\n\
2. Moisturizer -       Rs210.76/pc  | 2. Maida -           Rs45/kg\n\
3. Powder -            Rs59/pc      | 3. Pulses -          Rs126/kg\n\
4. Foundation -        Rs78/pc      | 4. Maggi -           Rs12/pc\n\
5. Nail Paint -        Rs20/pc      | 5. Rice -            Rs78/kg\n\
6. Remover -           Rs23.6/pc    | 6. Basmati -         Rs92/kg\n\
7. Blush -             Rs199/pc     | 7. Refined oil -     Rs135/L\n\
------------------------------------|---------------------------------\n\
         |3.|    Edible|            |          |4.|    Frozen|\n____________________________________|_________________________________\n\
1. Layz chips  -       Rs10/pkt     | 1. Buffalo Milk -    Rs69/L\n\
2. Kurkure  -          Rs20/pkt     | 2. Cow Milk -        Rs58/L\n\
3. Khatta Meetha -     Rs25/pkt     | 3. Paneer -          Rs70/150gm\n\
4. Sprite -            Rs40/500mL   | 4. Buttermilk -      Rs20/100mL\n\
5. Coca~Cola -         Rs65/500mL   | 5. Masala Butermilk- Rs35/150mL\n\
6. Bhujia -            Rs15/pkt     | 6. Cheese -          Rs80/200gm\n\
7. Dairy Milk -        Rs40/pkt     | 7. Frozen Peas -     Rs120/kg\n\
------------------------------------|---------------------------------")

bill()	

def amount():
    a=int(input("Enter amount of object :"))
    return a

lst=[]
total=0

# DEFINING PARTICULAR FUNCTIONS
def Cosmetics():
    print("--SELECT FURTHER FOR BILLING--")
    print("--------------o---------------")
    print("XX PRESS '0' TO EXIT & PRESS 9 TO PRINT BILL XX")
    print("--------------o---------------")
    global lst
    global total
    while True:
        try:
            n=int(input("Enter product number to choose :"))
            if n==1:
                print("--You selected Creme--")
                a=amount()
                c=a*150
                total+=c
                lst.append(['Creme - Rs150',c,a])
            elif n==2:
                print("--You selected Moisturizer--")
                a=amount()
                c=a*210
                total+=c
                lst.append(['Moisturizer - Rs210',c,a])
            elif n==3:
                print("--You selected Powder--")
                a=amount()
                c=a*59
                total+=c
                lst.append(['Powder - Rs59',c,a])
            elif n==4:
                print("--You selected Foundation--")
                a=amount()
                c=a*78
                total+=c
                lst.append(['Foundation - Rs78',c,a])
            elif n==5:
                print("--You selected Nail Paint--")
                a=amount()
                c=a*20
                total+=c
                lst.append(['Nail Paint - Rs20',c,a])
            elif n==6:
                print("--You selected Remover--")
                a=amount()
                c=a*23.6
                total+=c
                lst.append(['Remover - Rs23.6',c,a])
            elif n==7:
                print("--You selected Blush--")
                a=amount()
                c=a*199
                total+=c
                lst.append(['Blush - Rs199',c,a])
            elif n==0:
                print("---------------\U0001F917-------------")
                print()
                print("XX BILLING OVER FOR 'COSMETICS' SECTION XX")
                print()
                print("---------------\U0001F917-------------")
                break
            elif n==9:
                bill()
            else:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("XX INVALID INPUT ENTER AGAIN XX")
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        except:
            print("--------------o---------------")
            print("-----PLEASE ENTER A VALUE-----")
            print("--------------o---------------")
    return total,lst

def Provision():
    print("--SELECT FURTHER FOR BILLING--")
    print("--------------o---------------")
    print("XX PRESS '0' TO EXIT & PRESS 9 TO PRINT BILL XX")
    print("--------------o---------------")
    global total
    global lst
    while True:
        try:
            n=int(input("Enter product number to choose :"))
            if n==1:
                print("--You selected Wheat Flour--")
                a=amount()
                c=a*39
                total+=c
                lst.append(['Wheat Flour - Rs39',c,a])
            elif n==2:
                print("--You selected Maida--")
                a=amount()
                c=a*45
                total+=c
                lst.append(['Maida - Rs45',c,a])
            elif n==3:
                print("--You selected Pulses--")
                a=amount()
                c=a*126
                total+=c
                lst.append(['Pulses - Rs126',c,a])
            elif n==4:
                print("--You selected Maggi--")
                a=amount()
                c=a*12
                total+=c
                lst.append(['Maggi - Rs12',c,a])
            elif n==5:
                print("--You selected Rice--")
                a=amount()
                c=a*78
                total+=c
                lst.append(['Rice - Rs78',c,a])
            elif n==6:
                print("--You selected Basmati--")
                a=amount()
                c=a*92
                total+=c
                lst.append(['Basmati - Rs92',c,a])
            elif n==7:
                print("--You selected Refined Oil--")
                a=amount()
                c=a*135
                total+=c
                lst.append(['Refined oil - Rs135',c,a])
            elif n==0:
                print("---------------\U0001F917-------------")
                print()
                print("XX BILLING OVER FOR 'PROVISIONS' SECTION XX")
                print()
                print("---------------\U0001F917-------------")
                break
            elif n==9:
                bill()
            else:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("XX INVALID INPUT ENTER AGAIN XX")
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        except:
            print("--------------o---------------")
            print("-----PLEASE ENTER A VALUE-----")
            print("--------------o---------------")
    return total,lst

def Edible():
    print("--SELECT FURTHER FOR BILLING--")
    print("--------------o---------------")
    print("XX PRESS '0' TO EXIT & PRESS 9 TO PRINT BILL XX")
    print("--------------o---------------")
    global total
    global lst
    while True:
        try:
            n=int(input("Enter product number to choose :"))
            if n==1:
                print("--You selected Layz chips--")
                a=amount()
                c=a*10
                total+=c
                lst.append(['Layz Chips - Rs10',c,a])
            elif n==2:
                print("--You selected Kurkure--")
                a=amount()
                c=a*20
                total+=c
                lst.append(['Kurkure - Rs20',c,a])
            elif n==3:
                print("--You selected Khatta Meetha--")
                a=amount()
                c=a*25
                total+=c
                lst.append(['Khatta Meetha - Rs25',c,a])
            elif n==4:
                print("--You selected Sprite--")
                a=amount()
                c=a*40
                total+=c
                lst.append(['Sprite - Rs40',c,a])
            elif n==5:
                print("--You selected Coca~Cola--")
                a=amount()
                c=a*65
                total+=c
                lst.append(['Coca~Cola - Rs65',c,a])
            elif n==6:
                print("--You selected Bhujia--")
                a=amount()
                c=a*15
                total+=c
                lst.append(['Bhujia - Rs15',c,a])
            elif n==7:
                print("--You selected Dairy Milk--")
                a=amount()
                c=a*40
                total+=c
                lst.append(['Dairy Milk - Rs40',c,a])
            elif n==0:
                print("---------------\U0001F917-------------")
                print()
                print("XX BILLING OVER FOR 'EDIBLE' SECTION XX")
                print()
                print("---------------\U0001F917-------------")
                break
            elif n==9:
                bill()
            else:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("XX INVALID INPUT ENTER AGAIN XX")
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        except:
            print("--------------o---------------")
            print("-----PLEASE ENTER A VALUE-----")
            print("--------------o---------------")
    return total,lst

def Frozen():
    print("--SELECT FURTHER FOR BILLING--")
    print("--------------o---------------")
    print("XX PRESS '0' TO EXIT & PRESS 9 TO PRINT BILL XX")
    print("--------------o---------------")
    global total
    global lst
    while True:
        try:
            n=int(input("Enter product number to choose :"))
            if n==1:
                print("--You selected Buffalo Milk--")
                a=amount()
                c=a*69
                total+=c
                lst.append(['Buffalo Milk - Rs69',c,a])
            elif n==2:
                print("--You selected Cow MIlk--")
                a=amount()
                c=a*58
                total+=c
                lst.append(['Cow Milk - Rs58',c,a])
            elif n==3:
                print("--You selected Paneer--")
                a=amount()
                c=a*70
                total+=c
                lst.append(['Paneer - Rs70',c,a])
            elif n==4:
                print("--You selected Buttermilk--")
                a=amount()
                c=a*20
                total+=c
                lst.append(['Buttermilk - Rs20',c,a])
            elif n==5:
                print("--You selected Masala Buttermilk--")
                a=amount()
                c=a*35
                total+=c
                lst.append(['Masala Buttermilk - Rs35',c])
            elif n==6:
                print("--You selected Cheese--")
                a=amount()
                c=a*80
                total+=c
                lst.append(['Cheese - Rs80',c,a])
            elif n==7:
                print("--You selected Frozen Peas--")
                a=amount()
                c=a*120
                total+=c
                lst.append(['Frozen Peas - Rs120',c,a])
            elif n==0:
                print("---------------\U0001F917-------------")
                print()
                print("XX BILLING OVER FOR 'FROZEN' SECTION XX")
                print()
                print("---------------\U0001F917-------------")
                break
            elif n==9:
                bill()
            else:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("\u001b[31;1m"+"XX INVALID INPUT ENTER AGAIN XX")
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        except:
            print("--------------o---------------")
            print("-----PLEASE ENTER A VALUE-----")
            print("--------------o---------------")
    return total,lst

# MAIN PROGRAM
while True:
    try:
        n=int(input("--Enter Choice for Particulars--:"))
        if n==1:
            print("---------------\U0001F917-------------")
            print()
            print("NOW ENTERING COSMETICS SECTION",end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.'),time.sleep(1)
            print()
            print("---------------\U0001F917-------------")
            Cosmetics()
        elif n==2:
            print("---------------\U0001F917-------------")
            print()
            print("NOW ENTERING PROVISION SECTION",end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.'),time.sleep(1)
            print()
            print("---------------\U0001F917-------------")
            Provision()
        elif n==3:
            print("---------------\U0001F917-------------")
            print()
            print("NOW ENTERING EDIBLE SECTION",end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.'),time.sleep(1)
            print()
            print("---------------\U0001F917-------------")
            Edible()
        elif n==4:
            print("---------------\U0001F917-------------")
            print()
            print("NOW ENTERING FROZEN SECTION",end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.'),time.sleep(1)
            print()
            print("---------------\U0001F917-------------")
            Frozen()
        elif n==0:
            break
        else:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
            print("XX INVALID INPUT ENTER AGAIN XX")
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    except:
        print("--------------o---------------")
        print("-----PLEASE ENTER A VALUE-----")
        print("--------------o---------------")
print()
print()

# COMBINING COMMON ITMES
kval = {};rmk=[]
for i in range(len(lst)):
    for j in kval.keys():
        if kval[j]["name"] == lst[i][0]:
            kval[j]["value"]+=lst[i][1]
            kval[j]["quantity"]+=lst[i][2]
        else:
            if j not in rmk:
                rmk.append(j)

    kval[i] = {
        "name" : lst[i][0],
        "value" : lst[i][1],
        "quantity" : lst[i][2]
    }
elements = []
for i in rmk:
    elements.append(kval.pop(i))
N = []
for i in elements:
    lst1 = [i["name"],i["value"],i["quantity"]]
    N.append(lst1)
    
# PRINTING BILL
if len(N)>0:
    print("Loading bill",end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.',end=''),time.sleep(1),print('.')
    time.sleep(1)
    print("                        Bill No. : ",random.randint(1,1000))
    print("---------------------------------BILL---------------------------------")
    print("Sl.no.     Item Desc                   Item Amount      Item total")
    x=0
    for i in range(len(N)):
        print(i+1,'       ',N[i][0],'\t',end='')
        print('             ',N[i][2],end='')
        print('              ',N[i][1])
        x+=N[i][2]
    print("----------------------------------------------------------------------")
    print("Total Items : ",x,'                              ',"Total Fare : ",total)
    print("GST tax Perc :                                                12%")
    y=12/100*(total)
    print("GST tax amount :                                              %0.2f"%y)
    x=(12/100*(total))+total
    print("Total Payable :                                               %0.2f"%x)
else:
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()
    print("        BILL EMPTY         ")
    print()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("----------------------------------------------------------------------")
print("                  THANK YOU FOR BILLING!!! ")
print("                      \U0001F600")
print("                         HAVE A GOOD DAY!!! ")
print("----------------------------------------------------------------------")
