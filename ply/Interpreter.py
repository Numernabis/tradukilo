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
            # TODO: transpose b
            print('division')
        # TODO - implement proper multiplication
        pass

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
        if(node.op in bin_op):
            return bin_op.get(node.op)(r1,r2)
        else:
            return None

    @when(AST.DotExpr)
    def visit(self, node):
        r1 = self.visit(node.left)
        r2 = self.visit(node.right)
        if(node.op in dot_op):
            return dot_op.get(node.op)(r1,r2)
        else:
            return None

    @when(AST.Assign)
    def visit(self, node):
        right = self.visit(node.right)
        if(node.assignType == '='):
            self.memory_stack.insert(node.left.name, right)
        elif node.assignType in re_assign_op:
            idValue = self.memory_stack.get(node.left.name)
            self.memory_stack.insert(
                node.left.name,
                re_assign_op.get(node.assignType)(idValue,right)
            )
        else:
            return None

    @when(AST.MatrixSpecialMethod)
    def visit(self, node):
        # TODO
        pass

    @when(AST.Transpose)
    def visit(self, node):
        # TODO
        pass

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
        pass

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
        self.memory_stack.push(Memory("while"))
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
        # TODO
        pass

    @when(AST.Ref)
    def visit(self, node):
        # TODO
        pass
