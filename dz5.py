a = [-18888, 2, 5, 4, 2, 8, -100]
b = a[0]
for i in a:
    if i < int(b):
        b = 0
        b += int(i)
print(b)

