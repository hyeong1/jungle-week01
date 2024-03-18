a = input()
a = int(a)
point = 0
bonus = 0
all_point = []
for i in range(a):
    b = input()
    for j in range(len(b)):
        if(b[j] != 'X'):
            bonus += 1
            point += bonus
        else:
            bonus = 0
    all_point.append(point)
    point = 0
    bonus = 0

for i in range(len(all_point)):
    print(all_point[i])
