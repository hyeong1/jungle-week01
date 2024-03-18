import itertools
count = int(input())
choose = int(input())
number_list = []
for i in range(count):
    number_list.append(input())
    
temp = []
nPr = itertools.permutations(number_list,choose)
for i in nPr:
    temp.append("".join(i))

result = []
for i in temp:
    if i not in result:
        result.append(i)

print(len(result))