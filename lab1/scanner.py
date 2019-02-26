#!/usr/bin/python
# Python 2 or 3

import ply.lex as lex

# operatory binarne, nawiasy, operator zakresu, transpozycja macierzy,
# przecinek i srednik  ==> literaly

literals = "=+-*/()[]{}:',;"

# macierzowe operatory binarne
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\.\/'

# operatory przypisania
# t_ASSIGN = r'\='
t_ADDASSIGN = r'\+\='
t_SUBASSIGN = r'-\='
t_MULASSIGN = r'\*\='
t_DIVASSIGN = r'\/\='

# operatory relacyjne
t_GTE = r'\>\='
t_LTE = r'\<\='
t_NEQ = r'\!\='
t_EQ = r'\=\='
t_GT = r'\>'
t_LT = r'\<'

# słowa kluczowe
keywords = {
    'if' : 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}


tokens = [
    'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
    'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'GTE', 'LTE', 'NEQ', 'EQ', 'GT', 'LT',
    'ID', 
    'INTNUM', 'FLOATNUM',
    'STRING'
] + list(keywords.values());

# --------------- --------------- ---------------
# identyfikatory
def t_ID(t):
    r'[a-zA-Z_]\w*'
    # r'\b(?=\w)[a-zA-Z_]\w*'
    t.type = keywords.get(t.value,'ID')
    return t

# liczby zmiennoprzecinkowe
def t_FLOATNUM(t):
    r'[+-]?(\d+\.(\d*)?|\.\d+)([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

# liczby całkowite
def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# stringi
t_STRING = r'\".*\"'

# --------------- --------------- ---------------
# znaki pomijane
# spacje, tabulatory
t_ignore = ' \t'

# znaki nowej linii
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# komentarze
def t_COMMENT(t):
    r'\#.*'
    pass

# --------------- --------------- ---------------

def t_error(t):
    print("line %d: illegal character '%s' '%s'" %(t.lineno, t.value[0], t.value[1]) )
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos)
    return (token.lexpos - line_start)

# ---------------
lexer = lex.lex()
# ---------------
