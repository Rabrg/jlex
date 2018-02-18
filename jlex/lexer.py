def get_atom(s, i):
    j = i
    while j < len(s):
        if not s[j].isalpha():
            break
        j += 1
    return s.substring(i, j)

# def lex(input):
#     result = list()
#     for i in range(len(input)):
#         c = input[i]
#         if c == '(':
