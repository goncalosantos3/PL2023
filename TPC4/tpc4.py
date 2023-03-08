import re
import json

alunos = []

with open("input.csv") as f:
    cabecalho = f.readline()
    campos = re.split(r',', cabecalho)
    regex = r''

    for campo in campos:
        campo = campo.replace("\n", "")
        regex += rf'(?P<{campo}>[\w\s]+),*'

    print("Regular expression: " + regex)
    comp = re.compile(regex)

    for line in f.readlines():
        line = line.replace("\n", "")
        ent = comp.search(line)

        if ent:
            alunos.append(ent.groupdict())
        else:
            print("Fudeu")

jsonStr = json.dumps(alunos, indent = 2, ensure_ascii = False)
fout = open("output.json", "w")
fout.write(jsonStr)
fout.close()