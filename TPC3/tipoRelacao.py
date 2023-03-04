import re

dicGlobal = {}
file = open("processos.txt")

for line in file.readlines():
    lista = re.findall(r',(\w[\w\s]+\w).', line)

    for relacao in lista:
        if relacao not in dicGlobal.keys():
            dicGlobal[relacao] = 1
        else:
            dicGlobal[relacao] += 1

print(dicGlobal)

file.close()