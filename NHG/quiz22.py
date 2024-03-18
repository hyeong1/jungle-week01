import math


def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
a = int(input())
for _ in range(a):
    num = int(input())
    div = num//2
    div2 = num//2
    for _ in range(num//2):
        if is_prime(div) and is_prime(div2):
            print(div,div2)
            break
        else:
            div -= 1
            div2 += 1
