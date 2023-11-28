import os
from sly import Parser
from Nodes import *
from Lexer_PL0 import PL0Lex
import codecs

class PL0Par(Parser):
    tokens = PL0Lex.tokens
    
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'UMINUS'),
    )
    
    def __init__(self):
        self.names = { }
        self.errors = [ ]
    
    @_("functions")
    def program(self, p):
        return Program(p.functions)
    
    @_("function")
    def functions(self, p):
        return [p.function]
    
    @_("function functions")
    def functions(self, p):
        return [p.function] + p.functions
    
    @_("FUN ID '(' args ')' locals statements_block")
    def function(self, p):
        return Function(p.ID, p.args, p.locals, p.statements_block)
    
    @_("var_declaration")
    def locals(self, p):
        return [p.var_declaration]
    
    @_("var_declaration ';' locals")
    def locals(self, p):
        return [p.var_declaration] + p.locals
    
    @_("var_declaration")
    def args(self, p):
        return [p.var_declaration]
    
    @_("var_declaration ',' args")
    def args(self, p):
        return [p.var_declaration] + p.args
    
    @_("")
    def args(self, p):
        return []
    
    @_('ID ":" RNUM_TYPE')
    def var_declaration(self, p):
        return SimpleVariable(p.ID, p.RNUM_TYPE)
    
    @_('"*" ID ":" RNUM_TYPE')
    def var_declaration(self, p):
        return PointerVariable(p.ID, p.RNUM_TYPE)
    
    @_('ID ":" INUM_TYPE')
    def var_declaration(self, p):
        return SimpleVariable(p.ID, p.INUM_TYPE)
    
    @_('"*" ID ":" INUM_TYPE')
    def var_declaration(self, p):
        return PointerVariable(p.ID, p.INUM_TYPE)
    
    @_('ID ":" RNUM_TYPE "[" RNUM "]"')
    def var_declaration(self, p):
        return PointerVariable(p.ID, p.RNUM_TYPE, p.RNUM)
    
    @_('ID ":" INUM_TYPE "[" INUM "]"')
    def var_declaration(self, p):
        return PointerVariable(p.ID, p.INUM_TYPE, p.INUM)
    
    @_("BEGIN statements END")
    def statements_block(self, p):
        return StatementsBlock(p.statements)
    
    @_("statement ';' statements")
    def statements(self, p):
        return [p.statement] + p.statements
    
    @_("BEGIN statements END")
    def statements_block(self, p):
        return StatementsBlock(p.statements)
    
    @_('BEGIN statements END')
    def statement(self, p):
        return p.statements

    @_("statement")
    def statements(self, p):
        return [p.statement]
    
    @_("statement")
    def statements(self, p):
        return StatementsBlock([p.statement])
    
    @_('ID ASSING expr')
    def statement(self, p):
        self.names[p.ID] = p.expr
    
    @_('ID "(" [ arglist ] ")"')
    def statement(self, p):
        return (p.ID, p.arglist)
    
    @_("conditional_block")
    def statement(self, p):
        return p.conditional_block
    
    @_("NAME ASSIGN expression")
    def statement(self, p):
        return Assignment(SimpleLocation(p.NAME), p.expression)

    @_("NAME '[' INTEGER ']' ASSIGN expression")
    def statement(self, p):
        return Assignment(VectorLocation(p.NAME, p.integer), p.expression)

    @_("PRINT '(' STRING ')'")
    def statement(self, p):
        return Print(String(p.STRING.replace('"', '')))

    @_("WRITE '(' expression ')'")
    def statement(self, p):
        return Write(p.expression)

    @_("READ '(' NAME ')'")
    def statement(self, p):
        return Read(SimpleLocation(p.NAME))

    @_("RETURN expression")
    def statement(self, p):
        return Return(p.expression)
    
    @_('expr { COMMA expr }')
    def arglist(self, p):
        return [p.expr0, *p.expr1]

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER
    
    @_('statement SEMICOLON')
    def statement(self, p):
        return p.statement
    
    @_("expression '+' expression")
    def expression(self, p):
        return Binop(p[1], p.expression0, p.expression1)
    
    @_("expression '-' expression")
    def expression(self, p):
        return Binop(p[1], p.expression0, p.expression1)
    
    @_("expression '*' expression")
    def expression(self, p):
        return Binop(p[1], p.expression0, p.expression1)
    
    @_("expression '/' expression")
    def expression(self, p):
        return Binop(p[1], p.expression0, p.expression1)
    
    @_("expression EQ expression")
    def expression(self, p):
        return Binop(p[1], p.expression0, p.expression1)
    
    @_("'-' expression %prec UMINUS")
    def expression(self, p):
        return Unop(p[0], p.expression)
    
    @_("'+' expression %prec UMINUS")
    def expression(self, p):
        return Unop(p[0], p.expression)
    
    @_("'(' expression ')'")
    def expression(self, p):
        return p.expression
    
    @_("NAME")
    def expression(self, p):
        return ReadLocation(SimpleLocation(p.NAME))
    
    @_("NAME '[' INTEGER ']'")
    def expression(self, p):
        return ReadLocation(PointerLocation(p.NAME, p.INTEGER))
    
    @_("NAME '(' expression_list ')'")
    def expression(self, p):
        return FunctionCall(p.NAME, p.expression_list)
    
    @_("literal")
    def expression(self, p):
        return p.literal
    
    @_("RNUM")
    def literal(self, p):
        return RNUM(p.INTEGER)

    @_("INUM")
    def literal(self, p):
        return INUM(p.FLOAT)

    @_("STRING")
    def literal(self, p):
        return String(p.STRING.value.replace('"', ''))
    
    @_("RNUM_TYPE '(' expression ')'")
    def expression(self, p):
        return Map(p[0], p.expression)
    
    @_("INUM_TYPE '(' expression ')'")
    def expression(self, p):
        return Map(p[0], p.expression)
    
    @_("BREAK")
    def statement(self, p):
        return Break()
    
    @_("PRINT '(' STRING ')'")
    def statement(self, p):
        return Print(String(p.STRING.replace('"', '')))
    
    @_("WRITE '(' expression ')'")
    def statement(self, p):
        return Write(p.expression)

    @_("READ '(' NAME ')'")
    def statement(self, p):
        return Read(SimpleLocation(p.NAME))

    @_("RETURN expression")
    def statement(self, p):
        return Return(p.expression)
    
    @_("WHILE relation DO statement")
    def conditional_block(self, p):
        return While(p.relation, p.statement)

    @_("IF relation THEN statement")
    def conditional_block(self, p):
        return If(p.relation, p.statement)

    @_("IF relation THEN statement ELSE statement")
    def conditional_block(self, p):
        return If(p.relation, p.statement0, p.statement1)
    
    @_("'(' expression '<' expression ')'")
    def relation(self, p):
        return BinRel(p[2], p.expression0, p.expression1)
    
    @_("'(' expression <= expression ')'")
    def relation(self, p):
        return BinRel(p[2], p.expression0, p.expression1)
    
    @_("'(' expression '>' expression ')'")
    def relation(self, p):
        return BinRel(p[2], p.expression0, p.expression1)
    
    @_("'(' expression >= expression ')'")
    def relation(self, p):
        return BinRel(p[2], p.expression0, p.expression1)
    
    @_("'(' expression == expression ')'")
    def relation(self, p):
        return BinRel(p[2], p.expression0, p.expression1)
    
    @_("'(' expression != expression ')'")
    def relation(self, p):
        return BinRel(p[2], p.expression0, p.expression1)

    @_("NOT relation")
    def relation(self, p):
        return UnRel(p[0], p.relation)

    @_("'(' relation AND relation ')'")
    def relation(self, p):
        return ConditionNode(p[2], p.relation0, p.relation1)
    
    @_ ("'(' relation OR relation ')'")
    def relation(self, p):
        return ConditionNode(p[2], p.relation0, p.relation1)


    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            self.errors.append(('undefined', p.ID))
            return 0

    def error(self, p):
        if p:
            print("Syntax error at token", p.type)
            print(p)
        else:
            print("Syntax error at EOF")
        

def buscarFicheros(directorio):
    try:
        ficheros = []
        cont = 1

        for base, dirs, files in os.walk(directorio):
            ficheros.extend(files)

        for file in ficheros:
            print(f"{cont}. {file}")
            cont += 1

        respuesta = False
        while not respuesta:
            numArchivo = input('\nNúmero del test: ')
            try:
                numArchivo = int(numArchivo)
                if 0 < numArchivo <= len(ficheros):
                    respuesta = True
                else:
                    print("Número de archivo fuera de rango.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        archivo_seleccionado = ficheros[numArchivo - 1]
        print(f'Has escogido "{archivo_seleccionado}"\n')
        return archivo_seleccionado
    
    except FileNotFoundError:
        print("Directorio no encontrado.")
        return None
    
def traducir(result):
    graphFile = open('graphviztrhee.vz', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print("El programa traducido se guardo en \"graphviztrhee.vz\"")

directorio = '/Users/julia/OneDrive/Documentos/UTP_stuff/8_semestre/Compiladores/PL0/test1'
archivo = buscarFicheros()
test = os.path.join(directorio, archivo)
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

'''
    @_('statement SEMICOLON')
    def statement(self, p):
        

    @_('BEGIN statement END')
    def statement(self, p):
        pass

    @_('expression')
    def statement(self, p):
        pass

    @_('IDENTIFIER BECOMES expression')
    def statement(self, p):
        pass

    @_('IF condition THEN statement')
    def statement(self, p):
        pass

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        pass

    @_('WHILE condition DO statement')
    def statement(self, p):
        pass

    @_('CALL IDENTIFIER')
    def statement(self, p):
        pass

    @_('READ IDENTIFIER')
    def statement(self, p):
        pass

    @_('WRITE expression')
    def statement(self, p):
        pass

    @_('expression')
    def condition(self, p):
        pass

    @_('ODD expression')
    def condition(self, p):
        pass

    @_('expression relation expression')
    def condition(self, p):
        pass

    @_('expression PLUS term')
    def expression(self, p):
        pass

    @_('expression MINUS term')
    def expression(self, p):
        pass

    @_('term')
    def expression(self, p):
        pass

    @_('term TIMES factor')
    def term(self, p):
        pass

    @_('term SLASH factor')
    def term(self, p):
        pass

    @_('factor')
    def term(self, p):
        pass

    @_('PLUS factor')
    def factor(self, p):
        pass

    @_('MINUS factor')
    def factor(self, p):
        pass

    @_('NUMBER')
    def factor(self, p):
        pass

    @_('LPAREN expression RPAREN')
    def factor(self, p):
        pass

    @_('IDENTIFIER')
    def factor(self, p):
        pass

    @_('IDENTIFIER LPAREN RPAREN')
    def factor(self, p):
        pass
    '''