T = int(input())
for j in range(1, T+1):
    n = int(input())
    cnt = []
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = 0
    for i in range(len(money)):
        cnt.append(n//money[i])
        n = n - money[i]*(n//money[i])
    print('#%d' % j)
    for i in range(len(cnt)):
        print(cnt[i], end=' ')
    print()

    
