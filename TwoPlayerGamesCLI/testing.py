string = '' 
count = 0
total = 0
lenght = 20
total = 2 ** lenght

def int_binary(conv):
    _list = []
    for r in range(lenght):
        _list.append(0)
    for a in range(lenght):
        if conv - (2** (lenght-a-1)) >0:
            conv -= (2** (lenght-a-1))
            _list[a] = 1
    binary = ''
    for c in range(lenght):
        if _list[c] == 1:
            binary += 'A'
        else:
            binary += 'B'
    return binary


    ...

for i in range(total + 1):
    bina =int_binary(i)
    if 'ABBA' in bina:
        print(bina)
        count += 1
    ...
print(count)