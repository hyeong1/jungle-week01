import sys



def stack_test(start,now,value,cnt):
   
    global min
    # 종료조건 : 카운트가 cnt랑 같아졌을경우 모든 곳을 다 돌아본것
    if cnt == count:
        #print('---------')
        if a[now][start]:
         #   print('--------',a[now][start])
            value += a[now][start]
            if min > value:
               min = value
        return
    
    if value > min:
        return
    
    for i in range(count):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            stack_test(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0


count = int(sys.stdin.readline())
visited = [0]*count

min = sys.maxsize
a = [list(map(int, input().split()))for _ in range(count)]

for i in range(count):
    visited[i] = 1
    stack_test(i,i,0,1)
    visited[i] =0
print(min)


    