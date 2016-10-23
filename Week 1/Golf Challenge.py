def b(n):
    if n==0:return[[]]
    s =[]
    d = b(n-1)
    for e in d:
        for f in range(1,9):
            if not k(e,f): 
                s.append(e+[(n,f)])
    return s
def k(g,f):
    i=len(g)+1
    for h in g: 
        r,c=h
        if r==i or(f-c)==-(i-r)or c==f or(f-c)==(i-r): return 1
    return 0
for z in b(8):
    print(z)
