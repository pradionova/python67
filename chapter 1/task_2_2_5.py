s = input()
slower = s.lower()
count = 0
len0 = len(s)
for i in range(0, len0):
    if slower[i] == 'g':
        count += 1
    elif slower[i] == 'c':
        count += 1
    else:
        continue
print(count / len0 * 100)