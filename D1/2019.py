

def func(num):
    if num < 1:
        return 1
    else:
        return func(num-1)*2


a = int(input())

arr = [i for i in range(1, a+1)]
for i in range(len(arr)+1):
    print(func(i), end=' ')
