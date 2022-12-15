# arr = [6,-5 , 23, -1, -202]

# arr2 = [abs(x) for x in arr]

# arr3 = list(map(abs, arr))

# print(arr2)
# print(arr3)

# narx = int(input())

# a,b,c  = [int(x) for x in input().split()]

# if(a + b + c >= narx):
#     print("Yes")
# else:
#     print("No")


# x = int(input())

# res = x ** 5 + 8*x**4- 5*x**3 + 3 * x ** 2 + x - 12 

# print(res)

# import datetime 


# def find_even_index(arr):
#     for inx in range(len(arr)):
#         right = sum(arr[ : inx] )
#         left = sum(arr[inx + 1 : ])
#         if(right == left):
#             return inx
#     return -1 
# try:
#     a = datetime.date(2022, 2, 29)
# except ValueError:
#     print("ERROR") 

# print(a.weekday())


# def fact(n):
#     res = 1 
#     for num in range(1 , n + 1):
#         res *= num 

#     return res

# a = fact(5)
# print(a)




def sayHi(name , surname , age):
    if(age >= 18):
        print(f"Salom qadrli {name} {surname}")
    else:
        print("#KETYOQOL")

# sayHi("Tulkin" , "Bahodirov" , 16)
sayHi(age = 19 , surname = "Bahodirov" , name = "Tulkin")


# def eng_kattasi(*arr): 
#     return sorted(list(arr))[-1]




# print(eng_kattasi(4,5,6,6,4,23,32234,234,2342,34,2))



def sayHi(name, surname='sdfsdf' , *arr ): 
    print(name)
    print(surname )
    print(arr)

def sayhi(*arr):
    name = arr[:3]
    
sayHi(1,2,3,4,5)




