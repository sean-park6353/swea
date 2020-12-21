T = int(input())
for i in range(T):
    numbers = list(map(int, input().split(' ')))
    print("#%d %d" % (i+1, sum(odd_nums)/len(odd_nums)))
