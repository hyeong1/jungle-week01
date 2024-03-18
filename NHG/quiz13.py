a = input()
a = int(a)
average = []
middle = 0
hap = 0
population = 0
for i in range(a):
    b = list(map(int, input().split()))
    for j in range(1,b[0]+1):
        hap+=b[j]
    middle += hap/b[0]
    
    for j in range(1,b[0]+1):
        if b[j] > middle:
            population += 1
    c = 100/b[0]
  
    average.append(round(c*population,3))
    population = 0
    hap = 0
    middle = 0

for i in range(len(average)):
    print(average[i], end='%\n')
