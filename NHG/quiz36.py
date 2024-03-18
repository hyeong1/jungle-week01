# from itertools import combinations
import sys
# count, hap = list(map(int, sys.stdin.readline().split()))
# value = 0
# cards = list(map(int, sys.stdin.readline().split()))

# min = 300000
# for j in combinations(cards,3):
#         if sum(j) <= hap and hap - sum(j) < min:
#             min = hap - sum(j)
#             value = sum(j)
# print(value)

count, hap = list(map(int, sys.stdin.readline().split()))
check_lit = [False] * count
cards = list(map(int, sys.stdin.readline().split()))
min = sys.maxsize
answer = 0
answer_lit =[]
def dfs(value,cnt,num):
    global min
    global answer
    if cnt == 3:
        check_lit[num] = True
        if hap -value <min and hap -value >=0:
            min = hap - value
            answer = value
            
        return
    
    if cnt >=3:
        return

    for i in range(count):
        if not check_lit[i]:
            check_lit[i] = True
            answer_lit.append(cards[i])
            dfs(value+cards[i],cnt+1,i)
            check_lit[i] = False
            answer_lit.pop()

dfs(0,0, 0)
print(answer)
