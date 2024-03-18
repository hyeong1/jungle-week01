# from itertools import combinations
# lit = []
# for i in range(9):
#     lit.append(int(input()))
    
# lit.sort()
# result_lit = []
# for j in combinations(lit,7):
#         if sum(j) == 100:
#             result_lit.append(j)
#             break
# for i in range(len(result_lit[0])):
#     print(result_lit[0][i])

hap = 0
lit = []
check = [False] * 9
for i in range(9):
    lit.append(int(input()))
lit.sort()
check_lit = []
answer_lit=[]
def find_person(value,cnt,num):
    if cnt == 7:
        check[num] = True
        
        if sum(check_lit) == 100:
            for i in range(len(check_lit)):
                print(check_lit[i])
            answer_lit.append(str(check_lit))
        return
    
    if answer_lit:
        return
    
    for i in range(9):
        if not check[i]:
            check[i] = True
            check_lit.append(lit[i])
            find_person(value+lit[i],cnt+1,i)
            check[i] = False
            check_lit.pop()

find_person(0,0,0)