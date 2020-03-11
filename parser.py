from ASTModels import *
from models import Token


keywords = [
    ('if',''),
    ('else',''),
    ('int',''),
    ('return',''),
]


class ParserError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """
    def __init__(self, token):
         Exception.__init__(self,"Unrecognized Token {}".format(token)) 


def parser(tokens: [Token]) -> Node:
    ast = BaseNode([])

    while tokens:
        tokens, ast.statements = _parse(tokens,ast.statements)

    return ast

def _parse(tokens: [Token], nodes: [Node] = []) -> ([Token],[Node]):
    if not tokens:
        print("EOF")
        return ([],nodes)

    elif tokens[0].type == "EOL":
        return (tokens[1:],nodes)
    
    elif tokens[0].type == "RPAR":
        return (tokens[1:],nodes)

    elif tokens[0].type == "LPAR":
        return _parse(tokens[1:],nodes)
    
    elif tokens[0].type == "NUMBER":
        return (tokens[1:],nodes + [Value("INT",tokens[0].val)])
    
    elif tokens[0].type == "BINOP":
        rem_tokens, right = _parse(tokens[1:])
        if not nodes:
            raise ParserError(nodes)
        nodes[-1] = BinOp(
            left = nodes[-1],
            right = right[0],
            operation = tokens[0].val
        )
        return (rem_tokens,nodes)
    
    raise ParserError(tokens[0]) 

BaseNode(statements=[
    BinOp(
        left=BinOp(
            left=Value(type='INT', value='3'), 
            right=Value(type='INT', value='3'), 
            operation='+'
        ), 
        right=BinOp(
            left=Value(type='INT', value='3'), 
            right=Value(type='INT', value='3'), 
            operation='+'), 
        operation='/')])

BaseNode(statements=[
    BinOp(
        left=BinOp(
            left=Value(type='INT', value='3'), 
            right=[Value(type='INT', value='4')], 
            operation='+'), 
        right=[Value(type='INT', value='3')], 
        operation='/')])


BaseNode(statements=[
    BinOp(
        left=BinOp(
            left=Value(type='INT', value='3'), 
            right=Value(type='INT', value='4'), 
            operation='+'), 
        right=Value(type='INT', value='3'), 
        operation='/')
    ]
)
