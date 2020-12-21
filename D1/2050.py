def func(alphabet):
    return ord(alphabet)-64


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    a = input()
    tmp = list(map(func, list(a)))
    for i in tmp:
        print(i, end=' ')
