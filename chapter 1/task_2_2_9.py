a = input()
list0 = a.split()
list0.sort()
len0 = len(list0)
letter = ''
result = ''
some = ''
colvo = 0
for i in range(0, len0):
    if letter == list0[i]:
        colvo += 1
        if colvo == 2:
            result += letter + ' '
    else:
        letter = list0[i]
        colvo = 1
print(result)