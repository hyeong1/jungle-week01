a ,b = input().split()

reverse_a = int("".join(reversed(a)))
reversed_b = int("".join(reversed(b)))

if reverse_a > reversed_b:
    print(reverse_a)
else:
    print(reversed_b)