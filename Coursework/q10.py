import random

"""
    this function finds the longest acending sequence within another sequence
    I initially used recursion to achieve this but it felt forced and not a
    truely recursive function, so i have created this iterative approach
    with a temporary list, that finds acending sequences, when it finds the
    end of a sequence, it compares the length of the temporary list with the
    length of the longest list it has found so far, if it is equal or less no
    action is taken, if it is longer it becomes the longest list, at the end,
    you have the longest sequence
"""
def SubsequenceExtract(Sequence):
    Pointer=1
    TempLow=0
    TempHigh=0
    SubList=[]
    #the try except catch is to allow if the list goes out of index yet the sublist still works
    try:
        while Pointer<=len(Sequence):
            #could of had it >= but decided not to, to include that change here
            if Sequence[Pointer]>Sequence[Pointer-1]:
                TempHigh=Pointer
            else:
                if TempHigh-TempLow>=len(SubList):
                    SubList=Sequence[TempLow:TempHigh+1]
                TempLow=Pointer
            Pointer+=1
    except IndexError:
        if TempHigh-TempLow>=len(SubList):
            SubList=Sequence[TempLow:TempHigh+1]
    return SubList

def genrandomsequence():
    Sequence=[]
    for count in range(0,random.randint(0,200)):
        Sequence.append(random.randint(0,100))
    return Sequence
    
def main():
    while 1:
        a=0
        print("Sub-Suquence Extraction")
        print("1. Random Test")
        print("2. Manually Input Parameters")
        print("3. Hardcode Input")
        print("9. Quit")
        print()
        while 1:
            try:
                choice=int(input("Please enter your choice: "))
                if choice in [1,2,3,9]:
                    break
            except:
                print("That's not a valid input")
            
        if choice==9:
            break
        if choice==1:
            Sequence=genrandomsequence()
        elif choice==2:
            Sequence=[]
            print("q to quit")
            while 1:
                try:
                    temp=input(": ")
                    if temp=="q":
                        break
                    Sequence.append(int(temp))
                except:
                    print("That's not a valid number!")
        elif choice==3:
            Sequence=[1,2,3,4,5,1,1,1,1,1,1,2,3,4,5,6,1,1,1]
            
        print()
        sublist=SubsequenceExtract(Sequence)
        print("Longest Sequence: {0}".format(len(sublist)))
        print(sublist)
        print()
        
        
            
if __name__=="__main__":
    main()
    
