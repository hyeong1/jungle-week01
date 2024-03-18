a = int(input())
b = set(map(str, input().split()))
c = int(input())
d = list(map(str, input().split()))
e = []
for i in range(c):
    if d[i] in b:
        print(1)
    else:
        print(0)