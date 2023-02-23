print("Bem-Vindo ao meu programa Somador On/Off implementado em Python!")
print("Insira digitos para realizar uma soma")

def compara(ele, lst):

    for elem in lst:
        if elem == ele:
            return True
        
    return False

c = ''
total = 0
stop = False
off = ["off","ofF","oFf","Off","oFF","OFf","OfF","OFF"]
on = ["on", "On", "oN","ON"]
inp = input(">> ")

while inp != "":

    if compara(inp,off):
        stop = True
    elif compara(inp,on):
        stop = False  
    elif inp == "=":
        print(total)
    elif stop == False:
        numero = ""
        i = 0
        c = inp[i]

        while i < len(inp):
            c = inp[i]
            while c.isdigit() and i < len(inp):
                c = inp[i]
                numero += c
                i += 1

            if numero != "":
                print("Número-> " + numero)
                total += int(numero)
                numero = ""
            i += 1
        

    inp = input(">> ")