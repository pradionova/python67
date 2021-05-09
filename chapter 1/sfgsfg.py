def culcV(v, n, m):
    left = 0
    right = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            p = (r - 1) * m + c
            if v <= c:
                right += p
            else:
                left += p

    return abs(left - right)

def culcH(h, n, m):
    top = 0
    bottom = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            p = (r - 1) * m + c
            if h <= r:
                bottom += p
            else:
                top += p

    return abs(top - bottom)

def printt(n, m):
    hash = {}
    for a in range(1, m + 1):
        hash['V ' + str(a)] = culcV(a, n, m)

    for b in range(1, n + 1):
        hash['H ' + str(b)] = culcH(b, n, m)

    s = min(hash, key = hash.get)
    return s

results = []
countt = int(input())
for i in range(countt):
    sttr = input().split(' ')
    n = int(sttr[0])
    m = int(sttr[1])
    results.append(printt(n, m))
    
for rr in results:
    print(rr)

#printt(1, 3) #V 3
#printt(4, 7) #V 5
#printt(1, 10) #V 8
#printt(3, 3) #H 3
#printt(3, 5) #V 4

            


