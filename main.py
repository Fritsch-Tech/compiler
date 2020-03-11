from lexer import lexer
from parser import parser


def compiler(input_path:str):
    print_tokens = True

    with open(input_path,"r") as f:
        tokens = lexer(f.read())
    
    if print_tokens:
        for token in tokens:
            print(token)
    
    print(parser(tokens))
        
if __name__ == "__main__":
    compiler("tests/operations.c")