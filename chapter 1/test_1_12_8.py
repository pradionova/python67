a = int(input())
num6 = a % 10 
num5 = a % 100 // 10
num4 = a % 1000 // 100
num3 = a % 10000 // 1000
num2 = a % 100000 // 10000
num1 = a % 1000000 // 100000
if num1 + num2 + num3 == num4 + num5 + num6:
    print('Счастливый')
if num1 + num2 + num3 != num4 + num5 + num6:
    print('Обычный')