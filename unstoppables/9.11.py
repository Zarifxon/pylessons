# month = int(input())
# if (a==12 )or (a==1) or (a==2) :
#     print("Winter")
# elif a==3 or a==4 or a==5 :
#     print("Spring")
# elif a==6 or a==7 or a==8 :
#     print("Summer")
# elif a>12 or a<0 :
#     print("Error")
# else:
#     print("Autumn")\

# if( month in [1,2,12]):
#     print("Winter")
# elif(month in [3,4,5]):
#     print("Spring")
# elif(month in [6,7,8]):
#     print("Summer")
# elif(month in [9,10,11]):
#     print("Autumn")
# else:
#     print("Error")

# s = input()
# print(len(s))

# for char in s:
#     print(bin(ord(char))[2:])

# print(bin(ord("h"))[2:]) 


def filter_list(arr):
    return [x for x in arr if isinstance(x, int)]

def build_string(*arr):
    return f"I like {', '.join(arr)}!"

def is_isogram(string):
    return True if len(string) ==  len(set(string.lower())) else False 

def high_and_low(string):
    arr =[ int(x) for x in string.split()]
    return f"{max(arr)} {min(arr)}"


def get_count(sen):
    return len([1 for letter in sen if letter in "aeiou"])

def sum_two_smallest_numbers(arr):return sum(sorted(arr)[:2])

# theta3*x^3+theta2*x^2 + theta1*9x + theta0    


