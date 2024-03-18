import sys
count = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().strip().split()))

plus, minus, mul, div = map(int, input().split())
lit = [plus,minus,mul,div]
answer_lit = []

value = 0
min = 1e10
max = -1e10

ord = count -1

def dfs(start):
    global min
    global max
    global ord
    global value
    global count
    if start == count:
        
        if sum(lit) == 0:
            value = number[0]
            for i in range(0,len(answer_lit)):
                if i>= count-1:
                #    print('Rmx')
                    continue
                
                if answer_lit[i] == 0:
                    #print('1번 ', value,number[i+1])
                    value = value+number[i+1]
                elif answer_lit[i] == 1:
                    #print('2번 ', value,number[i+1])
                    value = value-number[i+1]
                elif answer_lit[i] == 2:
                    #print('3번 ', value,number[i+1])
                    value = value*number[i+1]
                else:
                    #print('4번 ', value,number[i+1])
                    value = value/number[i+1]
                if i == len(answer_lit)-1:

                    if value > max:
                        max = value
                    if value < min:
                        min = value
                #print(answer_lit, value, min, max)
            return
    if sum(lit) == 0:
        value = number[0]
        for i in range(0,len(answer_lit)):
            if i>= count-1:
            #    print('Rmx')
                continue
            
            if answer_lit[i] == 0:
                #print('1번 ', value,number[i+1])
                value = value+number[i+1]
            elif answer_lit[i] == 1:
                #print('2번 ', value,number[i+1])
                value = value-number[i+1]
            elif answer_lit[i] == 2:
                
                #print('3번 ', value,number[i+1])
                value = value*number[i+1]
            else:
                # if value ==-1 and number[i+1] == 3:
                #     print("----",answer_lit, value, min, max, int(value/number[i+1]))
                #print('4번 ', value,number[i+1],value/number[i+1],int(value//number[i+1]))
                value = int(value/number[i+1])
            if i == len(answer_lit)-1:
                if value > max:
                    max = value
                if value < min:
                    min = value
            
        return
    
    for i in range(4):
        if lit[i]:
            answer_lit.append(i)
            lit[i] -= 1
            dfs(start+1,0)
            lit[i] += 1
            answer_lit.pop()


dfs(0,0)
print(max)
print(min)


    


    
