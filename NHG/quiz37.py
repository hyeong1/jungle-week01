from itertools import permutations
import sys

count = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
lit = []
answer  = 0
max = 0
last = 0
for i in permutations(cards,count):
    lit.append(i)

for i in range (len(lit)):
    for j in range (2,len(lit[i])):
        answer += abs(lit[i][j-2] - lit[i][j-1])
        last = abs(lit[i][j-1]-lit[i][j])
    if answer+last > max:
        
        max = answer + last
        answer = 0
    else:
        answer = 0

print(max)
        