class Token:

    def __init__(self, t, v):
        self.t = t
        self.v = v

    def __str__(self):
        return self.t.name + '<' + self.v + '>'

    __repr__ = __str__
