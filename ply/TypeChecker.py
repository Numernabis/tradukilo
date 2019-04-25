#!/usr/bin/python


from SymbolTable import *
from AST import *

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
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

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):
    global symbol_table
    # podana jako argument 1 bo cos trzeba podac do konstruktora
    symbol_table = SymbolTable(1,"global")

    global generate_scope_name
    generate_scope_name = 1
    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        # print(op)
        # wszystko jest poprawne??
        # ... 
        #
    # i tutaj chyba bedzie trzeba pododawac sprawdzanie wszystkiego
    # czyli np czy uzywamy zmiennej ktora jest w scopie
    # czy macierz ma dobre wymiary itd.
    # to na dole oczywiscie nie jest do konca poprawne


    # pewnei trzeba dodac wszedzie sprawdzania czy wartosc dla
    # ID istnieje w SymbolTable
    def visit_Assign(self,node):
        assignType = node.assignType
        if(assignType != "="):
            pass
        else:
            left = node.left.name
            right = node.right
            if isinstance(right,IntNum):
                symbol_table.put(left,IntNumSymbol(right))
            elif isinstance(right, FloatNum):
                symbol_table.put(left,FloatNumSymbol(right))
            elif isinstance(right, String):
                symbol_table.put(left,StringSymbol(right))

    def visit_MatrixSpecialMethod(self,node):
        # type1 = self.visit(node.method)    
        type2 = self.visit(node.size)
        if(isinstance(node.size,IntNum)):
            # niezbyt dziala bo gramatyka nie daje wszystkich
            # mozliwosci, np nie mozna podac zeros(A)
            if(node.size.value <= 0):
                print("bad size of matrix")
            
        # id chyba tylko
        else:
            pass


    def visit_IntNum(self,node):
        pass

    def visit_FloatNum(self,node):
        pass
    
    def visit_String(self,node):
        pass

    def visit_Id(self,node):
        value = take_Id_value(node)
        if value == None:
            print("scope doesnt have my Id")
        pass

    def visit_Matrix(self,node):
        rows = node.rows
        size = -1
        for row in rows:
            if(size == -1):
                size = len(row)
            else:
                if len(row) != size:
                    print("wrong matrix sizeee!")
                    break

    # pewnie cos bardzo podobnego bedzie mial if, while, for
    def visit_Block(self,node):
        global symbol_table
        global generate_scope_name
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        for expr in node.exprs:
            self.visit(expr)
        symbol_table = symbol_table.getParentScope()

    # funkcja bedzie sprawdzala czy node jest
    # ID czy czym innym
    # jak bedzie ID to bedzie przeszukiwala SymbolTree
    # to chyba dziala
    global take_Id_value
    def take_Id_value(node):
        if(isinstance(node,Id)):
            current_symbol_table = symbol_table
            tried = False
            while(tried == False or current_symbol_table.name != "global"):
                what_founded = current_symbol_table.get(node.name)
                if what_founded != None:
                    return what_founded
                if(current_symbol_table.name == "global"):
                    tried = True
                current_symbol_table = current_symbol_table.getParentScope()
            return None
        else:
            return node