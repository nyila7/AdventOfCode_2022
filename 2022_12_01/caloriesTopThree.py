f = open("C:\input.txt", 'r')

index = 0

osszegLista = []
szamlalo = 0

for i in f:

    if i == "\n":
        osszegLista.append(szamlalo)
        index += 1
        szamlalo = 0
    else:
        szamlalo += int(i)

print(sum(sorted(osszegLista, reverse=True)[:3]))

