n, dy, dx = list(map(int, input().split()))
answer = 0
while n>0:
    n-=1
    #print(n)
    if dx < (2**n) and dy < (2**n):
        #print('1사분면 : ',answer) 
        answer += ((2**n)*(2**n)* 0)
    elif dx >= (2**n) and dy < (2**n):
        #print('2사분면 : ',answer) 
        answer += ((2**n)*(2**n)* 1)
    elif dx < (2**n) and dy >= (2**n):
        #print('3사분면 : ',answer)
        answer += ((2**n)*(2**n)* 2)
    else:
        #print('4사분면 : ',answer)
        answer += ((2**n)*(2**n)* 3)
    
    if dx >= 2**n:
        dx -= (2**n)
    if dy >= 2**n:
        dy -= (2**n)

print(answer)


# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)

# list_b = [0]*((a**2)*(a**2))
# check = 0
# if(a == 2): check = 2

# before_num =[0]
# current_position = [0]
# value = ((2**a)*(2**a))
# time = int(value%((2**(a-1))* (2**(a-1) )))
# print(time, value)
# if(time > 0):
#     time *=7
# else:
#     time = 7

# def put(num):
#     if(num<time):
#         if(before_num[0]==value):
#             print("================================================",before_num[0]-check)
            
#         if num == 0 or before_num[0] % 16 == 0:
#             if before_num[0] % 16 == 0:
#                 current_position[0] = 0
#             for i in range(2):
#                 list_b[i] = before_num[0]
#                 current_position[0] += 1
#                 before_num[0] += 1
#             #    print(list_b)
#                 if(before_num[0]==value):
#                     print("================================================",before_num[0]-check)
#                 continue
        
            

#         if before_num[0] % 8 == 0:
#             print('##########')
#             current_position[0] += ((2**a) - 4)
#             print(current_position[0])
#             for i in range(2):
#                 list_b[current_position[0]] = before_num[0]
#                 current_position[0] += 1    
#                 before_num[0] += 1
#                 #print(list_b)
#                 if(before_num[0]==value):
#                     print("================================================",before_num[0]-check)
#                 continue
#         elif before_num[0] % 4 == 0:
#             print('&&&&&&')
            
#             current_position[0] -= 2**a
#             print(current_position[0],current_position[0])
#             for i in range(2):
#                 list_b[current_position[0]] = before_num[0]
#                 current_position[0] += 1    
#                 before_num[0] += 1
#                 #print(list_b)
#                 if(before_num[0]==value):
#                     print("================================================",before_num[0]-check)
#                 continue
#         elif before_num[0] % 2 == 0:
#             print('-----',current_position[0])
#             current_position[0] += (a*(a-1))
#             for i in range(2):
#                 list_b[current_position[0]] = before_num[0]
#                 current_position[0] += 1   
#                 before_num[0] += 1
#                 #print(list_b)
#                 if(before_num[0]==value):
#                     print("================================================",before_num[0]-check)
#                 continue

#         put(num+1)


# if a == 1: 
#     print(0)
# else:
#     put(0)
