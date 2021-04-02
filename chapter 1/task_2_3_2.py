def modify_list(l):
    newList = []
    for i in range(lst):
        if i % 2 == 0:
            newList.append(i)
            return newList


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))