a = input()

b = int(a)
hansu = 0
if b <100:
    hansu = b 
else:
    hansu = 99
    for i in range(100,b+1):
        temp = int(str(i)[0]) - int(str(i)[1])
        temp2 = int(str(i)[1]) - int(str(i)[2])
        if temp == temp2:
            hansu += 1
            
print(hansu)