import ply.lex as lex

# Definición de los tokens

tokens = (
    "PROGRAM", "PROCEDURE", "MAIN", ";", "VAR", "ID", ":", "ASSIGN",
    "IF", "THEN", "ELSE", "WHILE", "DO", "CALL", "RETURN", "+", "-", "*", "/"
)

# Definición de las reglas léxicas

def t_PROGRAM(t):
    r"PROGRAM"
    return t

def t_PROCEDURE(t):
    r"PROCEDURE"
    return t

def t_MAIN(t):
    r"MAIN"
    return t

def t_SEMI(t):
    r";"
    return t

def t_VAR(t):
    r"VAR"
    return t

def t_ID(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    return t

def t_COLON(t):
    r":"
    return t

def t_ASSIGN(t):
    r"="
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

def t_PLUS(t):
    r"+"
    return t

def t_MINUS(t):
    r"-"
    return t

def t_TIMES(t):
    r"*"
    return t

def t_DIVIDE(t):
    r"/"
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_error(t):
    print("Error léxico en '%s'" % t.value)
    t.lexer.skip(1)

# Creación del analizador léxico

lexer = lex.lex()

# Prueba del analizador léxico

text = """
PROGRAM Main;
VAR
    a, b : INTEGER;
BEGIN
    a := 1;
    b := 2;
    IF a < b THEN
    WRITE(a);
ELSE
    WRITE(b);
END.
"""

lexer.input(text)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
