string = '' 
count = 0
total = 0
lenght = 10
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
    if 'ABBBA' in bina:
        print(bina)
        count += 1
    ...
print(count)
items = ['<li>Apple</li>', '<li>Banana</li>', '<li>Cherry</li>']
html = '\n'.join(items)
print(html)

li = []
for i in range(10000,100000):
    if i % 7 == 0:
        li.append(i)

print(li)