lst = input()
x = input()
spitLst = lst.split()
lenLst = len(lst)
for i in range(lenLst):
    if i == x:
        print(i)