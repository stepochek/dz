HELLO = 123  # это константа
field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def print_field(my_field):
    print(' _ _ _')
    for i in my_field:
        c = ""
        for b in i:
            c += '|' + b
        print(c + '|')


def make_move(my_field, move, coo, move_ch):
    if my_field[(coo - 1) // 3][(coo - 1) % 3] == "_":
        my_field[(coo - 1) // 3][(coo - 1) % 3] = move
        return my_field, True
    else:
        print('Клетка занята')
        move_ch += 1
        return my_field, False, move_ch

gg = True
print('LETS PLAY!')
print_field(field)
move_type = ['X', 'O']
move_ch = 1
print('Move of: ', move_type[move_ch % 2])
a = 0
while gg == True:
    coords = int(input('make your move: '))
    field = make_move(field, move_type[move_ch % 2], coords , move_ch)[0]
    print_field(field)
    move_ch += 1
    for i in field or field[(1 - 1) // 3][(1 - 1) % 3] == field[(4 - 1) // 3][(4 - 1) % 3] and field[(1 - 1) // 3][(1 - 1) % 3] == field[(7 - 1) // 3][(7 - 1) % 3]:
        for h in i:
            if h == '_':
                a += 1
    if a == 0:
        j = input('Хотите ли вы сыграть еще одну игру?')
        if j == 'да':
            gg = False