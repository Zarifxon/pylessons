# arr = [1,2,3,4]

# print(arr[100])

# v = int(input())

# import threading 

# threading.Thread

# a = 5 
# b = 0 
# print(a / b)
# 20 / 1 = 20 
# 20 / 0.1 = 200 
# 20 / 0.001 = 20000 
# 20 / 0.0000000000000000000000000000000000001 = 200000000000000000000000


# try: 
#     print("asdofasdf")
#     print(5/ 0)
#     print('sdfsjdfsdfs')
# except:
#     print("Qanaqadir xatolik")

# class AhmoqonaXatolik(BaseException):
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)
#         print("AHAHAHAH ")
    

# # raise ZeroDivisionError()
# try: 
#     a = int(input())
#     b = int(input())
#     print(a / b)
#     if(a == 404):
#         raise SyntaxError
# except ValueError:
#     print("Son xato")
# except ZeroDivisionError:
#     print("Ahmoq, nolga bolma")
# except KeyboardInterrupt:
#     print("Xayr")
# except:
#     print("Qanaqadir xatolik")
# else: 
#     print("Hammasi joyida")
# finally:
#     print("Finally ishladi")

# F = 345345 
# print(f"{F:.2}")
# from math import exp , fabs, atan, cos,

# -2.23423423423424
# print(1.2 * 3 )
# IEEE 754
# 6.532243
# 010101010101.101
# 1.2 *10 * 3 
# 12 * 3 = 36 
# 36 / 10
# 3.6


# import math

# diff = abs(a-b)
# if(diff == 0):
#     print(0)
# else:
#     print(math.ceil( diff / 10))

from math import gcd

from functools import reduce 

def lcm(*args):
    denominators = list(args)
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

a,b,c = [int(x) for x in input().split()]

original = lcm(a,b,c)
doniyor = lcm( lcm(a,b) , c )

if(original > doniyor):
    print (">")
elif(original < doniyor):
    print("<")
else:
    print("=")
