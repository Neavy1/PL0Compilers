import ply.lex as lex
import ply.yacc as yacc

# Definir los tokens del lenguaje
tokens = (
    "FUNC", "ID", "LPAREN", "RPAREN", "VAR", "SEMICOLON", "COLON", "INT", "BEGIN", "END",
    "IF", "THEN", "ELSE", "WHILE", "DO", "CALL", "RETURN", "PLUS", "MINUS",
    "TIMES", "DIVIDE", "NUMBER, EQUALS")

# Expresiones regulares para los tokens
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

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_ICONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_RCONST(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_SCONST(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("Error: caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Definir la gramática
def p_prog(p):
    'prog : BEGIN stmts END'
    p[0] = p[2]

def p_stmts(p):
    'stmts : stmts stmt'
    p[0] = p[1] + [p[2]]

def p_stmts_empty(p):
    'stmts :'
    p[0] = []

def p_printstmt(p):
    'stmt : PRINT exprlist SEMICOLON'
    p[0] = ('print', p[2])

def p_ifstmt(p):
    'stmt : IF LPAREN expr RPAREN THEN expr SEMICOLON'
    p[0] = ('if', p[3], p[6])

def p_assignstmt(p):
    'stmt : IDENT EQUALS expr SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_exprlist(p):
    'exprlist : exprlist COMMA expr'
    p[0] = p[1] + [p[3]]

def p_exprlist_single(p):
    'exprlist : expr'
    p[0] = [p[1]]

def p_expr_plus(p):
    'expr : term PLUS expr'
    p[0] = ('+', p[1], p[3])

def p_expr_minus(p):
    'expr : term MINUS expr'
    p[0] = ('-', p[1], p[3])

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_term_times(p):
    'term : factor TIMES term'
    p[0] = ('*', p[1], p[3])

def p_term_divide(p):
    'term : factor DIVIDE term'
    p[0] = ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_ident(p):
    'factor : IDENT'
    p[0] = ('ident', p[1])

def p_factor_literal(p):
    'factor : literal'
    p[0] = ('literal', p[1])

def p_factor_paren(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]

def p_literal_iconst(p):
    'literal : ICONST'
    p[0] = ('iconst', p[1])

def p_literal_rconst(p):
    'literal : RCONST'
    p[0] = ('rconst', p[1])

def p_literal_sconst(p):
    'literal : SCONST'
    p[0] = ('sconst', p[1])

def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis en la entrada")

# Construir el parser
lexer = lex.lex()
parser = yacc.yacc()

# Ejemplo de programa
programa = '''
BEGIN
  PRINT "Hola, mundo!";
  x = 2 + 3 * 4;
  IF (x > 10) THEN
    PRINT "x es mayor que 10";
  ENDIF
END
'''

# Analizar el programa
ast = parser.parse(programa)

# Ejecutar el programa        
def evaluar_expr(expr, variables):
    tipo = expr[0]
    if tipo == '+':
        return evaluar_expr(expr[1], variables) + evaluar_expr(expr[2], variables)
    elif tipo == '-':
        return evaluar_expr(expr[1], variables) - evaluar_expr(expr[2]),

    elif tipo == '*':
        return evaluar_expr(expr[1], variables) * evaluar_expr(expr[2], variables)
    elif tipo == '/':
        return evaluar_expr(expr[1], variables) / evaluar_expr(expr[2], variables)
    elif tipo == 'ident':
        return variables.get(expr[1], 0)
    elif tipo == 'literal':
        return expr[1]
        
def ejecutar_stmt(stmt, variables):
    for instruccion in stmt:
        tipo = instruccion[0]
        if tipo == 'print':
            valores = [evaluar_expr(e, variables) for e in instruccion[1]]
            print(*valores)
        elif tipo == 'if':
            condicion = evaluar_expr(instruccion[1], variables)
            if condicion:
                ejecutar_stmt(instruccion[2], variables)
        elif tipo == 'assign':
            variables[instruccion[1]] = evaluar_expr(instruccion[2], variables)
            
variables = {}
for instruccion in ast:
    tipo = instruccion[0]
    if tipo == 'print':
        valores = [evaluar_expr(e, variables) for e in instruccion[1]]
        print(*valores)
    elif tipo == 'if':
        condicion = evaluar_expr(instruccion[1], variables)
        if condicion:
            ejecutar_stmt(instruccion[2], variables)
    elif tipo == 'assign':
        variables[instruccion[1]] = evaluar_expr(instruccion[2], variables)