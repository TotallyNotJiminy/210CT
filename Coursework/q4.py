import random

def ListShuffle(IntergerList):
    Pointer = 0 #O(1)
    for Pointer in range(0,(len(IntergerList))):#O(n)
        Random=random.randint(0,(len(IntergerList)-Pointer-1)) #O(n)
        Temporary = IntergerList[Random]#O(n)
        IntergerList.pop(Random)#O(n)
        IntergerList.append(Temporary)#O(n)
                              
    return IntergerList #O(1)
    
def TrailingZeroCount(Factorial):
    Zeroes = 0 #O(1)
    for Factorial in range(2,Factorial+1):   #O(n)       
        while Factorial > 0: #O(n^2)
            if Factorial % 5 == 0: #O(n^2)
                Zeroes += 1 #O(n^2)
                Factorial = Factorial/5 #O(n^2)
            else: #O(n^2)
                break #O(n^2)
    return Zeroes #O(1)
