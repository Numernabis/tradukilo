from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:
    global space
    space = "|  "

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print(indent*space + str(self.value))

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print(indent*space + str(self.value))

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print(indent*space + self.value)

    @addToClass(AST.Id)
    def printTree(self,indent=0):
        print(indent*space + self.name)

    @addToClass(AST.UMinus)
    def printTree(self,indent=0):
        print(indent*space + "UMINUS")
        self.expr.printTree(indent + 1)

    @addToClass(AST.Transpose)
    def printTree(self,indent=0):
        print(indent*space + "TRANSPOSE")
        self.expr.printTree(indent + 1)

    @addToClass(AST.Block)
    def printTree(self,indent=0):
        for expr in self.exprs:
            expr.printTree(indent)

    @addToClass(AST.MatrixSpecialMethod)
    def printTree(self,indent=0):
        print(indent*space + self.method)
        self.size.printTree(indent + 1)

    @addToClass(AST.Matrix)
    def printTree(self,indent=0):
        print(indent*space + "VECTOR")
        for row in self.rows:
            print((indent+1)*space + "VECTOR")
            for cell in row:
                 cell.printTree(indent+2)

    @addToClass(AST.BinExpr)
    def printTree(self,indent=0):      
        print(indent*space + str(self.op))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.DotExpr)
    def printTree(self,indent=0):
        print(indent*space + str(self.op))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Assign)
    def printTree(self,indent=0):
        print(indent*space + str(self.assignType))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self,indent=0):
        print(indent*space + "FOR")
        self.id.printTree(indent + 1)
        print((indent+1)*space + "RANGE")
        self.firstIndex.printTree(indent + 2)
        self.secondIndex.printTree(indent + 2)
        self.expr.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self,indent=0):
        print(indent*space + "WHILE")
        self.condition.printTree(indent + 1)
        self.ifTrue.printTree(indent + 1)

    @addToClass(AST.If)
    def printTree(self,indent=0):
        print(indent*space + "IF")
        self.condition.printTree(indent + 1)
        print(indent*space + "THEN")
        self.ifTrue.printTree(indent + 1)
        if(self.ifFalse != ""):
            print(indent*space + "ELSE")
            self.ifFalse.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self,indent=0):
        print(indent*space + "PRINT")
        #self.cells.printTree(indent + 1)
        for expr in self.cells:
            expr.printTree(indent + 1)

    @addToClass(AST.Return)
    def printTree(self,indent=0):
        print(indent*space + "RETURN")
        self.expr.printTree(indent + 1)

    @addToClass(AST.Ref)
    def printTree(self,indent=0):
        print(indent*space + "REF")
        self.id.printTree(indent + 1)
        self.firstIndex.printTree(indent + 1)
        self.secondIndex.printTree(indent + 1)

    @addToClass(AST.Break)
    def printTree(self,indent=0):
        print(indent*space + self.name)

    @addToClass(AST.Continue)
    def printTree(self,indent=0):
        print(indent*space + self.name)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        raise Exception("Error (bum)")
