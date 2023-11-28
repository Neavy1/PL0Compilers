from dataclasses import dataclass, field
from multimethod import multimeta
from typing import List

class Visitor(metaclass = multimeta):
    pass

@dataclass
class Node:
    def accept(self, v:Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class BlockNode(Node):
    const_declarations: List['ConstDeclarationNode']
    var_declarations: List['VarDeclarationNode']
    procedures: List['ProcedureNode']
    statement: 'StatementNode'

@dataclass
class VarDeclarationNode:
    identifiers: List[str]

@dataclass
class ProcedureNode:
    identifier: str
    block: 'BlockNode'

@dataclass
class StatementNode:
    assignment: 'Assignment'
    call: 'SimpleLocation'
    block: 'StatementsBlock'
    if_statement: 'If'
    while_statement: 'While'

@dataclass
class ConstDeclarationNode:
    identifier: str
    value: int

@dataclass
class Program(Node):
    pass

@dataclass
class Function(Node):
    pass

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Node):
    pass

@dataclass
class Relation(Node):
    pass

@dataclass
class StatementsBlock(Statement):
    statements : List[Statement] = field(default_factory=List)
    
@dataclass
class Location(Statement):
    pass
    
@dataclass
class Assignment(Statement):
	location : Location
	value    : Expression

@dataclass
class Binop(Expression):
    op : str
    left : Expression
    right : Expression
    
@dataclass
class Unop(Expression):
    op    : str
    expr  : Expression
    
@dataclass
class Literal(Expression):
    pass
    
@dataclass
class RNUM(Literal):
    value : float
    
@dataclass
class INUM(Literal):
    value : int
    
@dataclass
class String(Literal):
    value : str
    
@dataclass
class Print(Statement):
    Expression: List[Expression] = field(default_factory=List)
    
@dataclass
class If(Statement):
    expr : Expression
    stmt : Statement

@dataclass
class While(Statement):
    expr : Expression
    stmt : Statement
    
@dataclass
class ReadLocation(Statement):
    location : Location

@dataclass
class SimpleLocation(Location):
	name : str

@dataclass
class Write(Statement):
    expr : Expression
    value : Expression
    
class Map(Expression):
    type  : str
    expr  : Expression
    
@dataclass
class Program(Statement):
    Statement : List[Statement] = field(default_factory=List)
    
@dataclass
class PointerLocation(Location):
    name : str
    index : int
    
@dataclass
class SimpleVariable(Location):
    name : str
    type : str

@dataclass
class PointerVariable(Location):
    name : str
    type : str
    size : int
    
@dataclass
class Read(Statement):
    location : Location

@dataclass
class Write(Statement):
    expr : Expression
    
@dataclass
class Return(Statement):
    expr : Expression
    
@dataclass
class Break(Statement):
    pass

@dataclass
class IfStatementNode:
    condition: 'ConditionNode'
    true_statement: 'StatementNode'
    false_statement: 'StatementNode'
    
@dataclass
class WhileStatementNode:
    condition: 'ConditionNode'
    statement: 'StatementNode'
    
class ConditionNode(Relation):
    op   : str  
    left : Relation
    right: Relation
    
@dataclass
class UnRel(Relation):
    op   : str  ## not
    relation: Relation
    
@dataclass
class BinRel(Relation):
    op   : str  
    left : Expression
    right: Expression
    
@dataclass
class Call(Statement):
    identifier: str
    arguments: List[Expression] = field(default_factory=List)
    
@dataclass
class Arguments(Statement):
    arguments: List[Expression] = field(default_factory=List)
    
@dataclass
class FunctionCall(Statement):
    identifier: str
    arguments: List[Expression] = field(default_factory=List)
    
@dataclass
class Function(Node):
    identifier: str
    block: 'BlockNode'