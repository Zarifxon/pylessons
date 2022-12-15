# d = {
#     "age" : 21 , 
#     "surname" : "Mirzaev" , 
#     "name" : "Muzaffar" , 
# }

# arr = [1,2,3]
# def func(name , surname ,age ,*args, **kwargs):

#     print("name",name)
#     print("Surname", surname)
#     print("age",age)
#     print("Args",args)
#     print("KW Args" , kwargs)

# func(d["name"] , d["surname"] , d["age"])
# func(*arr)
# func(*d.values())
# func(**d)

# func(name="Muzaffar" ,age=21 , surname="Mirzaev" )
# func(name="Faloncha" ,age = 100, surname = "Palonchaev" ,boyi=150 , laqabi="Jinni" )
# func("Muzaffar" , "Mirzaev" , 21, "python", 'music' , width=174 , laqab="aaaa" )

# def main():
#     ism = "mainnni ismi"
#     print(ism)

# ism = "hahah"
# main()


# val =  "GLOBAL"

# def main():
#     val = "Main"
#     print("Mainni ichida", val)
#     def func():
#         global val
#         val2 = val 
#         val2 = "234234"
#         # val = "Val"
#         print("Funcni ichida" , val)
#     func()


# main()
# print(val)



# oqim_boylab_tezlik = s/t
# x + (x-v) = by_stream

# 2x - v = by_stream
# x = (by_stream - v) / 2 

# qayiq = (oqim_boylab_tezlik - v ) /2 
# oqim = qayiq - v
# res = qayiq - oqim
# if(int(res) == res):
#     print(int(res))
# else:
#     print(res)

    # qayiq + oqim = s/t
    # oqim = qayiq - v 
    # qayiq + qayiq - v = s/t
# t,s,v = [float(x) for x in input().split()]
# qayiq = (s/t - v ) /2 
# oqim = qayiq - v 
# natija = qayiq - oqim

# if(int(natija) == natija):
#     print(int(natija))
# else:
#     print(natija)

# n = int(input())
# if(n in [1]):
#     print("murakkab")
# else:
#     print("tub")


# boshlar,panjalar = [int(x) for x in input().split()]

# if(panjalar % 2 ==1 ):
#     print(-1)
# else:
#     print(boshlar + panjalar//2 + 1 )


# def solve(ax , ay , bx , by):
#     if(ax > bx):
#         ax = bx - abs(bx - ax)
#     elif(ax < bx ):
#         ax = bx + abs(bx -ax) 

#     if(ay > by):
#         ay = by - abs(by - ay) 
#     elif(ay < by ):
#         ay = by + abs(ay - by)

#     return [ax, ay]

# n = int(input())

# for _ in range(n):
#     print(*solve( *[int(x) for x in input().split()] ))

    


