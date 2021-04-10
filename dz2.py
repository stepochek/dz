import random
file = input('Edit text:')
fule = []
ids = []
fuller = []
answer = ''
x = -1
a = -1
z = 1
fule.append(file)
for i in fule:
    f = i.split(' ')
p = f
for n in f:
    ids.append(id(n))
for l in range(len(f)):
    x += 1
    fuller.append(random.choice(p))
    p.remove(fuller[x])
print(fuller)
for q in ids:
    for b in range(z):
        for y in fuller:
            if q == id(y):
                answer += str(y)
                answer += ' '
            else:
                z += 1
            z = 1
with open('lol.txt','w') as file:
    file.write(answer)
print(answer)
            
