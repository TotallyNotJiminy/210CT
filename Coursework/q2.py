def TrailingZeroCount(Factorial):
    """
    This function counts the number of trailing zeros of a factorial number,
    by checking if is wholy divisible by 5, if so it has a trailing zero, etc.
    """
    Zeroes = 0
    for Factorial in range(2,Factorial+1):          
        while Factorial > 0:
            if Factorial % 5 == 0:
                Zeroes += 1
                Factorial = Factorial/5
            else:
                break
    return Zeroes

#manual input testing
if __name__=="__main__":
    while 1:
        try:
            FactorialTest=int(input("Enter the number you'd like to test: "))
            break
        except:
            print("That's not a valid number!")
    print("The number of trailing 0's in {0} is {1}".format(FactorialTest,TrailingZeroCount(FactorialTest)))
