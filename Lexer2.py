import re
import ply.lex as lex

# Definición de los tokens

tokens = (
    "FUNC", "ID", "LPAREN", "RPAREN", "VAR", "SEMICOLON", "COLON", "INT", "BEGIN", "END",
    "IF", "THEN", "ELSE", "WHILE", "DO", "CALL", "RETURN", "PLUS", "MINUS",
    "TIMES", "DIVIDE", "NUMBER, EQUALS"
)

#Expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_COLON = r','
t_ignore = ' \t'

# Definición de las reglas léxicas

def t_FUNC(t):
    r"FUNC"
    return t

def t_ID(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    t.type = "ID"
    return t

def t_RCONST(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t

def t_ICONST(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_SCONST(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("Error: caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_VAR(t):
    r"VAR"
    return t


def t_BEGIN(t):
    r"BEGIN"
    return t

def t_END(t):
    r"END"
    return t

def t_IF(t):
    r"IF"
    return t

def t_THEN(t):
    r"THEN"
    return t

def t_ELSE(t):
    r"ELSE"
    return t

def t_WHILE(t):
    r"WHILE"
    return t

def t_DO(t):
    r"DO"
    return t

def t_CALL(t):
    r"CALL"
    return t

def t_RETURN(t):
    r"RETURN"
    return t

# Definición de la función principal

def main():
    # Crear un analizador léxico
    lexer = lex.lex()

# Leer un programa
    input_data = open("program.pl0", "r").read()

# Analizar el programa
    lexer.input(input_data)
    while True:
        token = lexer.token()
    if not token:
        pass
    print(token.type, token.value)

# Llamada a la función principal

if __name__ == "__main__":
    main()
