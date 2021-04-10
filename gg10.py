import random
smallest = 300
biggest = 0
valuess = []
slovar = {}
for i in range(1,101):
    slovar[i] = random.randint(100,300)
for valu in slovar.values():
    valuess.append(valu)
for j in valuess:
    if j > biggest:
        biggest = j
    if j < smallest:
        smallest = j
print(smallest, biggest, valuess, slovar)