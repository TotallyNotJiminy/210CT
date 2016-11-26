"""
This function removes vowels from a string, recursively, by rewriting the
string without the vowel it comes across, then moves on, with the pointer
indicating where it is currently working on in the string
"""
def RemoveVowels(String,Pointer):
    if Pointer>len(String)-1:
        return String
    elif String[Pointer].lower() in ["a","e","i","o","u"]:
        String=String[:Pointer]+String[Pointer+1:]
        
    else:
        Pointer+=1
    String=RemoveVowels(String,Pointer)
    return String

def main():
    istring=input("Please enter text with vowels in: ")
    print()
    print(p4(istring,0))

if __name__=="__main__":
    main()
