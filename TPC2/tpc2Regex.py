import re
print("Bem-Vindo ao meu programa Somador On/Off implementado em Python!")
print("Insira digitos para realizar uma soma")

total = 0
stop = False
inp = input(">> ")

while inp != "":

    if inp == "=":
        print(total)    
    else:
        res = re.search("on", inp.lower())
        if res != None:
            stop = False
        else:
            res = re.search("off", inp.lower())
            if res != None:
                stop = True
            elif stop == False:
                lst = re.findall("[0-9]+" ,inp)
                for elem in lst:
                    total += int(elem)
        
    inp = input(">> ")