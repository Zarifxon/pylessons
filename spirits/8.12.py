# def is_defended(at ,df):
#     # at.sort(reversed = True )
#     # df.sort(reversed = True)
#     at_alive = len(at)
#     df_alive = len(df)
#     fights = min(at_alive , df_alive)

#     for arena in range(fights):
#         if(at[arena] > df[arena]):
#             df_alive -= 1 
#         elif (at[arena] < df[arena]):
#             at_alive -= 1 
#         else:
#             at_alive -= 1 
#             df_alive -= 1 
    
#     if(at_alive != df_alive):
#         if(at_alive > df_alive):
#             return False
#         else:
#             return True
#     # elif(at_alive == 0):
#     #     return True
#     else:
#         df_hp = sum(df)
#         at_hp = sum(at)

#         if(at_hp > df_hp):
#             return False 
#         else:
#             return True



# def power(a,b=2):
#     if(b == None):
#         b = 2 

#     return a ** b 

# def haha(name , age , arr,  surname="Spooner" ,  ):
#     print(name)
#     print(surname)
#     print(arr)



# # haha(4,5,6,7,8)
# # haha(name='sadfasdf' , surname="sdjfskdf" , age="fada" , arr = [4,5,6,])

# class COLORS:
#     green = "#00ff00"
#     red = "#ff0000"
#     blue = "#0000ff"
#     yellow = "#ffff00"



# light = "#ff0000"
# light2 = COLORS.blue

# class LOCALIZATION:
#     say_goodbye = open("ru_RU.txt")

# # lst = ["Muzaffar" , 21 , [5,6,7], "Mirzaev"]

# # haha(lst[0] , lst[1] , lst[2] , lst[3])
# # haha(*lst)

# def fun(a, b, *trash):
#     print(a,b)
#     print(trash)

# arr = [4,5, 6,7,8,]
# fun(4,5,6,7,8)



# n = int(input())
# print(f"The next number for the number {n} is {n+1}.\nThe previous number for the number {n} is {n-1}.")
import threading

def justprint(s):
    for x in range(100):
        print(s, end="", flush=True)
        a = 378453478573485 ** 23
    print(f"\nfunction {s} completed \n")
    
# justprint('+')
# justprint("-")

worker1 = threading.Thread(target=justprint , args=["+"])
worker2 = threading.Thread(target=justprint , args=["-"])

worker1.start()
worker2.start()
