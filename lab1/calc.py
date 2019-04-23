#!/usr/bin/python

import ply.lex as lex;
import ply.yacc as yacc;

symtab = {}

literals = [ '+','-','*','/','(',')','=' ]

tokens = ( "VAR", "NUMBER");

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
#    line = t.value.lstrip()
#    i = line.find("\n")
#    line = line if i == -1 else line[:i]
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

def t_VAR(t):
    r"[a-zA-Z_]\w*"
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

precedence = (
   ("right", '='),
   ("left", '+', '-'),
   ("left", '*', '/'),
)

def p_error(p):
    print("parsing error\n")

def p_start(p):
    """start : start expr
             | expr"""
    # if   len(p)==2: print("p[1]=", p[1])
    # else:           print("p[2]=", p[2])


def p_expr_number(p):
    """expr : NUMBER"""
    # p[0] = p[1]

def p_expr_var(p):
    """expr : VAR"""
    # val = symtab.get(p[1])
    # if val:
    #     p[0] = val
    # else:
    #     p[0] = 0
    #     print("%s not used\n" %p[1])

def p_expr_assignment(p):
    """expr : VAR '=' expr"""
    # p[0] = p[3]
    # symtab[p[1]] = p[3]

def p_expr_sum(p):
    """expr : expr '+' expr
                  | expr '-' expr"""
    # if   p[2]=='+': p[0] = p[1] + p[3];
    # elif p[2]=='-': p[0] = p[1] - p[3];


def p_expr_mul(p):
    """expr : expr '*' expr
                  | expr '/' expr"""
    # if   p[2]=='*': p[0] = p[1] * p[3];
    # elif p[2]=='/': p[0] = p[1] / p[3];


def p_expr_group(p):
    """expr : '(' expr ')'"""
    # p[0] = p[2]

file = open("plik.txt", "r");

lexer = lex.lex()
parser = yacc.yacc()
text = file.read()
parser.parse(text, lexer=lexer)




