a = 'f2dh5r2r7i9'
def my(string):
    m = 0
    for i in string:
        if i.isdigit():
            m += 1
    return m
print(my(a))
