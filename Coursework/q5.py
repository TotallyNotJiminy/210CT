import csv
import random
#algorithm for q1
def q1(l,h,e):         
    for d in range(0,len(l)):
        try:
            l[d+1]+=l[d]
            l[d+h-1]+=(l[d]*e)
        except IndexError:
            pass
    return l

#algoritm for q2
def matrixcalc(a,b,f):
    c=[]
    for q in a:
        m=False
        for w in b:
            if q[0]==w[0] and q[1]==w[1]:
                m=True
                if f==1:
                    c.append((q[0],q[1],(q[2]+w[2])))
                elif f==2:
                    c.append((q[0],q[1],(q[2]-w[2])))
                elif f==3:
                    c.append((q[0],q[1],(q[2]*w[2]))) 
                break
        if not m:
            c.append(q)
    return c

def q2():
    a=generate_matrix(100)
    b=generate_matrix(100)
    while 1:
        print()
        print("what would you like to do?")
        print("add")
        print("sub")
        print("mul")
        print("quit")
        print()
        choose=input()
        if choose=="add":
            c=matrixcalc(a,b,1)
            print(c)
            
        elif choose=="sub":
            c=matrixcalc(a,b,2)
            print(c)
            
        elif choose=="mul":
            
            c=matrixcalc(a,b,3)
            print(c)
        elif choose=="quit":
            break
        elif choose=="exp":
            export_matrix(c)
        else:
            print("Not one of the commands")
        
def generate_matrix(size):
    #i have chosen to store it as a list of coordinates as its probably more effient
    #for a sparce matrix rather than representing every index individually
    matrix=[]
    for count in range(0,size):
        for count2 in range(0,100):
            if random.randint(0,25)==4:
                matrix.append((count,count2,random.randint(0,99)))
    return matrix


    
    
def export_matrix(c):
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    for each in c:
        sheet1.write(each[0],each[1],each[2])
    
def main():
    while 1:
        print("1. Alien Invasion Question")
        print("2. Matrix Maths")
        print("9. Quit")
        try:
            choice=int(input("Please choose: "))
        except:
            print("Not a valid input")
            choice=0
        if choice==0:
            pass
        elif choice ==1:
            while 1:
                try:
                    #input
                    eggs=int(input("how many eggs does the alien lay: "))
                    hatch=int(input("how long does it take for each egg to hatch: "))
                    if hatch>0 and eggs>0:
                        break
                    else:
                        print("That's not valid")
                except:
                    print("Not a valid input")
            alienlist=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            aliens=q1(alienlist,hatch,eggs)
            count=1
            #output
            for each in aliens:
                if each==1:
                    aliens="alien"
                else:
                    aliens="aliens"
                print("on day {0} there will be {1} {2}.".format(count,each,aliens))
                count+=1
        elif choice==2:
            q2()
        elif choice==9:
            break
        else:
            print("Not a valid input")


if __name__=="__main__":
    main()
