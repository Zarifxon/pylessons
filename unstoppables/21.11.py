# z = abs(int(input()))
# res = 0 
# if(z == 0):
#     print(-1)
# else:
#     for i in range(1 , z + 1):
#         for j in range(1 , z +1):
#             if(i * j == z):
#                 res += 1 
                
#     print(res * 2)


# a,b,c = map(int , input().split())

# if( a > b):print(">")
# elif(a < b):print("<")
# else:print("=")


# price = int(input())
# a,b,c = map(int , input().split())

# if(a+b+c >=price):
#     print("Yes")
# else:
#     print("No")

# arr = list(map(int  , input().split()))
# arr.sort() 

# summa = sum(arr)
# kattasi = arr[-1]
# kichigi = arr[0]
# print(summa  - kattasi , summa - kichigi)


# n = int(input())


# if(n > 3):
#     res = 0.5 * n * (n-3)
# else:
#     res = 0 
# print(int(res))


# arr = [4,5,6,7,3,4,5,6]

# print(arr)
# arr.append(3453)
# s = {4,5,6,7,8,4,5,6}

# s.add(66)
# fromarr = set(arr)
# print(fromarr)

# database = {"kwutge" , "hurricane" , "arcane" , "boomer" , "tulkin"}

# user_nick = input()

# if(user_nick in database):
#     print("Already taken")
# else:
#     database.add(user_nick)
#     print("Successfully added")

gap = input().split()
words = set(gap)

l_word = list(words)

def sort_key(ob):
    return gap.count(ob)

l_word.sort(key=sort_key , reverse=True)


print(*l_word  , sep="\n")

