a = int(input())
b = int(input())
if a % b == 0 and a > b:
    print(a)
elif b % a == 0 and b > a:
    print(b)
elif a == b:
    print(a)
else:
    print(a * b)