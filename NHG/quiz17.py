a = int(input())
empty_b = []
for i in range(a):
    num, letter = input().split()
    temp = ''
    for j in range(len(letter)):
        temp = temp+ letter[j]*int(num)
    empty_b.append(temp)

for i in range(a):
    print(empty_b[i])
    
