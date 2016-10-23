import random

#solving with dictionary

def taska(a,b):
    dica=gendic(a)
    dicb=gendic(b)
    strc=("")
    
    for each in dica:
        
        if dica[each]<=dicb[each]:
            strc+=(each)*dica[each]
        else:
            strc+=(each)*dicb[each]
            
    return strc

def taskb(a,b):
    dica=gendic(a)
    dicb=gendic(b)
    strc=("")

    for each in dica:
        if dica[each]!=0 or dicb[each]!=0:
            strc+=each
            
    return strc

def taskc(a,b):
    dica=gendic(a)
    dicb=gendic(b)
    strc=("")

    for each in dica:
        if(dica[each]-dicb[each])>0:
            strc+=each*(dica[each]-dicb[each])

    return strc
        
def gendic(a):
    dica={"0": 0,"1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0,"8": 0,"9": 0}    
    for each in a:
        dica[each]+=1
    return dica
        
def genstring(length):
    a=("")
    for count in range(0,length):
        a+=str((random.randint(0,100)))
    return a

def main():
    
    a=genstring(random.randint(0,10))
    b=genstring(random.randint(0,10))
    while 1:
        choice=input()
        
        if choice=="a":
            c=taska(a,b)

        elif choice=="b":
            c=taskb(a,b)

        elif choice=="c":
            c=taskc(a,b)
            
        elif choice=="p":
            choice=input()
            if choice=="a":
                print(a)
            elif choice=="b":
                print(b)
            elif choice=="c":
                print(c)
                    
        elif choice=="q":
            break
        

    
if __name__=="__main__":
    main()
