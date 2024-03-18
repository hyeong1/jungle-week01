a,b = input().split()
c = int(input())
width = [int(a)]
height = [int(b)]
for i in range(c):
    check,number = input().split()
    
    if check == '0':
        height.append(int(number))
    else:
        width.append(int(number))

width.sort()
height.sort()
for i in range(len(width)-1,0,-1):
    width[i] = width[i] - width[i-1]
for i in range(len(height)-1,0,-1):
    height[i] = height[i] - height[i-1]

width.sort()
height.sort()

print(int(width[len(width)-1])*int(height[len(height)-1]))