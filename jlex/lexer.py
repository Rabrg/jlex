from jlex.type import Type
from jlex.token import Token


def get_atom(s, i):
    j = i
    while j < len(s):
        if not s[j].isalpha():
            break
        j += 1
    return s[i:j]


def lex(input):
    result = list()
    i = 0
    while i < len(input):
        c = input[i]
        if c == '(':
            result.append(Token(Type.LPAREN, '('))
            i += 1
        elif c == ')':
            result.append(Token(Type.RPAREN, ')'))
            i += 1
        else:
            if c.isspace():
                i += 1
            else:
                atom = get_atom(input, i)
                i += len(atom)
                result.append(Token(Type.ATOM, atom))
    return result


if __name__ == '__main__':
    input = '(foo (bar))'
    print('Input:', input)
    tokens = lex(input)
    print('Tokens:', tokens)
