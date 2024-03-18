a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
width = 0
height = 0
if c-a > a:
    width = a
else:
    width = c-a

if d-b > b:
    height = b
else:
    height = d-b

if width > height:
    print(height)
else:
    print(width)