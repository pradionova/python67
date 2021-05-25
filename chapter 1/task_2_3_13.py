# ------------VARIABLES------------
a = input()
b = input()
ab = input()
bc = input()
dict1 = {}
dict2 = {}
ab_result = ''
bc_result = ''
# ------------FOR1------------
for i in range(len(a)):
    dict1[a[i]] = b[i]
    dict2[b[i]] = a[i]
# ------------DICT1------------
for j in ab:
    ab_result += dict1[j]
# ------------DICT2------------
for k in bc:
    bc_result += dict2[k]
    
print(ab_result)
print(bc_result)