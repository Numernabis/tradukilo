#!/usr/bin/python

from SymbolTable import *
from AST import *

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        # return Symbol()
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
    symbol_table = SymbolTable(1, "global")
    global generate_scope_name
    generate_scope_name = 1

    def visit_BinExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if (left == None or right == None):
            print_error("Bad argument(s) for BinExpr", node)
            return None
        op = node.op
        type_left = type(left)
        type_right = type(right)
        if (type_left != MatrixSymbol and type_right != MatrixSymbol):
            return type_left
        elif (type_left == MatrixSymbol and type_right == IntNumSymbol):
            return MatrixSymbol(left.height,left.width,left.type)
        else:
            print_error("Bad types for BinExpr", node)
            return None

    def visit_DotExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if (left == None or right == None):
            print_error("Bad argument(s) for DotExpr", node)
            return None
        op = node.op
        type_left = type(left)
        type_right = type(right)
        if (type_left == MatrixSymbol and type_right == MatrixSymbol):
            if ((op == ".+" or op == ".-") and
                left.type == right.type and
                left.width == right.width and
                left.height == right.height):
                return left
            elif (op == ".*" and
                left.type == right.type and
                left.width == right.height):
                # save Matrix with proper dimensions
                return MatrixSymbol(left.height,right.width,right.type)
            else:
                print_error("Uncompatible dimensions for DotExpr", node)
                return None
        else:
            print_error("Bad types for DotExpr", node)
            return None

    def visit_Assign(self,node):
        id_value = None
        left = node.left
        right = self.visit(node.right)
        if (node.assignType != "="):
            id_value = take_id_value(left)
            if id_value == None:
                print_error("Assigning to not existing ID", node)
                return None
            else:
                if (type(id_value) == type(right)):
                    return AssignSymbol()
                else:
                    print_error("Assigning bad type to existing ID", node)
                    return None
        if (isinstance(right, IdSymbol) or
            isinstance(right, FloatNumSymbol) or
            isinstance(right, StringSymbol) or
            isinstance(right, IntNumSymbol) or
            isinstance(right, RefSymbol) or
            isinstance(right, MatrixSymbol)):
            symbol_table.put(left.name, right)
        else:
            #print_error("Assignment bad value", node)
            return None
        return AssignSymbol()

    def visit_MatrixSpecialMethod(self,node):
        size = node.size
        if isinstance(size, IntNum):
            return MatrixSymbol(size.value, size.value, IntNumSymbol)
        else:
            print_error("Bad argument for matrix special method", node)
            return None

    def visit_Transpose(self,node):
        expr = self.visit(node.expr)
        if(type(expr) != MatrixSymbol):
            print_error("Bad argument for transpose", node)
            return None
        return expr

    def visit_UMinus(self,node):
        expr = self.visit(node.expr)
        if(expr == None):
            print_error("Bad argument for uminus", node)
            return None
        return expr

    def visit_IntNum(self,node):
        return IntNumSymbol()

    def visit_FloatNum(self,node):
        return FloatNumSymbol()

    def visit_String(self,node):
        return StringSymbol()

    def visit_Id(self,node):
        value = take_id_value(node)
        if value == None:
            print_error(node.name + " is not in scope", node)
        return value

    def visit_Matrix(self,node):
        rows = node.rows
        size = len(rows[0])
        if size == 0:
            print_error("Empty matrix", node)
            return None
        matrix_type = type(self.visit(rows[0][0]))
        for row in rows:
            for cell in row:
                cell = self.visit(cell)
                if (cell == None or type(cell) != matrix_type):
                    print_error("Bad matrix cell type", node)
                    return None
            if len(row) != size:
                print_error("Uncompatible row size, expected: " + str(size), node)
                return None
        return MatrixSymbol(size, len(rows), matrix_type)

    def visit_Block(self,node):
        global symbol_table
        global generate_scope_name
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        for expr in node.exprs:
            if self.visit(expr) == None:
                print_error("Bad expr in block", node)
                return None
        symbol_table = symbol_table.popScope()
        return BlockSymbol()

    def visit_While(self,node):
        global symbol_table
        global generate_scope_name
        condition = self.visit(node.condition)
        if(condition == None):
            print_error("Bad condition while loop", node)
        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        ifTrue = self.visit(node.ifTrue)
        symbol_table = symbol_table.popScope()
        if(ifTrue == None):
            print_error("Bad ifTrue while loop",node)
        return WhileSymbol()

    def visit_For(self,node):
        global symbol_table
        global generate_scope_name
        firstIndex = self.visit(node.firstIndex)
        secondIndex = self.visit(node.secondIndex)
        if (firstIndex == None or secondIndex == None):
            print_error("Bad range in for loop", node)
            return None

        symbol_table = symbol_table.pushScope(generate_scope_name)
        generate_scope_name += 1
        symbol_table.put(node.id.name, IdSymbol(node.id.name, IntNumSymbol()))
        expr = self.visit(node.expr)
        symbol_table = symbol_table.getParentScope()
        if(expr == None):
            print_error("Bad expr for loop", node)
            return None
        return ForSymbol()

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
        ifFalse = node.ifFalse
        if(node.ifFalse != ""):
            ifFalse = self.visit(node.ifFalse)
        symbol_table = symbol_table.popScope()
        if (condition == None):
            print_error("Bad condition for if", node)
            return None
        if (ifTrue == None):
            print_error("Bad expr in if", node)
            return None
        if (ifFalse == None and node.ifFalse != ""):
            print_error("Bad expr in else", node)
            return None
        return IfSymbol()


    def visit_Break(self,node):
        return BreakSymbol()

    def visit_Continue(self,node):
        return ContinueSymbol()

    def visit_Print(self,node):
        for cell in node.cells:
            cell_value = self.visit(cell)
            if (cell_value == None):
                print_error("Bad print cells", node)
                return None
        return PrintSymbol()

    def visit_Return(self,node):
        return_value = self.visit(node.expr)
        if (return_value == None):
            print_error("Bad return value", node)
            return None
        return ReturnSymbol()


    def visit_Ref(self,node):
        id_value = self.visit(node.id)
        if (id_value == None or type(id_value) != MatrixSymbol):
            print_error("Reference to not existing variable", node)
            return None
        firstIndex = node.firstIndex
        secondIndex = node.secondIndex

        if (isinstance(firstIndex, IntNum)):
            firstIndex = firstIndex.value
        elif type(self.visit(firstIndex)) == IntNumSymbol:
            firstIndex = 0
        else:
            print_error("Bad reference firstIndex", node)
            return None

        if (isinstance(secondIndex, IntNum)):
            secondIndex = secondIndex.value
        elif type(self.visit(secondIndex)) == IntNumSymbol:
            secondIndex = 0
        else:
            print_error("Bad reference secondIndex", node)
            return None

        if (firstIndex > id_value.width or
            secondIndex > id_value.height):
            print_error("Bad reference to matrix", node)
            return None
        elif (firstIndex < 0 or secondIndex < 0):
            print_error("Negative reference index", node)
            return None
        else:
            return RefSymbol()

# ------------------------------------------------------------------

    global take_id_value
    def take_id_value(node):
        if isinstance(node, Id):
            current_scope = symbol_table
            flag = False
            while (flag == False):
                id_in_scope = current_scope.get(node.name)
                if id_in_scope != None:
                    return id_in_scope
                if current_scope.name == "global":
                    flag = True
                current_scope = current_scope.getParentScope()
            return None
        else:
            return node

    global print_error
    def print_error(msg, node):
        print(msg + " (line " + str(node.line) + ")")
# ------------------------------------------------------------------
