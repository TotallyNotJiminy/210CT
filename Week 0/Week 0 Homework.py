import random
def q1(intlist):
    #i know i could use random.shuffle but that kind of defeats the point
    #i also know that generating a random interger is a shortcut
    #i could do it via the on board clock to generate a random number but i feel that it isn't necessary
    count=0
    for count in range(0,(len(intlist))):
        randint=random.randint(0,(len(intlist)-count-1))
        temp=intlist[randint]
        intlist.pop(randint)
        intlist.append(temp)
        count+=1
    print(intlist)

def q2():
    factorial=int(input("What factorial would you like to count the 0's?"))
    number=getresult(factorial)
    numof0=0
    for count in range(len(str(number))-1,-1,-1):
        if str(number)[count]!="0":
            break
        numof0+=1
    print("the number of trailing 0's in {0} is {1}".format(number,numof0))
    
def getresult(n):
    if n == 0:
        return 1
    else:
        return n * getresult(n-1)

def q3():
    while 1:
        try:
            eggs=int(input("how many eggs does the alien lay: "))
            hatch=int(input("how long does it take for each egg to hatch: "))
            if hatch>0 and eggs>0:
                break
            else:
                print("That's not valid")
        except:
            print("Not a valid input")
    aliens=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for day in range(0,31):
        try:
            aliens[day+1]+=aliens[day]
        
            aliens[day+hatch]+=(aliens[day]*eggs)
        except IndexError:
            pass
    count=1
    for each in aliens:
        print("on day {0} there will be {1} aliens.".format(count,each))
        count+=1
    
        
        
        
def main():
    close=False
    while not close:
        print()
        print("Select what question you like to solve?")
        print("1. Shuffle an array of intergers")
        print("2. Count the number of trailing 0's in a factorial number")
        print("3. ADVANCED - predict the number of eggs an alien will lay")
        print("9. Quit")
        print()
        while 1:
            try:
                choice=int(input("what would you like to do?: "))
            except:
                print("that's not a valid number")
                choice=0
                
            if choice==1:
                    q1([5,3,8,6,1,9,2,7])
            elif choice==2:
                q2()
            elif choice==3:
                q3()
            elif choice==9:
                close=True
            else:
                print("not a valid choice(1,2,3,9)")
            break
    
if __name__=="__main__":
    main()
    
