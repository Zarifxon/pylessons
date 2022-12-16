def pal(obj):
    if(type(obj) in [str , list]):
        return obj == obj[::-1]
    elif(type(obj) == int): 
        return str(obj) == str(obj)[::-1]
    else:
        raise ValueError("Bu xato tur")

try:
    print(pal("aas"))
    print(pal("aaa"))
    print(pal([1,2,3]))
    print(pal(input))
    print(pal([3,2,3]))
    print(pal(456))
    print(pal(545))
except:
    print("Xato")