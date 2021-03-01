# ----------- NUMBER -----------
print('Введите число:')
num = int(input())
# ----------- WHILE START -----------
count = 0
while num >= 0:
    
    if num % 3 == 0:
        num = num - 1
    elif num % 3 == 2:
        num = num - 2
    elif num % 3 == 1:
        num = num + 2

    count = count + 1

print('Kоличество операций:', count)