import sys
b = int(input())
num = []
for i in range(b):
    num.append(sys.stdin.readline().rstrip())

num = list(set(num))

num.sort()
num.sort(key=lambda x: len(x))
for i in range(len(num)):
    print(num[i])
