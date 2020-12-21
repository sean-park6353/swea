

tmp = input()


def func(tmp):
    arr = ""
    for i in range(len(tmp)):
        arr += tmp[i]
        for j in range(i+1, i+3):
            if arr == tmp[j:j+len(arr)]:
                return j


print(func(tmp))
