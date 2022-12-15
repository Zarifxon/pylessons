# n = int(input())

# res = ""
# if(n % 2 == 0):
#     res = "PRIME"
# else:
#     res = "NOT PRIME"


# res = "PRIME" if n % 2==0 else "NOT PRIME"
# print("PRIME" if int(input()) % 2==0 else "NOT PRIME")


# arr = [(выражение) (цикл фор) (условие) ] 

# arr =  [x ** 2 for x in range(1, 10)]


# arr = [ x ** 2 for x in range(1, 21) if x % 2 == 0 ]

# arr = [(x** 2 if x % 2==0 else x) for x in range(1, 21)]

# print(arr)

# print 
# input 
# abs 
# min 
# max 
# sum 
# len
# range 



# это операторы
# if
# for 
# while 
# try 

# примеры ключевых слов
# import 
# in 
# 



# s = "asdjkfsaf"
# arr = []

# methods
# s.lower()
# arr.append(3424)


# a = 5 
# b = a 
# print(b)



# a = print

# a("jsfdfskf")


# a = input
# input = 5 

# print(input)

# a()

# def sayHi():
#     print("hello Jaxongir")
#     print("Hello Samir")
#     print("Hello Fariz")


# a = sayHi

# a()
# def sayhi(name="polzovatel"):
#     print("Privet dorogoy " + name)

# Priver Jaxongir
# sayhi(input("Type ur name: "))

# sayhi()

# def kvadrat(x):
#     print(x ** 2)

# def kvadrat(chislo):
#     print("Square of ur num: " + str(chislo ** 2 ))

# kvadrat(int(input("Type ur num : ")))

def greeting(name , age):
    if(age >=18):
        print(f"Welcome to PROHub dear {name}")
    else:
        print("U R 2 young, GET OFF")

# imya = input("What isur name: ")
# voz = int(input("How old r u : " ))

# greeting(imya , voz )



# power(a,b)
# power(5, 3) 

# def power(a=5,b=2):
#     print(a ** b)
    
# power(2, 10)
# power(5) # 25 
# power(7) # 49 
# power( b = 3)


# print("sdjfksd")
# print(2,23,4234,234,234,234,234,234)
# a = pow(4,5)
# print(a)


# def power(a,b):
#     res = a ** b 
#     return res
#     print("fuck off")

# a = power(5,6)

# print(a)


# def get_max(arr):
#     res = arr[0]

#     for item in arr:
#         if(item > res):
#             res = item

#     return res 



# arr = [-5 , -1 , -6, -101, -59]

# a = get_max(arr)
# print(a)



def high_and_low(numbers):
    arr = [int(x) for x in numbers.split()]

    return f"{max(arr)} {min(arr)}"


print("sdhfjisdfjsd")