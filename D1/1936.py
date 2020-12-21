
#! 가위 1
# ? 바위 2
# * 보 3

A, B = map(int, (input().split(' ')))


if A == 1:
    if B == 2:
        print("B")
    elif B == 3:
        print("A")
if A == 2:
    if B == 1:
        print("A")
    elif B == 3:
        print("B")
if A == 3:
    if B == 1:
        print("B")
    else:
        print("A")
