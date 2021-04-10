import random
spisok = []
chislo = 1000
lenn = []
for i in range(chislo):
    rndm = random.randint(100000, 999999)
    if rndm not in spisok:
        spisok.append(rndm)
    else:
        chislo += 1
for j in spisok:
    summanechotnich = int(j) % 1000000 // 100000 + int(j) % 10000 // 1000 + int(j) % 100 // 10
    summachotnich = int(j) % 100000 // 10000 + int(j) % 1000 // 100 + int(j) % 10
    answ = 0
    if summanechotnich == summachotnich:
        lenn.append(j)
        print(j)
print(len(lenn))
