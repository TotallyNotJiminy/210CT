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
    return intlist

def q2():
    #input
    factorial=int(input("What factorial would you like to count the 0's?"))
    number=getresult(factorial)
    numof0=0
    for count in range(len(str(number))-1,-1,-1):
        if str(number)[count]!="0":
            break
        numof0+=1
    #output
    print("the number of trailing 0's in {0} is {1}".format(number,numof0))
    
def getresult(n):
    if n == 0:
        return 1
    else:
        return n * getresult(n-1)        
        
def main():
    close=False
    while not close:
        print()
        print("Select what question you like to solve?")
        print("1. Shuffle an array of intergers")
        print("2. Count the number of trailing 0's in a factorial number")
        print("9. Quit")
        print()
        while 1:
            try:
                choice=int(input("what would you like to do?: "))
            except:
                print("that's not a valid number")
                choice=0
                
            if choice==1:
                    print(q1([5,3,8,6,1,9,2,7]))
            elif choice==2:
                q2()
            elif choice==9:
                close=True
            else:
                print("not a valid choice(1,2,3,9)")
            break
    
if __name__=="__main__":
    main()
    
