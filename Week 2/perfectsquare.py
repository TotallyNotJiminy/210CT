def perfectsquare(i):
    if i<=1:
        return i
    else:
        if i**0.5==int(i**0.5):
            return i
        else:
            i=perfectsquare(i-1)
            return i
        
def main():
    while 1:
        try:
            number=int(input("Please enter the number you'd like to check: "))
            break
        except ValueError:
            print("That's not a number!")
    q=perfectsquare(number)
    print(q)

if __name__=="__main__":
    main()
