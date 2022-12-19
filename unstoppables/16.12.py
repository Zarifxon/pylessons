# def pal(obj):
#     if(type(obj) in [str , list]):
#         return obj == obj[::-1]
#     elif(type(obj) == int): 
#         return str(obj) == str(obj)[::-1]
#     else:
#         raise ValueError("Bu xato tur")

# try:
#     print(pal("aas"))
#     print(pal("aaa"))
#     print(pal([1,2,3]))
#     print(pal(input))
#     print(pal([3,2,3]))
#     print(pal(456))
#     print(pal(545))
# except:
#     print("Xato")


    # def find_nb(m):
    #     n = 0
    #     summa = 0  
    #     while True:
    #         summa += n ** 3 
    #         if(summa == m):
    #             return n
    #         n += 1 
    #         if(summa > m):
    #             return -1
    
# def is_valid(positions):
#     positions = positions.upper()
#     bishop1_pos = positions.find("B")
#     bishop2_pos = positions.find("B" , bishop1_pos + 1)
#     if(bishop1_pos % 2 == bishop2_pos % 2):
#         return False 

#     rook1_pos = positions.find("R")
#     rook2_pos = positions.find("R", rook1_pos + 1)
#     king_pos = positions.find("K")
#     if(king_pos in [0,7]):
#         return False
#     if not (rook1_pos < king_pos < rook2_pos):
#         return False

#     return True
    
    
# def accum(pos):
#     base = dict()
#     for index in range(len(pos)):
#         letter = pos[index].lower()
#         base.setdefault(letter , index)
#     print(base)
#     res = []
#     for letter in pos.lower():
#         res.append( (letter * (base[letter] + 1 )).capitalize())

#     return "-".join(res)


# def accum(pos):
#     res = []  
#     for index in range(len(pos)):
#         res.append(  (pos[index].lower() *(index + 1)).capitalize())
#     return "-".join(res)
