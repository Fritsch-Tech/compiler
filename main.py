from lexer import lexer
def compiler(input_path:str):
    with open(input_path,"r") as f:
        for token in lexer(f.read()):
            print(token)
if __name__ == "__main__":
    compiler("test.c")