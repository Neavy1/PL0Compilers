import re
import codecs
import os
import sys
import keywords
import sly
import sly.lex as lex

class Lexer(sly.lexer):
    tokens = ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
            'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
            'LPARENT', 'RPARENT', 'COMMA', 'SEMICOLON',
            'DOT', 'UPDATE'
            ]

    reservadas = {
        'begin': 'BEGIN',
        'end': 'END',
        'if': 'IF',
        'then': 'THEN',
        'while': 'WHILE',
        'do': 'DO',
        'call': 'CALL',
        'const': 'CONST',
        'int': 'INT',
        'procedure': 'PROCEDURE',
        'out': 'OUT',
        'in': 'IN',
        'else': 'ELSE'
    }

    tokens = tokens + list(reservadas.values())

    t_ignore = '\t'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_ODD = r'ODD'
    t_ASSIGN = r'='
    t_NE = r'<>'
    t_LT = r'<'
    t_LTE = r'<='
    t_GT = r'>'
    t_GTE = r'>='
    t_LPARENT = r'\('
    t_RPARENT = r'\)'
    t_COMMA = r','
    t_SEMICOLON = r';'
    t_DOT = r'\.'
    t_UPDATE = r';='

    @(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def t_ID(t):
        t.type = reservadas.get(t.value.upper(), 'ID')
        return t

    @(r'\#.*')
    def t_COMMENT(t):
        pass

    @(r'\d+')
    def t_NUMBER(t):
        t.value = int(t.value)
        return t

    def t_error(t):
        print("Carácter ilegal '%s'" % t.value[0])
        t.lexer.skip(1)

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
                print("Has escogido \"%s\"\n" % archivo_seleccionado)
                return archivo_seleccionado
            else:
                print("Número de archivo fuera de rango.")
                return None

        except FileNotFoundError:
            print("Directorio no encontrado.")
            return None

    directorio = '/Users/julia/OneDrive/Documentos/UTP_stuff/8_semestre/Compiladores/PL0/Analizador_Lexico/test1'
    archivo = buscarFicheros(directorio)

    if archivo is not None:
        test = os.path.join(directorio, archivo)
        with open(test, "r", encoding="utf-8") as fp:
            cadena = fp.read()

        analizador = lex.lex()
        analizador.input(cadena)

        while True:
            tok = analizador.token()
            if not tok:
                break
            print(tok)
