from jlex.type import Type


class Token:

    def __init__(self, t, v):
        self.t = t
        self.v = v

    def __str__(self):
        if self.t == Type.atom:
            return 'ATOM<' + self.v + '>'
        return self.v

    __repr__ = __str__
