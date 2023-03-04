import re
import json

processos = []
i = 0
file = open("processos.txt")
entrada = re.compile(r'(?P<pasta>\d+)::+(?P<ano>\d+-\d+-\d+)::+(?P<nome>[\w\s]+)::+(?P<pai>[\w\s]+)::+(?P<mae>[\w\s]+)::+(?P<obs>[\w\s]+)*')

while i < 20:
    line = file.readline()
    dic = entrada.search(line)

    if dic != None:
        dicionario = dic.groupdict()
        if dicionario['obs'] == '\n':
            del dicionario['obs']

        processos.append(dicionario)
    else:
        print("Não houve match! Linha: " + str(i+1))
    
    i += 1

file.close()

jsonString = json.dumps(processos, indent = 2)

fout = open("teste.json", "w")
fout.write(jsonString)
fout.close()