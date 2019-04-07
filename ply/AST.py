
class Node(object):
    pass

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class String(Node):
    def __init__(self, value):
        self.value = value

class Id(Node):
    def __init__(self, name):
        self.name = name

class UMinus(Node):
    def __init__(self, expr):
        self.expr = expr

class Transpose(Node):
    def __init__(self, expr):
        self.expr = expr

class Block(Node):
    def __init__(self, exprs):
        self.exprs = exprs    
    
class MatrixSpecialMethod(Node):
    def __init__(self, method, size):
        self.method = method
        self.size = size

class Matrix(Node):
    def __init__(self, rows):
        self.rows = rows

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Assign(Node):
    def __init__(self, assignType, left, right):
        self.assignType = assignType
        self.left = left
        self.right = right

class For(Node):
    def __init__(self, id, firstIndex, secondIndex, expr):
        self.id = id
        self.firstIndex = firstIndex
        self.secondIndex = secondIndex
        self.expr = expr

class While(Node):
    def __init__(self, condition, ifTrue):
        self.condition = condition
        self.ifTrue = ifTrue

class If(Node):
    def __init__(self, condition, ifTrue, ifFalse = ""):
        self.condition = condition
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse

class Print(Node):
    def __init__(self, cells):
        self.cells = cells

class Return(Node):
    def __init__(self, expr):
        self.expr = expr

class Ref(Node):
    def __init__(self, id, firstIndex, secondIndex):
        self.id = id
        self.firstIndex = firstIndex
        self.secondIndex = secondIndex

class Break(Node):
    def __init__(self, name):
        self.name = name

class Continue(Node):
    def __init__(self, name):
        self.name = name

# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
      
