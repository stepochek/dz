import random
file = open('lol', 'w')
l = 1
word1 = ['Хорошего ', 'Приятного ', 'Счастиливого', 'Удачного', 'Уютного', 'Радостного']
word2 = ['нового', 'наступающего', 'ближайшего']
word3 = ['нового года', 'кошмара', 'праздника']
word4 = ['.', '!' , '!!!!!']
word5 = ['здоровья', 'счастья', 'сил']
word6 = ['благополучие в семье', 'друзей побольше', 'роботу получше']
word7 = ['и ума побольше', 'и жену покрасивее', 'и детей поумнее']
word8 = ['.', '!', '!!!']
file.write(random.choice(word1))
file.write(random.choice(word2))
file.write(random.choice(word3))
file.write(random.choice(word4))
file.write(random.choice('Желаю '))
file.write(random.choice(word5, ))
file.write(random.choice(word6))
file.write(random.choice(word7))
file.write(random.choice(word8))
print(random.choice(word1), random.choice(word2), random.choice(word3), random.choice(word4),'Желаю', random.choice(word5),  ',', random.choice(word6), random.choice(word7), random.choice(word8))
file.close()
