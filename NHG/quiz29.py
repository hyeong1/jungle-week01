size = int(input())
pos = [0]*size
flag = [False]*size
flag_a = [False]*(size*2-1)
flag_b = [False]*(size*2-1)
 
flag_count = [0]

def put():
    
    # for i in range(size):
    #     print(pos[i], end=" - ")
    #print()
    flag_count[0] += 1

    #print()

def set(i):
    for j in range(size):
        if (not flag[j] and not flag_a[i+j] and not flag_b[i-j+size-1]):
            pos[i] = j
            if i==size-1:
                put()
            else:
                flag[j] = flag_a[j+i] = flag_b[i-j+size-1] = True
                set(i+1)
                flag[j] = flag_a[j+i] = flag_b[i-j+size-1] = False

set(0)
print(flag_count[0])