inputik = int(input('Please input your number:'))

a = 1
chislo = 0
for i in range(a):
    inputik = inputik / 2
    inputik = int(inputik)
    if int(inputik) % 2 == 0:
        chislo += 1
    inputiktwo = int(inputik) / 2
    inputiktwo = int(inputiktwo)
    if int(inputiktwo) % 2 == 0:
        a += 1

print(chislo, a, inputik, inputiktwo)