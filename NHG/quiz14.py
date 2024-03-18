a = input()
b = input()
c = input()

a = int(a)
b = int(b)
c = int(c)
d = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']
num = []
gop = a*b*c
gop = str(gop)
count = 0
for i in range(10):
    for j in range(len(gop)):

        if gop[j] == d[i]:
            count += 1
    num.append(count)
    count = 0

for i in range(10):
    print(num[i])