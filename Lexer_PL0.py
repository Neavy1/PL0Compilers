import os
from sly import Lexer
from sly import Parser
import pytest

class PL0Lex(Lexer):
    tokens = [
            'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
            'ODD', 'ASSING', 'NE', 'LTE', 'GTE', 'LPARENT',
            'RPARENT', 'COMMA', 'SEMICOLOM', 'COLOM',
            'DOT', 'UPDATE', 'INUM', 'RNUM',
            
            # Reservadas
            'BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO',
            'CALL', 'CONST', 'PROCEDURE', 'OUT',
            'IN', 'ELSE', 'INT', 'FLOAT', 'BOOL', 'VAR',
            'RETURN', 'BREAK', 'STRING', 'FUN', 'SKIP',
            'PRINT', 'READ', 'WRITE',
            
            # Operadores logicos:
            'AND', 'OR', 'NOT',
            
            # Operadores de relación
            'EQ', 'NEQ', 'LEQ', 'GEQ', 'GT', 'LT'
            ]

    literals = {'=', '(', ')', '+', '-', '*', '/', ',', ';', '.', '<', '>', ':='}
    ignore = '\t' 
    
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    RNUM = r'(0|[1-9]\d*)'
    INUM = r'\d+\.\d+([eE][+-]?\d+)?|\.\d+([eE][+-]?\d+)?|\d+[eE][+-]?\d+'
    STRING = r'"([^"\\]|\\.)*"'
    
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    UPDATE = r'='
    NE = r'<>'
    LT = r'<'
    LTE = r'<='
    GT = r'>'
    GTE = r'>='
    NEQ = r'!='
    EQ = r'=='
    LPARENT = r'\('
    RPARENT = r'\)'
    COMMA = r','
    SEMICOLOM = r';'
    DOT = r'\.'
    ASSING = r':='
    
    BEGIN = r'begin\b'
    ODD = r'odd\b'
    END = r'end\b'
    IF = r'if\b'
    THEN = r'then\b' 
    ELSE = r'else\b'
    WHILE = r'while\b'
    DO = r'do\b'
    PRINT = r'print\b'
    READ = r'read\b'
    WRITE = r'write\b'
    RETURN = r'return\b'
    INT = r'int\b'
    FLOAT = r'float\b'
    AND = r'and\b'
    OR = r'or\b'
    NOT = r'not\b'
    FUN = r'fun\b'
    BREAK = r'break\b'
    SKIP = r'skip\b'
    
    @_(r'0[0-9]+')
    def BAD_INT(self, t):
        error = f"Lexical error in line {self.lineno}. The number {t.value} is incorrect."
        print(error)

    @_(r'0[0-9]+\.\d+([eE][-+]?\d+)?')
    def BAD_FLOAT(self, t):
        error = f"Lexical error in line {self.lineno}. The number {t.value} is incorrect."
        print(error)

    def error(self, t):
        print(f"Lexical error in line {self.lineno}")
        self.index += 1
    
    def tokenize(self, text):
        self.lineno = 1
        tokens = []
        for token in super().tokenize(text):
            tokens.append((token.type, token.value, token.lineno))
        return tokens
    
    @_(r'\n+')
    def NEWLINE(self, t):
        self.lineno += t.value.count('\n')
    
    @_(r'/\*(.|\n)*?\*/')
    def ignore_comment(self, t):
        pass
    
    @_(r'/\*(.|\n)+')
    def ignore_incoment(self, t):
        print(f'Line {self.lineno}. Unterminated comment.')   
    
def buscarFicheros(directorio):
    try:
        ficheros = os.listdir(directorio)
        cont = 1

        for file in ficheros:
            print(str(cont) + ". " + file)
            cont = cont + 1

        numArchivo = input('\nNúmero del test: ')
        numArchivo = int(numArchivo) - 1

        if 0 <= numArchivo < len(ficheros):
            archivo_seleccionado = ficheros[numArchivo]
            print(f'Has escogido "{archivo_seleccionado}"\n')
            return archivo_seleccionado
        else:
            print("Número de archivo fuera de rango.")
            return None

    except FileNotFoundError:
        print("Directorio no encontrado.")
        return None

directorio = '/Users/julia/OneDrive/Documentos/UTP_stuff/8_semestre/Compiladores/PL0/test1'
archivo = buscarFicheros(directorio)

if archivo is not None:
    test = os.path.join(directorio, archivo)
    with open(test, "r", encoding="utf-8") as fp:
        cadena = fp.read()

    analizador = PL0Lex()
    analizador.tokenize(cadena)

    for tok in analizador.tokenize(cadena):
        print(tok)