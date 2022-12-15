# s1 = {1,2,3,4,5}
# s2 = {5,6,7,8,9,10}

# print(s1.isdisjoint(s2))
# s2.discard()
# s2.remove()

# n = int(input())

# res = ""
# if(n % 2 ==0):
#     res = "JUFT"
# else:
#     res = "TOQ"

# res = "JUFT" if n % 2 ==0 else "TOQ" 

# print("JUFT" if n % 2 == 0 else "TOQ")

# arr = [ (ifoda) (for_sikl) (if_qism) ]

# arr = [ (x ** 2 if x % 2 ==0 else x)  for x in range(1, 21) ]

# print(arr)


# print
# input
# len 
# min 
# max  

# if 
# for 
# while 

# s = "sdhjfgsd"
# s.lower()
# s.swapcase()

# a= input
# input = 5 
# print(input)
# print(a())
# a = int 

# def salom_ber():
#     print("Salom Quvonchbek")
#     print("Salom Tukin")
#     print("Salom Doston")

# print(salom_ber )
# A = salom_ber
# print(A)
# a = salom_ber

# def sayhi(name="foydalanuvchi"):
#     print(f"Salom {name}")


# sayhi(123123)
# sayhi() 


# kvadrat(5) # 25


# def kvadrat(n):
#     print(n ** 2)

# kvadrat(60)

# def sayhi(name , surname=None):
#     print(f"Salom {'' if surname == None else surname} {name}")


# sayhi("Muzaffar", "fsdfsf") 

# power(a,b)
# power()
# power(4, 5)

# power(5)



# def power(a,b=2):
#     print(a **b)

def factorial(n):
    res = 1 
    for x in range(1, n + 1):
        res *= x 
    print(res)


# factorial(5) # 120
# factorial(6) # 720 
# factorial((10))

# "Muzafffar"
# "aabbaaca"
# "Abbosali"
# "aBaABB"



def sortafter(s):
    for index in range(len(s) -2):
        if(s[index].lower() == 'a'):
            print(s[index + 1])


sortafter("aBaABB")

# Hello World


# def duplicate_count(s):
#     s = s.lower()
#     counter = 0 
#     base = set(list(s))
#     for char in base:
#         if s.count(char) > 1:
#             counter += 1 

#     return counter



def square_digits(num):
    return int("".join([str(int(x)**2) for x in list(str(num))]))

    
print(square_digits(356))

