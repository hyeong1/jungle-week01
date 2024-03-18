
def move(no,a,b,c):
    if(no == 1):
        print(a,c)
    else:
        move(no-1,a,c,b)
        move(1,a,b,c)
        move(no-1,b,a,c)
a = int(input())
print(2**a-1)
if(a <= 20):
    move(a,1,2,3)