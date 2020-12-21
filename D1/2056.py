T = int(input())
for test_case in range(1, T + 1):
    a = input()
    y = a[0:4]
    m = a[4:6]
    d = a[6:]
    if int(m) == 1 or int(m) == 3 or int(m) == 5 or int(m) == 7 or int(m) == 8 or int(m) == 10 or int(m) == 12:
        if int(d) <= 31 and int(d) > 0:
            result = y+'/'+m+'/'+d
        else:
            result = -1
    elif int(m) == 2:
        if int(d) <= 28 and int(d) > 0:
            result = y+'/'+m+'/'+d
        else:
            result = -1
    elif int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11:
        if int(d) <= 30 and int(d) > 0:
            result = y+'/'+m+'/'+d
        else:
            result = -1
    else:
        result = -1
    print('#%d %s' % (test_case, result))
