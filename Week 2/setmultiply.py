import random

def setmultiply(sets,iteration):
    if iteration==0:
        return sets[0]
    else:
        for item in range(0,len(sets[0])):
            sets[0][item]=sets[0][item]*sets[iteration][item]
        setmultiply(sets,iteration-1)
        return sets[0]

def setadd(sets):
    pass

def setsubtract(self):
    pass

def gensets(length):
    sets=[]
    for count in range(0,length):
        sets.append(random.randint(1,5))
    return sets

def main():
    sets=[gensets(15),gensets(15),gensets(15),gensets(15),gensets(15),gensets(15)]
    sets=setmultiply(sets,len(sets)-1)
    print(sets)
if __name__=="__main__": 
    main()
