a = input()
a = int(a)
lit = []
for i in range(a):
    b = int(input())
    lit.append(int(b))
lit.sort()
for i in range(a):
    print(lit[i])