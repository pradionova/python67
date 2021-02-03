a = int(input())
n = 'программистов'
m = 'программист'
k = 'программиста'

# ------- MAIN -------

a1 = a % 100

# ------- N -------

if a1 == 11 or a1 == 12 or a1 == 13 or a1 == 14:
    print(a, n)
elif a1 % 10 == 5 or a1 % 10 == 6 or a1 % 10 == 7 or a1 % 10 == 8 or a1 % 10 == 9 or a1 % 10 == 0:
    print(a, n)

# ------- M -------

elif a1 == 1:
    print(a, m)
elif a1 % 10 == 1:
    print(a, m)

# ------- K -------

elif a1 == 2 or a1 == 3 or a1 == 4:
    print(a, k)
elif a1 % 10 == 2 or a1 % 10 == 3 or a1 % 10 == 4:
    print(a, k)