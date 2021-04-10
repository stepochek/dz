string = 'a3v3b2j6f8dg0d1g6d3'
def my(string):
    letters = ''
    numbers = ''
    for i in string:
        if i.isdigit() or i == '.':
            numbers += str(i)
        else:
            letters += str(i)
    return letters,numbers
print(my(string))