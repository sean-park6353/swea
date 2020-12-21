
a = int(input())

arr = [i for i in range(1, a+1)]
arr = arr[::-1]
for i in arr:
    print(i, end=' ')
