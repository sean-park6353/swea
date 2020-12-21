N = int(input())
for i in range(N):
    numbers = list(map(int, input().split(' ')))
    print("#%d %d" % (i+1, max(numbers)))
