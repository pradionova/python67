a = float(input())
b = float(input())
oper = input()
if oper == '+':
    print(a + b)
#elif (oper == '/' & b == 0):
#    print('Деление на 0!')
elif oper == '-':
    print(a - b)
elif oper == '*':
    print(a * b)
elif oper == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
        
elif oper == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)

elif oper == 'pow':
    print(a ** b)

elif oper == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)