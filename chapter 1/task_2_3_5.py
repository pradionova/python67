def f(n):
    return n


n1 = int(input())
while n1 > 0:
    value = int(input())
    key = f(value)
    dict = {}
    if key in dict:
        print(dict[key])
    else:
        dict[key] = value
        print(value)
    n1 -= 1
