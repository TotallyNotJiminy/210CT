import csv
import random
def q1():
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
    aliens=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for day in range(0,31):
        try:
            aliens[day+1]+=aliens[day]
        
            aliens[day+hatch]+=(aliens[day]*eggs)
        except IndexError:
            pass
    count=1
    #output
    for each in aliens:
        print("on day {0} there will be {1} aliens.".format(count,each))
        count+=1

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
            c=add_matrix(a,b)
            print(c)
            
        elif choose=="sub":
            c=subtract_matrix(a,b)
            print(c)
            
        elif choose=="mul":
            
            c=multiply_matrix(a,b)
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

def add_matrix(a,b):
    c=[]
    for eacha in a:
        match=False
        
        for eachb in b:

            if eacha[0]==eachb[0] and eacha[1]==eachb[1]:
                match=True
                c.append((eacha[0],eacha[1],(eacha[2]+eachb[2])))                
                break
            
        if not match:
            c.append(eacha)


            
    for eachb in b:
        match=False
        
        for eacha in a:
            
            if eacha[0]==eachb[0] and eacha[1]==eachb[1]:
                print(eacha)
                print(eachb)
                match=True
                break
            
        if not match:
            c.append(eachb)

    return c

def subtract_matrix(a,b):
    c=[]
    for eacha in a:
        match=False
        
        for eachb in b:

            if eacha[0]==eachb[0] and eacha[1]==eachb[1]:
                match=True
                c.append((eacha[0],eacha[1],(eacha[2]-eachb[2])))                
                break
            
        if not match:
            c.append(eacha)
            
    return c

def multiply_matrix(a,b):
    c=[]
    for eacha in a:
        match=False
        
        for eachb in b:

            if eacha[0]==eachb[0] and eacha[1]==eachb[1]:
                match=True
                c.append((eacha[0],eacha[1],(eacha[2]*eachb[2])))                
                break
            
        if not match:
            c.append(eacha)
            
    return c
    
    
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
            q1()
        elif choice==2:
            q2()
        elif choice==9:
            break
        else:
            print("Not a valid input")


if __name__=="__main__":
    main()
