#!/usr/bin/python
import pandas as pd

class Symbol(object):
    pass

class VariableSymbol(Symbol):
    def __init__(self, name, type):
        self.name = name
        self.type = type

class IdSymbol(Symbol):
    def __init__(self, name, type):
        # wczesniejszy Id w AST nie ma type
        self.name = name
        self.type = type

class MatrixSymbol(Symbol):
    def __init__(self, width, height, type):
        self.width = width
        self.height = height
        self.type = type

class MatrixSpecialMethodSymbol(Symbol):
    def __init__(self, method, size):
        self.method = method
        self.size = size

class PrintSymbol(Symbol):
    pass
    
# chyba nie potrzebne
class AssignSymbol(Symbol):
    pass

class IfSymbol(Symbol):
    pass
# chyba lepiej bedzie zwracac  IntNumSymbol lub cos takiego
class BinExprSymbol(Symbol):
    def __init__(self, resultType):
        self.resultType = resultType

class IntNumSymbol(Symbol):
    pass

class FloatNumSymbol(Symbol):
    pass

class StringSymbol(Symbol):
    pass



# luzna koncepcja SymbolTable. Ma ona chyba zawierac nazwe zmiennej lub funkcji
# oraz jej instancje jako Symbol. Ponizej link do rysunku, ktory ma troche sensu
# https://www.javatpoint.com/data-structure-for-symbol-table
class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        if name == 'global':
            self.parent = self
        else:
            self.parent = parent
        self.name = name
        self.table = pd.DataFrame(
            data = { 'name': [''], 'symbol': [Symbol()] }
        )

    def put(self, name, symbol):
        # put variable symbol or fundef under <name> entry
        # powinno usuwac wczesniejsza wartosc jesli istnieje
        # table = self.table
        self.table = self.table[self.table.name != name]
        self.table = self.table.append(
            { 'name': name, 'symbol': symbol },
            ignore_index = True
        )

    def get(self, name):
        # get variable symbol or fundef from <name> entry
        try:
            return self.table.loc[self.table['name'] == name].iloc[0]['symbol']
        except:
            return None

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        return SymbolTable(self,name)

    def popScope(self):
        return self.parent
