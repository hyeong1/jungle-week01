max = 0
value = 0
for i in range(9):
    a = input()
    a = int(a)
    if(a>max):
        max = a
        value = i+1

print(max, value)