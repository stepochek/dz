noreturn = {'lol': 'nolol','lolol':'nololol'}
returnn = {}
hohoho = []
for i in noreturn.keys():
    hohoho.append(i)
for j in noreturn.values():
    hohoho.append(j)
haha = len(hohoho) // 2
print(hohoho)
for k in range(haha):
    returnn[hohoho[haha]] = hohoho[k]
    haha += 1
print(returnn)
