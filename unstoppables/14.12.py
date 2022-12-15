def sort_array(source):
    evens = [] 
    for inx in range(len(source)):
        if(source[inx] % 2 == 0):
            value = source[inx]
            evens.append([inx , value])
    
    odds  = [x for x in source if x % 2]
    odds.sort()
    
    for inx , value in evens: 
        odds.insert(inx , value)
    
    return odds
    
# def find_uniq(arr):
#     items = set(arr)
#     if(arr.count(items[0])  == 1 ): return items[0]
#     if(arr.count(items[1])  == 1 ): return items[1]


# def purify(s):
#     print(s)
#     res = ""
#     infected = [0] * len(s)
#     for inx in range(len(s)):
#         if(s[inx].lower() == 'i'):
#             infected[inx] = 1 
#             if inx > 0: infected[inx - 1] = 1
#             if inx < (len(s) -1) : infected[inx + 1] = 1  
#     for inx in range(len(s)):
#         if(not infected[inx]):
#             res += s[inx]
#     arr =  [x for x in res.split(" ") if x]
#     return " ".join(arr )


# try: 
#     a = int(input())
# except ValueError:
#     print("a gha togri qiymat berilmadi ")
# except: 
#     print("Nomalum xaro")
# print("Uraaa bu kod ishlaydi")

# a = 5 
# b = 0 
# print(a / b)
# 20 / 1 = 20 
# 20 / 0.1 = 200
# 20 /  0.0001 = 200000
# 20 / 0.000000000001 = 2000000000000  



# try: 
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ValueError:
#     print("Xato qiymat berildi")
# except ZeroDivisionError:
#     print("0 ga bolish mumkin emas, B ga noldan farqli son berib koring")
# except KeyboardInterrupt:
#     print("Goodbye")
# except: 
#     print("Nomaslum xatolik yuz berdi")
# else:
#     print("hech qanaqa xato yuz bermadi")
# finally: 

#     print("Programma tugadi")
#     print(5/0)
#     print("UrAA LALALAL ")


# raise  SyntaxError("AHAHAHAH HAZILLASHDIM")

# try: 
#     try : 
#         pass 

import threading 
WSGI
def function(s):
    for _ in range(100):
        print(s , end="" , flush=True)

potok1 = threading.Thread(target=function , args=["+"])
potok2 = threading.Thread(target=function , args=['-'])
# function("+")
# function("-")

potok1.start()
potok2.start()

import keyboard
import numpy