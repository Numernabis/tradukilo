import sys
import numpy as np
import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
sys.setrecursionlimit(10000)

class Interpreter(object):
    global bin_op
    bin_op = {
        '*': lambda a, b : a * b,
        '-': lambda a, b : a - b,
        '+': lambda a, b : a + b,
        '/': lambda a, b : a / b,
        '<': lambda a, b : a < b,
        '>': lambda a, b : a > b,
        '<=': lambda a, b : a <= b,
        '>=': lambda a, b : a >= b,
        '==': lambda a, b : a == b,
        '!=': lambda a, b : a != b,
    }

    global dotadd
    def dotadd(a,b, minus):
        matrix = a
        for i in range(0,len(a)):
            for j in range(0,len(a[i])):
                if (minus):
                    matrix[i][j] = a[i][j] - b[i][j]
                else:
                    matrix[i][j] = a[i][j] + b[i][j]
        return matrix

    global dotmul
    def dotmul(a,b, division):
        if (division):
            b = np.transpose(b)
        return np.matmul(a,b)

    global dot_op
    dot_op = {
        '.*': lambda a, b : dotmul(a,b, False),
        '.-': lambda a, b : dotadd(a,b, True),
        '.+': lambda a, b : dotadd(a,b, False),
        './': lambda a, b : dotmul(a,b, True),
    }

    global re_assign_op
    re_assign_op = {
        '*=': lambda a, b : a * b,
        '-=': lambda a, b : a - b,
        '+=': lambda a, b : a + b,
        '/=': lambda a, b : a / b,
    }

    def __init__(self): # memory name
        self.memory_stack = MemoryStack()

    @on('node')
    def visit(self, node):
        pass

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = self.visit(node.left)
        r2 = self.visit(node.right)
        if (node.op in bin_op):
            return bin_op.get(node.op)(r1,r2)
        else:
            return None

    @when(AST.DotExpr)
    def visit(self, node):
        r1 = self.visit(node.left)
        r2 = self.visit(node.right)
        if (node.op in dot_op):
            return dot_op.get(node.op)(r1,r2)
        else:
            return None

    global visit_Assign_Ref
    def visit_Assign_Ref(self, node):
        left = node.left
        right = self.visit(node.right)
        assignType = node.assignType
        id = left.id.name
        matrix = self.memory_stack.get(id)
        firstIndex = self.visit(left.firstIndex)
        secondIndex = self.visit(left.secondIndex)
        if (assignType == '='):
            matrix[firstIndex][secondIndex] = right
            self.memory_stack.insert(id, matrix)
        elif assignType in re_assign_op:
            newValue = re_assign_op.get(assignType)(matrix[firstIndex][secondIndex],right)
            matrix[firstIndex][secondIndex] = newValue
            self.memory_stack.insert(id, matrix)
        else:
            return None

    @when(AST.Assign)
    def visit(self, node):
        if(type(node.left) == AST.Ref):
            return visit_Assign_Ref(self, node)
        right = self.visit(node.right)
        name = node.left.name
        assignType = node.assignType
        if (assignType == '='):
            self.memory_stack.insert(name, right)
        elif assignType in re_assign_op:
            idValue = self.memory_stack.get(name)
            newValue = re_assign_op.get(assignType)(idValue,right)
            self.memory_stack.insert(name, newValue)
        else:
            return None
    

    @when(AST.MatrixSpecialMethod)
    def visit(self, node):
        method = node.method
        size = node.size.value
        if method == "zeros":
            return np.zeros((size,size))
        elif method == "ones":
            return np.ones((size,size))
        elif method == "eye":
            return np.eye(size)
        else:
            return None

    @when(AST.Transpose)
    def visit(self, node):
        matrix = self.visit(node.expr)
        return np.transpose(matrix)

    @when(AST.UMinus)
    def visit(self, node):
        return self.visit(node.expr)*(-1)

    @when(AST.IntNum)
    def visit(self,node):
        return node.value

    @when(AST.FloatNum)
    def visit(self,node):
        return node.value

    @when(AST.String)
    def visit(self,node):
        return node.value

    @when(AST.Id)
    def visit(self, node):
        return self.memory_stack.get(node.name)

    @when(AST.Matrix)
    def visit(self, node):
        matrix = []
        for row in node.rows:
            matrix_row = []
            for cell in row:
                matrix_row.append(cell.value)
            matrix.append(matrix_row)
        return matrix

    @when(AST.Block)
    def visit(self, node):
        self.memory_stack.push(Memory("block"))
        for expr in node.exprs:
            self.visit(expr)
        self.memory_stack.pop()

    @when(AST.While)
    def visit(self, node):
        self.memory_stack.push(Memory("while"))
        while self.visit(node.condition):
            try:
                self.visit(node.ifTrue)
            except BreakException:
                # bo block tworzy wlasny scope
                if type(node.ifTrue) == AST.Block:
                    self.memory_stack.pop()
                break
            except ContinueException:
                continue
        self.memory_stack.pop()

    @when(AST.For)
    def visit(self, node):
        self.memory_stack.push(Memory("for"))
        firstIndex = self.visit(node.firstIndex)
        secondIndex = self.visit(node.secondIndex)
        for value in range(firstIndex, secondIndex):
            self.memory_stack.insert(node.id.name, value)
            try:
                self.visit(node.expr)
            except BreakException:
                if type(node.expr) == AST.Block:
                    self.memory_stack.pop()
                break
            except ContinueException:
                continue
        self.memory_stack.pop()

    @when(AST.If)
    def visit(self, node):
        if self.visit(node.condition):
            self.visit(node.ifTrue)
        else:
            self.visit(node.ifFalse)

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Print)
    def visit(self,node):
        for cell in node.cells:
            toPrint = self.visit(cell)
            print(toPrint)

    @when(AST.Return)
    def visit(self, node):
        toReturn = self.visit(node.expr)
        print("return " + str(toReturn))
        sys.exit(toReturn)

    @when(AST.Ref)
    def visit(self, node):
        id = self.visit(node.id)
        index1 = self.visit(node.firstIndex)
        index2 = self.visit(node.secondIndex)
        return id[index1][index2]
