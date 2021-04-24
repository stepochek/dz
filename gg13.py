stroka = input(':')


def func(stroka):
    summ = 0
    for i in stroka:
        if i.isdigit():
            summ += int(i)
    return summ


print(func(stroka))