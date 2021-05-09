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
            if count > 1:
                anything += str(count)
            anything += letter
        letter = s[i]
        count = 1
if count > 1:
    anything += str(count)
anything += letter
print(anything)