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

    # problem z operacjami takimi jak <
    # bo nie mamy typu Boolean
    def visit_BinExpr(self, node):
        left_symbol = self.visit(node.left)     # type1 = node.left.accept(self)
        right_symbol = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        type_left = type(left_symbol)
        type_right = type(right_symbol)
        if(type_left != type_right):
            # operacja ze skalarem
            if(type_right != MatrixSymbol):
                print("bad types for binExpr")
                return None
            # sprawdzic poprawnosc wynikow dzialan, rozmiar tablic itp
        if(type_left == MatrixSymbol):
            if( op != "*" and 
                left_symbol.width == right_symbol.width and
                left_symbol.height == right_symbol.height):
                return left_symbol
            elif( op == "*" and
                left_symbol.width == right_symbol.height):
                return MatrixSymbol(left_symbol.height,right_symbol.width)
        else:
            math_op = {"+","-","*","/"}
            if(op in math_op):  
                return left_symbol
        

        
        # print(op)
        # wszystko jest poprawne??
        # dodac sprawdzanie czy left ma taki sam typ, rozmiar co right

    # i tutaj chyba bedzie trzeba pododawac sprawdzanie wszystkiego
    # czyli np czy uzywamy zmiennej ktora jest w scopie
    # czy macierz ma dobre wymiary itd.
    # to na dole oczywiscie nie jest do konca poprawne

    # pewnie trzeba dodac wszedzie sprawdzania czy wartosc dla
    # ID istnieje w SymbolTable
    def visit_Assign(self,node):
        id_value = None
        if(node.assignType != "="):
            id_value = take_id_value(node.left)
            if id_value == None:
                print("assignment to non-ID node")
                return None
            else:
                pass
        # node.assignType = {'=', '+=', '-=', '*=', '/='}
        left = node.left.name
        right = self.visit(node.right)
        # print(type(right))

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

    def visit_MatrixSpecialMethod(self,node):
        # method = node.method
        size = self.visit(node.size)
        if isinstance(size, IntNumSymbol):
            if node.size.value <= 0:
                print("argument for matrix special method must be positive integer")
                return None
            else:
                return MatrixSpecialMethodSymbol(node.method,size)
        else:
            print("bad argument for matrix special method")
            return None


    def visit_IntNum(self,node):
        return IntNumSymbol()

    def visit_FloatNum(self,node):
        return FloatNumSymbol()

    def visit_String(self,node):
        return StringSymbol()

    # chyba fajnie bedzie jak bedzie zwracał nie IdSymbol, a wartosc
    # pod nim czyli np IntNumSymbol
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
        # trzeba dodac do symbol table Id, tylko z jaka wartoscia?
        self.visit(node.firstIndex)
        self.visit(node.secondIndex)
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        # id_type = take_id_value(node.id)
        symbol_table.put(node.id.name,IdSymbol(node.id.name, id_type))
        self.visit(node.expr)
        symbol_table = symbol_table.getParentScope()

    def visit_If(self,node):
        # TODO
        print("if")
        condition = self.visit(node.condition)
        ifTrue = self.visit(node.ifTrue)
        # ifFalse = self.visit(node.ifFalse)
        if(condition == None):
            print("bad condition for if")
        pass

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
        return return_value
        
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
