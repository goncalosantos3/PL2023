import re

dicGlobal = {}
file = open("processos.txt")
entrada = re.compile(r'(?P<data>(?P<ano>\d+)-\d+-\d+)')

for line in file.readlines():
    dic = entrada.search(line)

    if dic != None:
        if dic['ano'] not in dicGlobal.keys():
            dicGlobal[dic['ano']] = 1
        else:
            dicGlobal[dic['ano']] += 1
    else: 
        print("Não houve match!")

print(dicGlobal)

file.close()