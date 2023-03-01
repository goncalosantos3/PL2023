print("Bem-Vindo ao meu programa Somador On/Off implementado em Python!")
print("Insira digitos para realizar uma soma")

c = ''
total = 0
stop = False
inp = input(">> ")

while inp != "":

    if "off" == inp.lower():
        stop = True
    elif "on" == inp.lower():
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
                numero += c
                i += 1
                if i < len(inp):
                    c = inp[i]

            if numero != "":
                total += int(numero)
                numero = ""
            i += 1
        
    inp = input(">> ")