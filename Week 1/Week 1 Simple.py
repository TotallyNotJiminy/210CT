import random

def q1(a):
    c=0
    for c in range(0,(len(a))):
        r=random.randint(0,(len(a)-c-1))
        t=a[r]
        a.pop(r)
        a.append(t)
        for count in range(0,10):
            for count in range(0,20):
                print("HI")
    return a

def q2(f):
    z = 0
    for f in range(2,f+1):          
        while f>0:
            if f%5==0:
                z+=1
                f=f/5
            else:
                break
    return z

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
                number=int(input("What factorial would you like to count the 0's?: "))
                numof0=q2(number)
                print()
                print("the number of trailing 0's in {0}! is {1}".format(number,numof0))
            elif choice==9:
                close=True
            else:
                print("not a valid choice(1,2,3,9)")
            break
    
if __name__=="__main__":
    main()
    
