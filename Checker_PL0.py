from Parser_PL0 import *

txt = " "
cont = 0

def incrementarContador():
    global cont
    cont += 1
    return "%d" % cont

class Nodo():
    pass

class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def print_Nodo(self, ident):
        print(ident + "nodo nulo")

    def translate(self):
        global txt
        Nodo_id = incrementarContador()
        txt += Nodo_id + "[label= " + "nodo_nulo" + "]" + "\n\t"
        return Nodo_id

class Program(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        Nodo_id = incrementarContador()
        son1 = self.son1.translate()
        txt += Nodo_id + "[label= " + self.name + "]" + "\n\t"
        txt += Nodo_id + "->" + son1 + "\n\t"
        return "digraph G {\n\t" + txt + "}"

class Block(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def print_Nodo(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].print_Nodo(" " + ident)
        else:
            self.son1.print_Nodo(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].print_Nodo(" " + ident)
        else:
            self.son2.print_Nodo(" " + ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].print_Nodo(" " + ident)
        else:
            self.son3.print_Nodo(" " + ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].print_Nodo(" " + ident)
        else:
            self.son4.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        Nodo_id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].translate()
        else:
            son1 = self.son1.translate()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].translate()
        else:
            son2 = self.son2.translate()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].translate()
        else:
            son3 = self.son3.translate()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].translate()
        else:
            son4 = self.son4.translate()

        txt += Nodo_id + "[label= " + self.name + "]" + "\n\t"
        txt += Nodo_id + " -> " + son1 + "\n\t"
        txt += Nodo_id + " -> " + son2 + "\n\t"
        txt += Nodo_id + " -> " + son3 + "\n\t"
        txt += Nodo_id + " -> " + son4 + "\n\t"

        return Nodo_id

class constDecl(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        if isinstance(self.son1, tuple):
            son1 = self.son1[0].translate()
        else:
            son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id


class constAssignmentList1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        self.son3.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class constAssignmentList2(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        self.son3.print_Nodo(" " + ident)
        self.son4.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id


class varDecl1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
class identList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class identList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class procDecl1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def print_Nodo(self, ident):

        if isinstance(self.son1, tuple):
            self.son1[0].print_Nodo(" " + ident)
        else:
            self.son1.print_Nodo(" " + ident)

        self.son2.print_Nodo(" " + ident)
        self.son3.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class statement1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        self.son3.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id
class statement2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class statement3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class statement4(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        if isinstance(self.son2, tuple):
            self.son2[0].print_Nodo(" " + ident)
        else:
            self.son2.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement5(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        if isinstance(self.son2, tuple):
            self.son2[0].print_Nodo(" " + ident)
        else:
            self.son2.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statementList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class statementList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
class condition1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class condition2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        self.son3.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class relation1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class expression1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
class expression2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class expression3(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        self.son3.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class addingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class addingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class term1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class term2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)
        self.son2.print_Nodo(" " + ident)
        self.son3.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id
class multiplyingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class multiplyingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_Nodo(self, ident):
        self.son1.print_Nodo(" " + ident)

        print(ident + "Nodo: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class Id(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "ID: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class Assign(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):

        print(ident + "Assign: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class NE(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "NE: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class LT(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "LT: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class GT(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "GT: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class LTE(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "LTE: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class GTE(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "GTE: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Plus(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "Plus: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Minus(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "Minus: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Times(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "Times: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Divide(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "Divide: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Update(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "Update: " + self.name)

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Number(Nodo):
    def __init__(self, name):
        self.name = name

    def print_Nodo(self, ident):
        print(ident + "Number: " + str(self.name))

    def translate(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

