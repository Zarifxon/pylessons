# def sayhi(name , surname , age):
    # print(f"hello dear {name} {surname} with age {age}")


# sayhi(age=36 , surname = "Brock" , name="Eddie")
# sayhi("Eddie" , age=36, surname="Brock")


# def sayhi(*arr):
#     for name in arr:
#         print(f"Hello {name}")

# sayhi("Eddie")
# # sayhi("Toby", "Cobey")
# sayhi("Sevara" , "Nasiba" , "Nozima")


# def abc(name , surname , *arr):
#     print(f"name {name}")
#     print(f"surname {surname}")

#     print(arr)

# abc("yoo" , "foo", 3,4,5, 6,34,33,45,345,45)


# print("fsdf",  'sdfsdf' , "sdfsdf")

# def yigindi(*arr):
#     res = 0
#     for i in arr:
#        res += i 

#     return res  

# print(yigindi(5,4,6,4,32,2))


# \
# res = 34850
# 239 2394 2 23 234 986 34850


def kattasi(*arr):
    res = arr[0]

    for i in arr:
        if(i > res):
            res = i
    return res 


# a = kattasi(5,23,324,234,26,23 , 500 , 400 , 600 , 550,)

# print(a)

def sayhi(name , surname , age):
    print(f"hello dear {name} {surname} with age {age}")


# a = ["Eddie" , "Brock" , 36]

# sayhi(*a)

# arr = [6,5,4,7,8,2,3,4,9,0]
# print(kattasi(*arr))

# def abc( *args , **kwargs):
#     print(args)
#     print(kwargs)


# abc(3,4,5,2,23,4,2 , name="Muuzaffar" , surname="Mirzaev")


# d = {
#     "surname" : "Brock",  
#     "age"   : 36, 
#     "name" : "Eddie",
# }

# sayhi(**d)
# sayhi(surname="Brock" , age=36 , name="Eddie")

# sayhi(sevara="ergasheva" , nozima="toxtayeva" , eddie="brock")

# salom Sevara Ergasheva 
# salom Nozima Toxtayeva
# salom Eddie Brock




# try:
#     arr = [1,2,3]

#     a = arr[4040]
# except IndexError:
#     print("Index ERROR")
# except SyntaxError

def number_to_string(n):
    return str(n)

print(repr(number_to_string(-100)))


