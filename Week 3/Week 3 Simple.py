#non recursive
def p1(istring):
    istring=" "+istring
    count=0
    split=[0]
    for each in istring:
        if each ==" ":
            split.append(count)
        count+=1
    split.append(len(istring))
    rstring=""
    for count in range(len(split)-1,-1,-1):
        rstring+=istring[split[count-1]:split[count]]
    return rstring

#recursive
def p1b(istring,wordlist):
    for count in range(0,len(istring)):
        if istring[count]==" ":
            wordlist.append(istring[:count])
            p1b(istring[count+1:],wordlist)
            break
    rstring=""     
    for each in wordlist:
        rstring=each+" " + rstring
    return rstring

def p3(n,p):
    if n == 0 or n ==1:
        return True
    else:
        if not p%n:
            return False
        else:
            return(p3(n-1,p))

def p4(istring,pointer):
    if pointer>len(istring)-1:
        return istring
    
    elif istring[pointer].lower() in ["a","e","i","o","u"]:
        istring=istring[:pointer]+istring[pointer+1:]
        
    else:
        pointer+=1
    istring=p4(istring,pointer)
    return istring
            

def main():
    while 1:
        print()
        print("Select what you would like to run: ")
        print()
        print("1. Reverse a sentence (non recursive)")
        print("2. Reverse a sentence (recursive)")
        print("3. Check if a number is prime")
        print("4. Remove vowels from a string")
        print("9. Quit")
        print()
        print("What would you like to choose: ")
        try:
            choice=int(input())
        except:
            print("That's not a valid number!")
            choice=None

        if choice==1:
            istring=input("Please enter the sentence you would like to reverse: ")
            output=p1(istring)
            print(output)

        elif choice==2:
            istring=input("Please enter the sentence you would like to reverse: ")+ " "
            rstring=p1b(istring,[])
            print(rstring)
            
        elif choice==3:
            try:
                n=int(input("Please enter a number: "))
                if n>0:
                    valid=True
                else:
                    print("That's not a valid number!")
                    valid=False
            except:
                valid=False
                print("That's not a valid number")
            if valid:
                print()
                if p3(n-1,n):
                    
                    print("It is prime")
                else:
                    print("It's not prime")
            
        elif choice==4:
            istring=input("Please enter text with vowels in: ")
            print()
            print(p4(istring,0))

        
        elif choice==9:
            break
        
        else:
            print()
            print("That's not correct! (1-9)")
        

if __name__=="__main__":
    main()
    
