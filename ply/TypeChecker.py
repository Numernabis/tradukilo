#!/usr/bin/python


from SymbolTable import *

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

    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        print(op)
        # ... 
        #
    # i tutaj chyba bedzie trzeba pododawac sprawdzanie wszystkiego
    # czyli np czy uzywamy zmiennej ktora jest w scopie
    # czy macierz ma dobre wymiary itd.
    # to na dole oczywiscie nie jest do konca poprawne
    def visit_Assign(self,node):
        assignType = node.assignType
        if(assignType != "="):
            pass
        else:
            left = node.left.name
            right = node.right.value
            symbol_table.put(left,IntNumSymbol(right))

    def visit_IntNum(self,node):
        pass

    def visit_Variable(self, node):
        pass
        

