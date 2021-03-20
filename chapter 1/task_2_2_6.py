s =  input()
len0 = len(s)
count = 0
letter = ''
anything = ''
for i in range(0, len0):
    if letter == s[i]:
        count += 1
    else:
        if count != 0:
            anything += letter
            anything += str(count)
        letter = s[i]
        count = 1

anything += letter + str(count)
print(anything)