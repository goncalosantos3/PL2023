import re
import math

dicGlobal = {}
file = open("processos.txt")
entrada = re.compile(r'(?P<data>(?P<ano>\d+)-\d+-\d+)::+(?P<p1>\w+)[\s\w]+\s(?P<u1>\w+)::+(?P<p2>\w+)[\s\w]+\s(?P<u2>\w+)::+(?P<p3>\w+)[\s\w]+\s(?P<u3>\w+)')

for line in file.readlines():
    dic = entrada.search(line)

    if dic != None:
        sec = math.floor(int(dic['ano']) / 100) + 1
        if sec not in dicGlobal.keys():
            dicGlobal[sec] = {}
        
        nomes = [dic['p1'],dic['p2'],dic['p3'],dic['u1'],dic['u2'],dic['u3']]
        for nome in nomes:
            if nome not in dicGlobal[sec].keys():
                dicGlobal[sec][nome] = 1
            else:
                dicGlobal[sec][nome] += 1
    else: 
        print("Não houve match!")

print(dicGlobal)

file.close()