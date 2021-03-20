a = input()
list1 = a.split()
len1 = len(list1)
space = ''
if len1 == 1:
    print(a)
else:
    for i in range(0, len1):
        if i == 0:
            previewIndex = len1 - 1
        else:
            previewIndex = i - 1
#----------------------------------
        if i == len1 - 1:
            nextIndex = 0
        else:
            nextIndex = i + 1

        n1 = list1[previewIndex]
        n2 = list1[nextIndex]
        sum = int(n1) + int(n2)
        space += str(sum)
        space += ' '
print(space)