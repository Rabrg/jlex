from jlex.type import Type
from jlex.token import Token
import re


class LexicalError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def lex(input):
    tokens = list()
    index = 0
    while index < len(input):
        token = seperate_token(input, index)
        if token is None:
            break
        index = token.end
        tokens.append(token)
    if index != len(input):
        # raise LexicalError(input, 'Lexical error at position ' + str(index))
        print("Shit")
    return tokens


def seperate_token(input, begin):
    if begin < 0 or begin >= len(input):
        raise IndexError(input, 'Index out of bounds: ' + begin)
    for type in Type:
        pattern = r'.{' + str(begin) + '}' + type.value
        match = re.match(pattern, input, re.DOTALL)
        if match:
            lexema = match.group(1)
            return Token(begin, begin + len(lexema), lexema, type)
    return None


if __name__ == '__main__':
    with open('../res/Test.java', 'r') as file:
        input = file.read()
    print('Input:\n', input)
    tokens = lex(input)
    output = str()
    for token in tokens:
        output += token.value
        print(token)
    # print('Output:\n', output)
