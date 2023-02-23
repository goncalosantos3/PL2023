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
        res = re.search("on|ON|oN|On", inp)
        if res != None:
            stop = False
        else:
            res = re.search("off|ofF|oFf|Off|oFF|OFf|OfF|OFF", inp)
            if res != None:
                stop = True
            elif stop == False:
                res = re.search("[0-9]*" ,inp)
                while res != None:
                    number = res.group()
                    total += int(number)
                    inp = inp.replace(number,"")
                    res = re.search("[0-9]+" ,inp)
        
    inp = input(">> ")