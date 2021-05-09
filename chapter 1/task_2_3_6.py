a = input()
saveCount = ''
saveLetter = ''
len0 = len(a)
piece = ''
result = ''

def process(letter, count):
    newCount = int(count)
    piece = newCount * letter
    #print(piece)
    return piece

for i in a:
    if i.isalpha() == True:
        if saveLetter != '' and saveCount != '':
            result += process(saveLetter, saveCount)
            saveCount = ''
        saveLetter = i  
    if i.isnumeric() == True:
        saveCount += i

result += process(saveLetter, saveCount)
print(result)