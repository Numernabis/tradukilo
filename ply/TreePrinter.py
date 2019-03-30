from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        space = "|    "
        print(indent*space + str(self.value))

    @addToClass(AST.For)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + "FOR")
        self.id.printTree(indent + 1)
        print((indent+1)*space + "RANGE")
        self.firstIndex.printTree(indent + 2)
        self.secondIndex.printTree(indent + 2)
        self.expr.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + "WHILE")
        self.condition.printTree(indent + 1)
        self.ifTrue.printTree(indent + 1)

    @addToClass(AST.If)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + "IF")
        self.condition.printTree(indent + 1)
        print((indent+1)*space + "THEN")
        self.ifTrue.printTree(indent + 2)
        if(self.ifFalse != ""):
            print((indent+1)*space + "ELSE")
            self.ifFalse.printTree(indent + 2)

    @addToClass(AST.Assign)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + str(self.assignType))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Transpose)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + "TRANSPOSE")
        self.expr.printTree(indent + 1)

    @addToClass(AST.UMinus)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + "UMINUS")
        self.expr.printTree(indent + 1)

    @addToClass(AST.BinExpr)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + str(self.op))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Block)
    def printTree(self,indent=0):
        space = "|    "
        for expr in self.exprs:
            expr.printTree(indent)

    @addToClass(AST.Matrix)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + "MATRIX")
        for row in self.rows:
            print((indent+1)*space + "ROW")
            for cell in row:
                 cell.printTree(indent+2)

    @addToClass(AST.MatrixSpecialMethod)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + self.method)
        self.size.printTree(indent + 1)

    @addToClass(AST.ID)
    def printTree(self,indent=0):
        space = "|    "
        print(indent*space + self.name)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass    
        # fill in the body



    # define printTree for other classes
    # ...


