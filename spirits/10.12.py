


# def sayhi(name , surname , age, **kwargs):
#     print("hello dear" , name , 'with surname' , surname)
#     print(age)
#     print(kwargs)


# arr  = ["Eddie" , "Brock" , 30]

# sayhi(*arr)

# dct = {
#     "name": "Eddie" , 
#     "age" : 30, 
#     "surname" : "Brock" , 
# }

# sayhi("A" , "B" , "C" , muzaffar = "noob" , edgar = "best one")

# # sayhi( name="Eddie" , age=30 , surname="Brock" )

# def fun(a,b,c , d=0 , e="" , *args , **kwargs):
#     print(a)
#     print(c)
#     print(kwargs)


# fun(4,5,6,4,5,6, e='ewrwer' , illarion="dsfsdf" , chashka="blue" , chashka_inner="грязь", chashka="black")


# то_что_внутри_чашки = "кофе"
# print(то_что_внутри_чашки)



# def main(): 
#     def privet():
#         print("Hello VSEM")

#     def fun():
#         privet()
#     fun()

# main()


# def main():
#     print("sdfjsdf")
#     # name = "main_name" 
#     def fun():
#         # name = "fun_name"
#         print(name)
#     fun()





# OOP - Object Oriented Programming 




# name = 3242 
# name = "global_name"
# main()






# print("asdofhasodfnas")



# print(name)







# def main():
#     print("sdfjsdf")
#     name = "main_name" 
#     def fun():
#         global name
#         print(name)
#     fun()

# name = "dafsdfa"
# main()






# p,q = [int(x) for x in input().split() ]
# res = [] 
# for num in range(2 , q):
#     if(q  % num == 0):
#         if not((p % num == 0) or(num % p ==0)):
#             res.append(num)


# print(*res)


arr =[int(x) for x in input().split()]

negatives = [abs(x) for x in arr if x < 0]
average_negs = sum(negatives) / len(negatives)

elems = []
for item in arr:
    if(abs(item) > average_negs):
        elems.append(item)


print(sum(elems))












