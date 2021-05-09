def f(n):
    return n

dict = {}
n1 = int(input())
for i in range(n1):
    inputNum = int(input())
    if inputNum not in dict:
        dict[inputNum] = f(inputNum)

    print(dict[inputNum])