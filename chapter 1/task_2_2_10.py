sum = 0
result = 0
while True:
    a = int(input())
    sum += a
    result += a * a
    if sum == 0:
        break
print(result)