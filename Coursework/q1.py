import random

def ListShuffle(IntergerList):
    """
    This funtion takes an input list, and shuffles the values randomly, to keep the function as efficient as I can
    yet and only running once per item in the list ( O(n) ). It takes a random value from the list, with a pointer
    that points at the end of the unshuffled values of the list, it takes a random item from that list and adds it
    to the end of list. it then iterates and points at the next item in the unshuffled list, this completely
    randomises the list without moving items more than once, as efficient as I could make it.
    """
    Pointer = 0
    for Pointer in range(0,(len(IntergerList))):
        #the random integer generation is a built in python funtion, as i didn't want to have to do it myself
        #it generates a number that correlates with a remaining unshuffled number 
        Random=random.randint(0,(len(IntergerList)-Pointer-1))           
        #having a temporary varable, popping the original, and appending the temporary one is how i edit the list
        Temporary = IntergerList[Random]
        IntergerList.pop(Random)
        IntergerList.append(Temporary)
                              
    return IntergerList

if __name__ == "__main__":
    #this is for testing purposes only, if you run this program it will run this code, if you import this 
    OriginalList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    SortedList = OriginalList[:]
    ListShuffle(SortedList)
    print("Original List")
    print(OriginalList)
    print()
    print("Sorted List")
    print(SortedList)

