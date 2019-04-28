
class Node(object):
    pass

class IntNum(Node):
    def __init__(self, value, line):
        self.value = value
        self.line = line

class FloatNum(Node):
    def __init__(self, value, line):
        self.value = value
        self.line = line

class String(Node):
    def __init__(self, value, line):
        self.value = value
        self.line = line

class Id(Node):
    def __init__(self, name, line):
        self.name = name
        self.line = line

class UMinus(Node):
    def __init__(self, expr, line):
        self.expr = expr
        self.line = line

class Transpose(Node):
    def __init__(self, expr, line):
        self.expr = expr
        self.line = line

class Block(Node):
    def __init__(self, exprs, line):
        self.exprs = exprs
        self.line = line

class MatrixSpecialMethod(Node):
    def __init__(self, method, size, line):
        self.method = method
        self.size = size
        self.line = line

class Matrix(Node):
    def __init__(self, rows, line):
        self.rows = rows
        self.line = line

class BinExpr(Node):
    def __init__(self, op, left, right, line):
        self.op = op
        self.left = left
        self.right = right
        self.line = line

class Assign(Node):
    def __init__(self, assignType, left, right, line):
        self.assignType = assignType
        self.left = left
        self.right = right
        self.line = line

class For(Node):
    def __init__(self, id, firstIndex, secondIndex, expr, line):
        self.id = id
        self.firstIndex = firstIndex
        self.secondIndex = secondIndex
        self.expr = expr
        self.line = line

class While(Node):
    def __init__(self, condition, ifTrue, line):
        self.condition = condition
        self.ifTrue = ifTrue
        self.line = line

class If(Node):
    def __init__(self, condition, ifTrue, ifFalse, line):
        self.condition = condition
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.line = line

class Print(Node):
    def __init__(self, cells, line):
        self.cells = cells
        self.line = line

class Return(Node):
    def __init__(self, expr, line):
        self.expr = expr
        self.line = line

class Ref(Node):
    def __init__(self, id, firstIndex, secondIndex, line):
        self.id = id
        self.firstIndex = firstIndex
        self.secondIndex = secondIndex
        self.line = line

class Break(Node):
    def __init__(self, name, line):
        self.name = name
        self.line = line        

class Continue(Node):
    def __init__(self, name, line):
        self.name = name
        self.line = line

class Error(Node):
    def __init__(self):
        pass
