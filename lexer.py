import re

from models import Token


class LexerError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """
    def __init__(self, pos):
         Exception.__init__(self,"Lexer error at position {}".format(pos)) 

rules = [
    ('\d+',             'NUMBER'),
    ('[&%a-zA-Z_]\w+|[a-zA-Z_]',    'IDENTIFIER'),
    ('\+',              'PLUS'),
    ('\-',              'MINUS'),
    ('\*',              'MULTIPLY'),
    ('\/(?!\/)',        'DIVIDE'),
    ('\(',              'LP'),
    ('\)',              'RP'),
    ('\{',              'LB'),
    ('\}',              'RB'),
    ('\;',              'EOL'),
    ('\=',              'EQUALS'),
    ('\"(\\.|[^\"])*\"','STRING'),
    (',',               'SEPERATOR'),
    ('\/\/.*$',         'COMMENT'),

]

rules = [(re.compile(regex,re.MULTILINE),type) for regex, type in rules]
re_ws_skip = re.compile('\S')

def lexer(input:str, skip_whitespace:bool = True):
    tokens = []
    pos = 0
    while pos < len(input):
        if skip_whitespace:
                match = re_ws_skip.search(input, pos)

                if match:
                    pos = match.start()
                else:
                    return None

        matches = [re.match(input,pos) for re,_ in rules]
        try:
            match = [(match, rules[idx][1]) for idx,match in enumerate(matches) if match][0]
        except IndexError as e:
            print(input[pos])
            raise LexerError(pos)
        
        if match[1] is not 'COMMENT':
            tokens.append(Token(match[1],match[0].group(0)))
        pos = match[0].end()

    return tokens
