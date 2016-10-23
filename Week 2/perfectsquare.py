def perfectsquare(i):
    if i==0 or i==1:
        return i
    else:
        if i**0.5==int(i**0.5):
            return i
        else:
            i=perfectsquare(i-1)
            return i
             
q=perfectsquare(1874092837089560834756087174563745674657868347)
print(q)
