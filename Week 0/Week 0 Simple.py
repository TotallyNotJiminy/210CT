def p1():
    x=[]
    i=1
    while i!=5:
        try:
            a=int(input("Enter number {0}: ".format(i)))
            x.append(a)
            i+=1
        except:
            print("That's not a number")
            
    if x[0]/x[1]>x[2]/x[3]:
        print(int((x[0]/x[1])))
    else:
        print(int((x[2]/x[3])))

def p2():
    x=[]
    i=1
    while i!=5:
        a=input("Enter co-ordinates {0}: ".format(i))
        if len(a)==5:
            x.append((int(a[1]),int(a[3])))
            i+=1
        else:
            print("That's not a valid co-ordinate")
    if x[3][0]>x[0][0] and x[3][0]>x[1][0] and x[3][0]>x[2][0]:
        print("right")
    elif x[3][0]<x[0][0] and x[3][0]<x[1][0] and x[3][0]<x[2][0]:
        print("left")
    elif x[3][1]>x[0][1] and x[3][1]>x[1][1] and x[3][1]>x[2][1]:
        print("above")
    elif x[3][1]<x[0][1] and x[3][1]<x[1][1] and x[3][1]<x[2][1]:
        print("below")
    else:
        print("not completely to one side")

def p3():
    while 1:
        try:
           x=float(input("Enter your value for x: "))
           break
        except:
            print("Not a valid float")
    if x<-2:
        print((x**2)+(x*4)+4)
    elif x==0:
        print(0)
    elif x>-2:
        print((x**2)+(x*5))

def p4():
    str1=input("Enter your string: ")
    dele=int(input("What letter would you like to remove?: "))
    delenum=int(input("How may letters would you like to remove: "))
    print(str1[:dele]+str1[(dele+delenum):])

def p5():
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    while 1:
        try:
            in1=int(input("Enter the year: "))
            if in1 not in range(0,10000000000):
                print("Not a valid year")
            else:
                break
        except:
            print("not a number, needs to be a year")

    leap=False
    if in1//4==in1/4:
        if in1//100==in1/100:
            if in1//400==in1/400:
                leap=True
        else:
            leap=True

    while 1:
        try:
            in2=int(input("Enter the month number: "))
            if in2 not in range(1,13):
                print("not a valid month(1-12)")
            else:
                break
        except:
            print("That's not a number")

    while 1:
        try:
            in3=int(input("Enter the day: "))
            if in3 not in range(0,31):
                print("not a valid day")
            else:
                break
        except:
            print("That's not a number")

    month=in2-1
    daystot=0
    if leap:
        daystot+=1
    daystot+=in3
    for count in range(0,month):
        daystot+=days[count]
    print("days gone: {0}".format(daystot))
    print("days left: {0}".format(365-daystot))

def p6():
    inlist=[1,4,6,7,2]
    maxval=max(inlist)
    maxidx=inlist.index(maxval)+1
    minval=min(inlist)
    minidx=inlist.index(minval)+1
    print("max is {0} on position {1}, min is {2} on position {3}.".format(maxval,maxidx,minval,minidx))

def main():
    while 1:
        choo=input("")
        if choo=="1":
            p1()
        elif choo=="2":
            p2()
        elif choo=="3":
            p3()
        elif choo=="4":
            p4()
        elif choo=="5":
            p5()
        elif choo=="6":
            p6()
            
if __name__=="__main__":
    main()
    
