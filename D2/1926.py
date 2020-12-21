

a = input()
result = []

for i in range(1, int(a)+1):
    value = str(i)
    arr = list(map(str, value))
    if arr.count('3') != 0 or arr.count('6') != 0 or arr.count('9') != 0:
        cnt = arr.count('3')+arr.count('6')+arr.count('9')
        result.append('-'*cnt)
    else:
        result.append(i)

for i in result:
    print(i, end=' ')

    

    
