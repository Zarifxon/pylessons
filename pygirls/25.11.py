# def salom_ber(name , age , hobby):
#     print("Salom " + name) 
#     print("AGE: " + str(age)) 
#     print("HOBBY: " + hobby)



# salom_ber("DSFS", 10 , "jdsofkas")


# # salom_ber("Mehrangiz")

# def kvadrat(son):
#     print(son ** 2)

# kvadrat(5)


# def power(a,b):
#     print(a ** b)

# power(5,2)
# power(5,3)


arr = [5,4,7,3,8,10]
# max(arr)


def eng_kattasi(lst):
    res = lst[0]
    for i in lst:
        if(i > res):
            res = i 
    print(res)




# def multiple(a,b):
#     print(a * b)

# print(multiple(4,5))

# a,b = map(int , input().split())
# a,b = [int(x) for x in input().split()]
# multiple(a,b) #21

# print( multiple(a,b) )



# print( kupaytma(4,5) )

# print(c)

# a = print
# a("sdfsdf")
# a = kupaytma
# print(a)



# b = kupaytma
# print(b)
def kupaytma(a,b):
    return a * b
    print("FUnksiya tugadi")

    
def pow(a,b):
    res = 1
    for _ in range(b):
        res *= a 
    return res 

# int pow(int a , int b){
#     int res = 1 ; 
#     for(int i = 0 ; i < b ; i++) res *= a ; 
#     return res 
# }


def factorial(n):
    res = 1 
    for i in range(1 , n + 1):
        res *= i 
    return res 


def sayHi(surname, name = "Foydalanuvchi"):
    print(f'Salom qadrli {name} with surname {surname}')

# sayHi("dsjhfsdf" , "IWER")


# pow(5) 


def pow(a,b=2):
    return a ** b

print(pow(4))

