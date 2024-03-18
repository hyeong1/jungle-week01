

number, count = map(int, input().split())
visited = [False] * (number+1)
ans = []
def back(num):
    
    if len(ans) == count:
        visited[num-1] = True
        print(" ".join(map(str,ans)))
        return
    else:
        visited[num] = False
    for i in range(1, number):
        print(visited)
        
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            # print('------',ans, i)
            back(num+1)
            visited[i] = False
            ans.pop()
            

back(1)