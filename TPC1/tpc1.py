import math

# Retorna uma lista de listas que reprensenta a informação no ficheiro csv
def carregaFicheiro(path):
    est = []
    f = open(path)

    for line in f.readlines():
        line = line[:-1]
        est.append(line.split(','))

    f.close()
    est.pop(0)
    return est

def distSexo(est):
    doencaF = 0
    doencaM = 0

    for entrada in est:
        if entrada[5] == '1' and entrada[1] == 'F':
            doencaF += 1
        if entrada[5] == '1' and entrada[1] == 'M':
            doencaM += 1

    dic = {}
    dic['Feminino'] = doencaF
    dic['Masculino'] = doencaM
    return dic

def distEscaloesEtarios(est):
    total = 0
    aux = {}

    for entrada in est:
        if entrada[5] == '1':
            num = math.floor(int(entrada[0])/5) + 1
            if num not in aux.keys():
                total += 1
                aux[num] = 1
            else:
                total += 1
                aux[num] += 1

    return aux


def distColesterol(est):
    aux = {}

    for entrada in est:
        if entrada[5] == '1':
            nivel = math.floor(int(entrada[3])/10) + 1
            if nivel not in aux.keys():
                aux[nivel] = 1
            else:
                aux[nivel] += 1
    
    return aux


def imprimeDist(dist, sexo=False, idade=False, colesterol=False):

    if sexo:
        print("Quantidade de casos de doença por Sexo")
        print("|   Feminino   |   Masculino   |")
        print("--------------------------------")
        print(f"|      {dist['Feminino']}      |      {dist['Masculino']}      |")
        print("--------------------------------\n")
    elif idade:
        print("Quantidade de casos de doença por Faixa Etária")
        print("---------------")
        keys = list(dist.keys())
        keys.sort()
        for key in keys:
            if len(str(dist[key])) == 1:
                print(f"[{(key-1)*5}-{key*5-1}] | {dist[key]}   |")
            elif len(str(dist[key])) == 2:
                print(f"[{(key-1)*5}-{key*5-1}] | {dist[key]}  |")
            else:
                print(f"[{(key-1)*5}-{key*5-1}] | {dist[key]} |")
            print("---------------")
        print("\n")

est = carregaFicheiro('myheart.csv')

print("Distribuição da doença por Sexo")
dic = distSexo(est)
# print(f"Quantidade de casos da doença no Sexo Feminino: {dic['Feminino']}")
# print(f"Quantidade de casos da doença no Sexo Masculino: {dic['Masculino']}\n")
imprimeDist(dic, sexo=True)

print("Distribuição da doença por Faixa Etária")
dic = distEscaloesEtarios(est)
# for key in dic.keys():
#     print(f"Quantidade de casos da doença na faixa etária [{(key-1)*5}-{key*5-1}]: {dic[key]}")
# print("\n")
imprimeDist(dic, idade=True)

print("Distribuição da doença por Níveis de Colesterol")
dic = distColesterol(est)
for key in dic.keys():
    print(f"Quantidade de casos da doença no nível de colesterol [{(key-1)*10}-{key*10-1}]: {dic[key]}")
print("\n")

