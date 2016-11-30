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
                if TempHigh-TempLow>len(SubList):
                    SubList=Sequence[TempLow:TempHigh+1]
                TempLow=Pointer
            Pointer+=1
    except IndexError:
        print(TempLow)
        print(TempHigh)
        if TempHigh-TempLow>len(SubList):
            SubList=Sequence[TempLow:TempHigh+1]
    return SubList
        
print(SubsequenceExtract([1,2,3,4,5,4]))
