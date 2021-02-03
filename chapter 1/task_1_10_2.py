a = int(input())
if a % 4 != 0:
    print('Обычный')
elif a % 100 != 0:
    print('Високосный')
elif a % 400 == 0:
    print('Високосный') 
else:
    print('Обычный')