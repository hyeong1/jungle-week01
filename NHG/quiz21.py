a = int(input())
b = list(map(int, input().split()))
count = 0
nocount = 0

for i in range(a):
    nocount = 0
    for j in range(2,b[i]):
        if(b[i]%j == 0):
            nocount += 1
            break
    if b[i] != 1 and nocount == 0:
        count += 1 
print(count)
        
