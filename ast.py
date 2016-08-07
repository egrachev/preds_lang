from operator import eq as op_eq, and_ as op_and


class Expression(object):
    pass


class Literal(Expression):
    def __init__(self, value):
        self.value = value


class Variable(Expression):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Pred(Expression):
    def __init__(self, op, a, b):
        self.op = op
        self.a = a
        self.b = b


class If(Expression):
    def __init__(self, pred, body):
        self.pred = pred
        self.body = body









