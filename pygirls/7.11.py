# def square_digits(num):
#     return int("".join([int(x) ** 2 for x in str(num)]))

    
# def build_string(*arr):
#     res = ", ".join(arr)
#     return f"I like {res}!"

# def a(*arr):
#     print(arr)

# a(6,5,7,5,3,432,5435,34)


# def get_grade(*arr):
#     score = sum(arr) / 3 
#     if(90 <=score <=100):return "A"
#     elif(80 <=score < 90): return "B"
#     elif(70 <=score < 80): return "C"
#     elif(60 <=score < 70): return "D"
#     elif(0 <=score < 60): return "F"
#     else: return "KET YOQOL"


# def descending_order(num):
#     s = str(num)
#     arr = list(s)
#     arr.sort(reverse=True)
#     return int("".join(arr)) 


# print(descending_order(123456789))



# def greeting(**kwargs):
#     for name , surname in kwargs.items():
#         print("Salom" , name.capitalize() , surname.capitalize())



# greeting(nozima="toxtayeva" , eddie="brock")


# def fun():
#     a = 5 
#     def fun2():
#         b = 6 
#     fun2()
#     print(b)




# fun() 

# print(a)

# name = "Sevara"
# def fun():
#     global name
#     name = "ljodsglsdfkgjsd"


# fun()

# print(name)



name = "Sevara"

def fun():
    name = "Eddie"

    def fun2():
        global name
        name = "fjskdlfsdf"

    fun2()

    print(name)
fun()
print(name)




