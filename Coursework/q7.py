"""
    This function checks if a number is a prime number, you pass in the number
    you want to check and that same number -1 since the function is recursive
    """

def PrimeNumber(Number,Divide):
    if Divide == 1:
        return True
    else:
        if Number//Divide == Number/Divide:
            return False
        else:
            return PrimeNumber(Number,Divide-1)

def main():
    prime=[]
    actualprime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for count in range(2,500):
        if PrimeNumber(count,count-1):
            prime.append(count)
    print(prime)
    print()

    print("Any missed: ")
    missed=False
    for each in actualprime:
        if each not in prime:
            missed=True
            print(each)
    if not missed:
        print("No inconsistencies")


if __name__=="__main__":
    main()
