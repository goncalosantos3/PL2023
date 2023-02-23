import math
import matplotlib.pyplot as plt

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
        print("------------------------------------")
        print("|    Sexo    | Quantidade de Casos |")
        print("------------------------------------")
        print(f"|  Feminino  |         {dist['Feminino']}          |")
        print("------------------------------------")
        print(f"|  Masculino |         {dist['Masculino']}         |")
        print("------------------------------------\n")
    elif idade:
        print("Quantidade de casos de doença por Faixa Etária")
        print("--------------------------------------")
        print("| Faixa Etária | Quantidade de Casos |")
        print("--------------------------------------")
        keys = list(dist.keys())
        keys.sort()
        for key in keys:
            if len(str(dist[key])) == 1:
                print(f"|    [{(key-1)*5}-{key*5-1}]   |          {dist[key]}          |")
            elif len(str(dist[key])) == 2:
                print(f"|    [{(key-1)*5}-{key*5-1}]   |          {dist[key]}         |")
            else:
                print(f"|    [{(key-1)*5}-{key*5-1}]   |         {dist[key]}         |")
            print("--------------------------------------")
        print("\n")
    elif colesterol:
        print("Quantidade de casos de doença por níveis de Colesterol")
        print("---------------------------------------------")
        print("| Nível de Colesterol | Quantidade de Casos |")
        print("---------------------------------------------")
        keys = list(dist.keys())
        keys.sort()
        for key in keys:
            print(f"|      [{(key-1)*10}-{key*10 - 1}]      |         {dist[key]}         |")
            print("---------------------------------------------")
        print("\n")

est = carregaFicheiro('myheart.csv')

print("----------------------------------------- Tabelas ----------------------------------")

print("Distribuição da doença por Sexo")
dicSex = distSexo(est)
imprimeDist(dicSex, sexo=True)

print("Distribuição da doença por Faixa Etária")
dicEt = distEscaloesEtarios(est)
imprimeDist(dicEt, idade=True)

print("Distribuição da doença por Níveis de Colesterol")
dicCol = distColesterol(est)
imprimeDist(dicCol, colesterol=True)

# ----------------------------------------- Gráficos -------------------------------------
# -- Por Sexo
# x-coordinates of left sides of bars 
# 1 -> Feminino | 2 -> Masculino 
left = [1, 2]
  
# heights of bars
height = [dicSex['Feminino'], dicSex['Masculino']]
  
# labels for bars
tick_label = ['Feminino', 'Masculino']
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('Sexo')
# naming the y-axis
plt.ylabel('Quantidade de Casos')
# plot title
plt.title('Gráfico de Barras')
  
# function to show the plot
plt.show()


# -- Por Faixa Etária
# x-coordinates of left sides of bars 
keys = list(dicEt.keys())
keys.sort()
left = []
for i in range(len(dicEt)):
    left.append(i+1)

# heights of bars
height = []
for key in keys:
    height.append(dicEt[key])
  
# labels for bars
tick_label = []
for key in keys:
    tick_label.append(f'[{(key-1)*5}-{key*5-1}]')
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('Faixa Etária')
# naming the y-axis
plt.ylabel('Quantidade de Casos')
# plot title
plt.title('Gráfico de Barras')
  
# function to show the plot
plt.show()


# -- Por Níveis de Colesterol
# x-coordinates of left sides of bars
keys = list(dicCol.keys())
keys.sort()
left = []
for i in range(len(dicCol)):
    left.append(i+1)

# heights of bars
height = []
for key in keys:
    height.append(dicCol[key])
  
# labels for bars
tick_label = []
for key in keys:
    tick_label.append(f'[{(key-1)*10}-{key*10-1}]')
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('Níveis de Colesterol')
# naming the y-axis
plt.ylabel('Quantidade de Casos')
# plot title
plt.title('Gráfico de Barras')
  
# function to show the plot
plt.show()