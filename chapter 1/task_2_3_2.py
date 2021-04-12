def modify_list(l):
    for i in range(len(l) -1, -1, -1):
        if l[i] % 2 != 0:
            l.remove(l[i])
    for j in range(len(l)):
        if l[j] % 2 == 0:
            l[j] = int(l[j] / 2)

lst = [1, 3, 5, 7]
modify_list(lst)
print(lst)