#!/usr/bin/python

from SymbolTable import *
from AST import *

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
         # called if no explicit visitor function exists for a node
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)
# ------------------------------------------------------------------

class TypeChecker(NodeVisitor):
    global symbol_table
    # podana jako argument 1 bo cos trzeba podac do konstruktora
    symbol_table = SymbolTable(1,"global")
    global generate_scope_name
    generate_scope_name = 1

    def visit_BinExpr(self, node):
        left_symbol = self.visit(node.left)
        right_symbol = self.visit(node.right)
        if(left_symbol == None or right_symbol == None):
            print("bad argument(s) for operation")
            return None
        op = node.op
        type_left = type(left_symbol)
        type_right = type(right_symbol)
        if(type_left == type_right):
            if(type_left != MatrixSymbol):
                return type_left
            else:
                if( (op == "+" or op == "-") and 
                    left_symbol.type == right_symbol.type and
                    left_symbol.width == right_symbol.width and
                    left_symbol.height == right_symbol.height):
                    return left_symbol
                elif( op == "*" and
                    left_symbol.type == right_symbol.type and
                    left_symbol.width == right_symbol.height):
                    return MatrixSymbol(left_symbol.height,right_symbol.width,right_symbol.type)
                else:
                    print("bad operation ?")
                    return None

        elif(type_right == MatrixSymbol):
            if( op == "*" and type_left == right_symbol.type):
                return right_symbol
            else:
                print("bad types for operation")
            return None
        else:
            print("bad types for operation")
            return None

    def visit_Assign(self,node):
        id_value = None
        left = node.left.name
        right = self.visit(node.right)
        if(node.assignType != "="):
            id_value = take_id_value(node.left)
            if id_value == None:
                print("assignment to non-ID node")
                return None
            else:
                if(type(id_value) == type(right)):
                    return AssignSymbol()
                else:
                    print("bad assign to already existing Id")
                    return None
        if( isinstance(right, IntNumSymbol) or
            isinstance(right, FloatNumSymbol) or
            isinstance(right, StringSymbol) or
            isinstance(right, IdSymbol) or
            isinstance(right, MatrixSymbol)):
            symbol_table.put(left, right)
        else:
            print("bad assignment value")
            return None
        return AssignSymbol()

    # pewnie da sie uproscic
    def visit_MatrixSpecialMethod(self,node):
        # method = node.method
        size = node.size
        if isinstance(size, IntNum):
            if node.size.value <= 0:
                print("argument for matrix special method must be positive integer")
                return None
            else:
                return MatrixSymbol(size.value,size.value,IntNumSymbol)
        else:
            print("bad argument for matrix special method")
            return None


    def visit_IntNum(self,node):
        return IntNumSymbol()

    def visit_FloatNum(self,node):
        return FloatNumSymbol()

    def visit_String(self,node):
        return StringSymbol()

    def visit_Id(self,node):
        value = take_id_value(node)
        if value == None:
            print("no such ID in scope: " + node.name)
        return value

    def visit_Matrix(self,node):
        rows = node.rows
        size = len(rows[0])
        if size == 0:
            print("empty matrix")
            return None
        matrix_type = type(self.visit(rows[0][0]))
        for row in rows:
            for cell in row:
                cell = self.visit(cell)
                if(cell == None or type(cell) != matrix_type):
                    print("bad matrix cell")
                    return None
            if len(row) != size:
                print("uncompatible row size, expected: " + str(size))
                return None
        return MatrixSymbol(size, len(rows), matrix_type)

    def visit_Block(self,node):
        global symbol_table
        global generate_scope_name
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        for expr in node.exprs:
            self.visit(expr)
        symbol_table = symbol_table.popScope()

    def visit_While(self,node):
        global symbol_table
        global generate_scope_name
        self.visit(node.condition)
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        self.visit(node.ifTrue)
        symbol_table = symbol_table.popScope()

    def visit_For(self,node):
        global symbol_table
        global generate_scope_name
        firstIndex = self.visit(node.firstIndex)
        secondIndex = self.visit(node.secondIndex)
        if(firstIndex == None or secondIndex == None):
            print("bad range for if")
            return None

        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        symbol_table.put(node.id.name,IdSymbol(node.id.name, IntNumSymbol()))
        self.visit(node.expr)
        symbol_table = symbol_table.getParentScope()

    def visit_If(self,node):
        global symbol_table
        global generate_scope_name
        condition = self.visit(node.condition)
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        ifTrue = self.visit(node.ifTrue)
        symbol_table = symbol_table.popScope()
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        ifFalse = self.visit(node.ifFalse)
        symbol_table = symbol_table.popScope()
        if(condition == None):
            print("bad condition for if")
            return None
        if(ifTrue == None):
            print("bad true expr")
            return None
        if(ifFalse == None and node.ifFalse != ""):
            print("bad false expr")
            return None
        return IfSymbol()
        

    def visit_Print(self,node):
        for cell in node.cells:
            cell_value = self.visit(cell)
            if(cell_value == None):
                print("bad print cells")
                return None
        return PrintSymbol()

    def visit_Return(self,node):
        return_value = self.visit(node.expr)
        if(return_value == None):
            print("bad return value")
            return None
        
        
    def visit_Ref(self,node):
        id_value = self.visit(node.id)
        if(id_value == None or type(id_value) != MatrixSymbol):
            print("ref doesnt exist")
            return None
        firstIndex = node.firstIndex
        secondIndex = node.secondIndex

        if(isinstance(firstIndex,IntNum)):
            firstIndex = firstIndex.value
        elif type(self.visit(firstIndex)) == IntNumSymbol:
            firstIndex = 0
        else:
            print("firstIndex doesnt exist")
            return None

        if(isinstance(secondIndex,IntNum)):
            secondIndex = secondIndex.value
        elif type(self.visit(secondIndex)) == IntNumSymbol:
            secondIndex = 0
        else:
            print("secondIndex doesnt exist")
            return None
        if( 0 <= firstIndex < id_value.width and 
            0 <= secondIndex < id_value.height):
            return id_value.type
        print("bad reference to matrix")
        return None
# ------------------------------------------------------------------

    # TODO: nazwy do poprawy, refaktor
    global take_id_value
    def take_id_value(node):
        if isinstance(node, Id):
            current_symbol_table = symbol_table
            tried = False
            while(tried == False or current_symbol_table.name != "global"):
                what_founded = current_symbol_table.get(node.name)
                if what_founded != None:
                    return what_founded
                if current_symbol_table.name == "global":
                    tried = True
                current_symbol_table = current_symbol_table.getParentScope()
            return None
        else:
            return node
# ------------------------------------------------------------------
