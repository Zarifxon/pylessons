# arr = [int(x) for x in input().split()]


# price = int(input())

# summa = sum(arr)
# if(price > summa):
#     print(price - summa)
# else:
#     print(0)


# n = int(input())

# if(n % 2 ==0 ):
#     print("Second player")
# else:
#     print("First player")



# n = int(input())
# if(n < 38):
#     pass 
# elif(n % 5 > 2):
#     n += (5 - (n%5))
# print(n)


# import math
# a = int(input())
# b = int(input())
# print(math.ceil(a /b))
# print(math.floor(2.9)) 



# n = int(input())
# print(int( 0.5*n * (n+1)))

#include<bits/stdc++.h> 

# using namespace std ; 

# int main(){
#     int n ; 
#         cin >> n ; 
#         int res = n * (n-1) /2 ; 
#     cout << res ; 
# }

# arr = list(map(int , input().split())) 

# print(max(arr) - min(arr))




# arr = [x for x in range(1, 100)]  
# print(arr)

# arr= [] 

# for i in range(1,100):
#     arr.append(i **2)

# print(arr)


# arr = [x **2 for x in range(1, 100) if(x % 2 == 0)]

# # print(arr)
# arr = [int(x)**2 for x in input().split()]

# print(arr)

# n = int(input())
# res = ""
# if(n %2 == 0):
#     res = "JUFT"
# else:
#     res = "TOQ"

# print(res)

# n = int(input())

 
# print("JUFT" if n % 2 == 0 else "TOQ")


# arr = []

# for i in range(1, 100):
#     if(i %2 == 0):
#         arr.append(i ** 2)
#     else:
#         arr.append(i)


# arr = [i**2 if i % 2 ==0 else i for i in range(1, 100)]


# print(arr)


# a = input
# b = input
# a("gdsfgsd")

# print(a)
# print(b)
# a = input
# input = 5

# print(a)

# print(input)

# input = 5 

# def sayHi_three_times():
#     print("Salom")
#     print("Salom")
#     print("Salom")

# sayHi_three_times()

# def kvadrat(n):
#     print(n * 2)

# kvadrat(4)


# def sayHi(name):
#     print(f"Salom {name * 2}")



# sayHi("Muzaffar")
# sayHi(input())
# sayHi(53)


for n in range(1 ,100):
    if(n % 3 == 0 and n % 5 == 0):
        print("FizzBuzz")
    elif(n % 5 ==0):
        print("Buzz")
    elif(n %3 == 0):
        print("Fizz")
    else:
        print(n)

