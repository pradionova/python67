a = int(input())
list0 = []
sum0 = ''
space = ''

for i in range(1, a + 1):
    for j in range(0, i):
        list0.append(i)
        if len(list0) == a:
            break
    if len(list0) == a:
        break    
for y in list0:
    sum0 += str(y)
    space += str(y)
    space += ' '
print(space)