# a, b, c = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))
# result = 0
# cnt = 1
# if arr.count(max(arr)) >= 1:
#     for i in range(1, b+1):
#         if cnt >= c+1:
#             tmp = arr.pop(arr.index(max(arr)))
#             result = result+max(arr)
#             arr.append(tmp)
#             cnt = 1
#         else:
#             cnt += 1
#             result = result+max(arr)
#     print("한 개 인경우")
# else:

#     print("두 개 이상인 경우")


# print(result)


a, b, c = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
one = arr.pop(arr.index(max(arr)))
two = arr.pop(arr.index(max(arr)))
arr.append(one)
arr.append(two)
