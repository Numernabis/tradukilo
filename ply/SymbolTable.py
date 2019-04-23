#!/usr/bin/python
import pandas as pd

# to ponizej sam dodalem
class Symbol(object):
    pass

class VariableSymbol(Symbol):

    def __init__(self, name, type):
        # pass
        self.name = name
        self.type = type
    #

class IntNumSymbol(Symbol):

    def __init__(self, value):
        # pass
        self.value = value

# luzna koncepcja SymbolTable. Ma ona chyba zawierac nazwe zmiennej lub funkcji
# oraz jej instancje jako Symbol. Ponizej link do rysunku, ktory ma troche sensu
# https://www.javatpoint.com/data-structure-for-symbol-table
class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        if(name == "global"):
            self.parent = self
        else:
            self.parent = parent
        self.name = name
        self.table = pd.DataFrame(data={'name': [], 'symbol': []})
        # pass
    #

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.table = self.table.append({'name': name, 'symbol': symbol}, ignore_index=True)
        print(self.table)
        # pass
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        return self.table.loc[name,'symbol']
        # pass
    
    #

    def getParentScope(self):
        return self.parent
        # pass
    #

    def pushScope(self, name):
        return SymbolTable(self,name)
        # pass
    #

    def popScope(self):
        return self.parent
        # pass
    #

