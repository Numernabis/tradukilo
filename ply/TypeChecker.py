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
        type1 = self.visit(node.left)     # type1 = node.left.accept(self)
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
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
        id_value = take_id_value(node.left)
        if id_value == None:
            print("assignment to non-ID node")
            return None
        # node.assignType = {'=', '+=', '-=', '*=', '/='}
        left = node.left.name
        right = node.right
        if isinstance(right, IntNum):
            symbol_table.put(left, IntNumSymbol(right))
        elif isinstance(right, FloatNum):
            symbol_table.put(left, FloatNumSymbol(right))
        elif isinstance(right, String):
            symbol_table.put(left, StringSymbol(right))
        elif isinstance(right, Id):
            symbol_table.put(left, IdSymbol(right))
        elif isinstance(right, Matrix):
            symbol_table.put(left, MatrixSymbol(right))
        else:
            print("bad assignment value")
            return None

    def visit_MatrixSpecialMethod(self,node):
        # type1 = self.visit(node.method)
        # type2 = self.visit(node.size)

        if isinstance(node.size, IntNum):
            if node.size.value <= 0:
                print("argument for matrix special method must be positive integer")
                return None
            else:
                return 0 # TODO: co zwracać?
        else:
            print("bad argument for matrix special method")
            return None


    def visit_IntNum(self,node):
        pass

    def visit_FloatNum(self,node):
        pass

    def visit_String(self,node):
        pass

    def visit_Id(self,node):
        value = take_id_value(node)
        if value == None:
            print("no such ID in scope: " + node.name)
        return value

    def visit_Matrix(self,node):
        rows = node.rows
        size = len(rows[0])
        if size = 0:
            print("empty matrix")
            return None
        for row in rows:
            # dodac petle na przechodze po komorkach
            # self.visit(row) # TODO
            type = row[0]
            if len(row) != size:
                print("uncompatible row size, expected: " + size)
                break
        return MatrixSymbol(size, len(rows), type)

    def visit_Block(self,node):
        # global symbol_table
        # global generate_scope_name
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        for expr in node.exprs:
            self.visit(expr)
        symbol_table = symbol_table.popScope()

    def visit_While(self,node):
        # global symbol_table
        # global generate_scope_name
        self.visit(node.condition)
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        self.visit(node.ifTrue)
        symbol_table = symbol_table.popScope()

    def visit_For(self,node):
        # global symbol_table
        # global generate_scope_name
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
        pass

    def visit_Print(self,node):
        # TODO
        pass

    def visit_Return(self,node):
        # TODO
        pass

    def visit_Ref(self,node):
        # TODO
        pass
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
