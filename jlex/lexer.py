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
        raise LexicalError('Lexical error at position ' + str(index))
    return tokens


def seperate_token(input, begin):
    if begin < 0 or begin >= len(input):
        raise IndexError(input, 'Index out of bounds: ' + begin)
    for type in Type:
        pattern = r'.{' + str(begin) + '}' + type.value
        match = re.match(pattern, input, re.DOTALL)
        if match:
            end = match.end(1)
            if type == Type.STRING_LITERAL or type == Type.CHARACTER_LITERAL:
                end += 1
            return Token(begin, end, input[begin:end], type)
    return None
