import re
import math

def processosPorAno(file):
    dic = {}

    with open(file) as f:
        for line in f.readlines():
            res = re.search("::", line)
            if res != None:
                res = re.split("::", line)
                ano = re.split("-",res[1])[0]
                if ano not in dic.keys():
                    dic[ano] = 1
                else:
                    dic[ano] += 1
    
    return dic

def nomesApelidos(file):
    seculos = {}

    with open(file) as f:
        for line in f.readlines():
            res = re.search("::", line)
            if res != None:
                res = re.split("::", line)
                ano = re.split("-",res[1])[0]
                seculo = math.floor(int(ano) / 100) +1
                res = res[2:]

                for pessoa in res:
                    pal = re.split(" ", pessoa)

                    if seculo not in seculos.keys():
                        seculos[seculo] = {} 
                    
                    if pal[0] not in seculos[seculo].keys():
                        seculos[seculo][pal[0]] = 1
                    else:
                        seculos[seculo][pal[0]] += 1

                    if pal[-1] not in seculos[seculo].keys():
                        seculos[seculo][pal[-1]] = 1
                    else:
                        seculos[seculo][pal[-1]] += 1


    return seculos

# def relacoes(file):
#     dic = {}
# 
#     with open(file) as f:
#         for line in f.readlines():
#             
#     
#     return dic

def toJson(fileIn, fileOut):
    i = 0

    with open(fileIn) as fin:
        with open(fileOut, "w") as fout:
            fout.write('{\n\t"processos": [\n')
            while i < 20:
                line = fin.readline()
                res = re.search(r"(::)+",line)
                if res != None:
                    res = re.split(r"::+", line)
                    fout.write('\t\t{\n\t\t\t"id": "' + res[0] + '",')
                    fout.write('\n\t\t\t"data": "' + res[1] + '",')
                    fout.write('\n\t\t\t"confessados": [')
                    res = res[2:-1]
                    
                    for index, pessoa in enumerate(res):
                        if index == len(res)-1:
                            fout.write('"' + pessoa + '"')
                        else:   
                            fout.write('"' + pessoa + '", ')
                    
                    if(i == 19):
                        fout.write(']\n\t\t}\n')
                    else:
                        fout.write(']\n\t\t},\n')

                i += 1
            
            fout.write('\t]\n}')

toJson("processos.txt", "teste.json")