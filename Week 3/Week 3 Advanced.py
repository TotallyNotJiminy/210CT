import random

def blocks(blocklist,p):
    if p==0:
        return blocklist
    reorder=[]
    if blocklist[p][0]==blocklist[p-1][0]:
        for each in blocklist:
            if each[1]==blocklist[p][1]:
                reorder.append(each)
        if len(reorder)==1:
            blocklist.pop(p-1)
        else:
            print(reorder)
    blocklist=blocks(blocklist,p-1)
    return blocklist
        
        
    #return tower
def possible(tower):
    lasblock=["weuqinwib",99999999999999999]
    for block in tower:
        if block[0]==lastblock[0] or block[1]>lastblock[1]:
            return False
        lastblock=block
    return True

def genblocks(n):
    blocklist=[]
    for count in range(0,n):
        blocklist.append((random.choice(["y","b","g","r","p"]),random.randint(0,50)))
    return blocklist

def sortblocks(blocklist):
    bubble = True
    passnum = len(blocklist)-1
    while passnum > 0 and bubble:
       bubble = False
       for i in range(passnum):
           if blocklist[i][1]>blocklist[i+1][1]:
               bubble = True
               temp = blocklist[i]
               blocklist[i] = blocklist[i+1]
               blocklist[i+1] = temp
       passnum = passnum-1
    return blocklist

def main():
    n=30
    blocklist=genblocks(n)
    blocklist=sortblocks(blocklist)
    tower=blocks(blocklist,len(blocklist)-1)
    for each in tower:
        print(each)
if __name__=="__main__":
    main()
    
