
T = int(input())
for i in range(1, T+1):
    arr = [0 for p in range(5)]
    n = int(input())
    j = 0
    while True:
        if n % 2 == 0:
            n = n/2
            arr[0] += 1
        elif n % 3 == 0:
            n = n/3
            arr[1] += 1
        elif n % 5 == 0:
            n = n/5
            arr[2] += 1
        elif n % 7 == 0:
            n = n/7
            arr[3] += 1
        elif n % 11 == 0:
            n = n/11
            arr[4] += 1
        else:
            break

    print('#%d ' % i, end='')
    for d in range(len(arr)):
        print(arr[d], end=' ')
    print()
