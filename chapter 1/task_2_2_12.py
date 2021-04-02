lst = input()
x = input()
result = ''
splitLst = lst.split()
lenLst = len(splitLst)
for i in range(lenLst):
    indexSplit = splitLst[i]
    if indexSplit == x:
        result += str(i)
        result += ' '
if result == '':
    result = 'Отсутствует'
print(result)