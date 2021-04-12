a = input()
alow = a.lower()
lisT = alow.split()
dict = {}
for i in lisT:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for j in dict:
    print(j, dict[j])