class Token:

    def __init__(self, begin, end, value, type):
        self.begin = begin
        self.end = end
        self.value = value
        self.type = type

    def __str__(self):
        return self.type.name + '\t[' + str(self.begin) + ':' + str(self.end) + ']\t' + self.value

    __repr__ = __str__
