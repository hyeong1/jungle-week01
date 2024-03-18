import sys

a = int(input())
lit = []

for i in range(a):
    num = int(sys.stdin.readline())
    lit.append(num)

lit.sort()

for num in lit:
    print(num)