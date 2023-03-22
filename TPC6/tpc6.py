import ply.lex as lex

print("Insira o caminho para o ficheiro .p ao qual fazer a análise léxica.")
fich = input(">> ")

f = open(fich)
texto = ""
for line in f.readlines():
    texto += line
f.close()

tokens = [
    'COMENTARIO',
    'MULTI_COMENTARIO',
    'RESERVADO',
    'TIPO_DADOS',
    'ID',
    'NUM',
    'FUNCAO',
    'LISTA',
    'ARRAY'
]

# Definição de tokens
literals = '{}=;-*(),><'

def t_RESERVADO(t):
    r'if|for|while|function|program|in\s'
    return t

def t_ID(t):
    r'[_a-z]\w*(\[.*\])?'
    return t

def t_FUNCAO(t):
    r'print'
    return t

def t_TIPO_DADOS(t):
    r'int|float|double|char'
    return t

def t_ARRAY(t):
    r'\{[\d\,]*\}'
    return t


t_LISTA = r'\[.*\]'
t_COMENTARIO = r'\/\/.*'
t_MULTI_COMENTARIO = r'\/\*(.|\n)*?\*\/'
t_NUM = r'\d+'

# Ignorar espaços brancos
t_ignore = ' \t\n'

# Em caso de erro
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()
lexer.input(texto)
while True:
    tok = lexer.token()
    if not tok: # Não é um token
        break
    print(tok)