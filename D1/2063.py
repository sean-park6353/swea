# T = int(input())
# for i in range(T):
#     numbers = list(map(int, input().split(' ')))


# print(numbers)


T = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
print(arr[round((T-1)/2)])
