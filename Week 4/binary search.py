import random

def binary_search(array,lowval,highval):
    low = 0
    upper = len(array)
    while low < upper:
        x = low + (upper - low) // 2
        val = array[x]
        if lowval<=val<=highval:
            return True
        elif highval > val:
            if low == x:
                return False
            low = x
        elif lowval < val:
            upper = x
    return False

def test(passes):
    testcondition=[]
    for count in range(0,passes):
        array=[]
        for count in range(0,50):
            array.append(random.randint(0,500))
        array.sort()
        lower=random.randint(100,120)
        higher=random.randint(100,120)
        
        if lower<higher:
            testcondition.append((array,lower,higher))
        else:
            testcondition.append((array,higher,lower))

    passfail=[0,[]]
    testno=0
    for each in testcondition:
        testno+=1
        possiblelist=[]
        predict=False
        
        for count in range(each[1],each[2]+1):
            if count in each[0]:
                predict=True
                
        actual=binary_search(each[0],each[1],each[2])
        print()
        print("Test #{0}: ".format(testno))
        print("Predicted Outcome: {0}".format(predict))
        print("Actual Outcome: {0}".format(actual))                             
        if predict==actual:
            passfail[0]+=1
        else:
            passfail[1].append(each)
    print()
    print("Total Runs: {0}".format(passfail[0]+len(passfail[1])))
    print("Total Successful Passes: {0}".format(passfail[0]))
    print("Total Fail Passes: {0}".format(len(passfail[1])))
    print("Success Rate: %{0}".format((passfail[0]/(passfail[0]+len(passfail[1])))*100))
    for each in passfail[1]:
        print()
        print("Fail Case: ")
        print("List: {0}".format(each[0]))
        print("Lower: {0}".format(each[1]))
        print("Upper: {0}".format(each[2]))
        
def manual_enter():
    print("enter the value you would like to the list (-1 to quit)")
    array=[]
    while 1:
        try:
            append=int(input())
            if append==-1:
                break
            else:
                array.append(append)
        except:
            print("That's not a valid number!")
    array.sort()
    while 1:
        try:
            lowval=int(input("Please enter your lower value: "))
            highval=int(input("Please enter your high value: "))
            break
        except:
            print("That's not a valid input")
    return binary_search(array,lowval,highval)

def main():
    while 1:
        print()
        print("Binary Search Algorithm")
        print()
        print("1. Manual Enter Values")
        print("2. Use Random Test Set Parameters")
        print("9. Quit")
        print()
        print("Please Select an option")
        try:
            choice=int(input())
        except:
            print("That's not a valid number!")
            choice==None
        if choice==1:
            print(manual_enter())
        elif choice==2:
            while 1:
                try:
                    passes=int(input("Enter the amount of passes you would like to test: "))
                    if passes>0:
                        break
                    else:
                        print("that's not a valid number")
                except:
                    print("That's not a valid number")
                    
            test(passes)
        elif choice==9:
            break
            
if __name__=="__main__":
    main()
