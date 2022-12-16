# m , n = [int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]

# arr.sort()
# summa= 0 
# count = 0 
# is_empty = False
# while(summa < m):
#     if(not arr):
#         is_empty = True
#         break
#     summa += arr.pop()
#     count += 1 
# if is_empty:
#     print(-1)
# else:
#     print(count)



# from math import ceil
# tables = 0 
# a , b ,c = [int(x) for x in input().split() ]
# tables += ceil(a / 2) 
# tables += ceil(b / 2) 
# tables += ceil(c / 2) 
# print(tables)

# from math import ceil
# print(sum([ceil(int(x)/2) for x in input().split()]))

n = int(input())
print(int(n * (n+1) * 0.5) + 1)
