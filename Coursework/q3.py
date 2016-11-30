def PerfectSquare(i):
    if i<=1:
        return i
    else:
        if i**0.5==int(i**0.5):
            return i
        else:
            i=PerfectSquare(i-1)
            return i
        
def main():
    while 1:
        try:
            TestNumber=int(input("Please enter the number you'd like to check: "))
            #recursion limit
            if TestNumber<=1000993:
                break
            else:
                print("That's too big!")
        except ValueError:
            print("That's not a number!")
    SquareNum=PerfectSquare(TestNumber)
    print(SquareNum)
    
def test():
    t=1000990
    while 1:
        print(t)
        r=PerfectSquare(t)
        t+=1
        
if __name__=="__main__":
    #test()
    main()
    
