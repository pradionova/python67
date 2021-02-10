import math

a = input()
pi = 3.14

if a == 'прямоугольник':
    b = int(input())
    c = int(input())
    print(b * c)
elif a == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    print(math.sqrt(s))
elif a == 'круг':
    r = int(input())
    print(pi * r * r)