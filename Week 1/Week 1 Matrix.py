import random

def generate_dict(size):
    dictionary={}
    for count in range(0,size):
        for count2 in range(0,size):
            if random.randint(0,25)==5:
                dictionary[(count,count2)]=random.randint(0,100)
    if len(dictionary)>(size*size)/2:
        generate_dict(size)
    return dictionary

def gen_match(a,b):
    addlist=[]
    for each in a:
        if each in b:
            addlist.append(each)
    return addlist

def matrix_add(a,b,add):
    c={}
    addlist=gen_match(a,b)
    for each in a:
        if each in addlist:
            if add:
                c[each]=a[each]+b[each]
            else:
                c[each]=a[each]-b[each]
        else:
            c[each]=a[each]
            
    for each in b:
        if each not in addlist:
            c[each]=b[each]
    return c

def matrix_multiply(a,b):
    pass



a=generate_dict(100)
b=generate_dict(100)
add=True
c=matrix_add(a,b,True)
print(c)


