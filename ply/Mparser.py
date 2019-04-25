#!/usr/bin/python

import scanner
import ply.yacc as yacc
from AST import *

tokens = scanner.tokens

precedence = (
    ("left", 'IF'),   # Dangling-else solution
    ("left", 'ELSE'), 
    ('nonassoc', '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ('nonassoc', 'GTE', 'LTE', 'NEQ', 'EQ', 'GT', 'LT'),
    ('left', '+', '-', 'DOTADD', 'DOTSUB'),
    ('left', '*', '/', 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS', '\''),   # Unary minus & transpose
)

def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, p.lexpos, p.type, p.value))
    else:
        print("Unexpected end of input")

def p_program(p):
    """program : instr_rec
               | """
    p[0] = p[1]

def p_instr_rec(p):
    """instr_rec : instr_rec instr
                 | instr"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_instr(p):
    """instr : instr_colon ';'
             | instr_coloff"""
    p[0] = p[1]

def p_instr_colon(p):
    """instr_colon : assign
                   | expr
                   | print
                   | return"""
    p[0] = p[1]

def p_instr_coloff(p):
    """instr_coloff : for
                    | while
                    | block
                    | if"""
    p[0] = p[1]

def p_instr_inside_loop(p):
    """instr_inside_loop : instr_colon ';'
                         | instr_coloff_inside_loop"""
    p[0] = p[1]

def p_instr_coloff_inside_loop(p):
    """instr_coloff_inside_loop : for
                                | while
                                | block_loop
                                | if_inside_loop"""
    p[0] = p[1]

# ------------------------------------------------------------------

def p_expr_1(p):
    """expr : INTNUM"""
    p[0] = IntNum(p[1])

def p_expr_2(p):
    """expr : FLOATNUM"""
    p[0] = FloatNum(p[1])

def p_expr_3(p):
    """expr : STRING"""
    p[0] = String(p[1])

def p_expr_4(p):
    """expr : ID"""
    p[0] = Id(p[1])

def p_expr_5(p):
    """expr : expr_rel"""
    p[0] = p[1]

def p_expr_6(p):
    """expr : '(' expr ')'"""
    p[0] = p[2]

def p_expr_7(p):
    """expr : '-' expr %prec UMINUS"""
    p[0] = UMinus(p[2])

def p_expr_8(p):
    """expr : expr '\\''"""
    p[0] = Transpose(p[1])

def p_expr_9(p):
    """expr : '[' rows ']'"""
    p[0] = Matrix(p[2])

def p_expr_bin(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '/' expr
            | expr '*' expr"""
    p[0] = BinExpr(p[2], p[1], p[3]) 

def p_expr_matrix(p):
    """expr : ZEROS '(' INTNUM ')'
            | ONES '(' INTNUM ')'
            | EYE '(' INTNUM ')'"""
    p[0] = MatrixSpecialMethod(p[1], IntNum(p[3]))

# nie mozemy zrobic np zeros(A) zeros(-2) a wypadaloby dac taka mozliwosc
def p_expr_matrix_with_expr(p):
    """expr : ZEROS '(' expr ')'
            | ONES '(' expr ')'
            | EYE '(' expr ')'"""
    p[0] = MatrixSpecialMethod(p[1], IntNum(p[3]))

def p_expr_dot(p):
    """expr : expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTDIV expr
            | expr DOTMUL expr"""
    p[0] = BinExpr(p[2], p[1], p[3])

def p_expr_rel(p):
    """expr_rel : expr GTE expr
                | expr LTE expr
                | expr NEQ expr
                | expr EQ expr
                | expr GT expr
                | expr LT expr"""
    p[0] = BinExpr(p[2], p[1], p[3])

def p_assign(p):
    """assign : id '=' expr
              | id ADDASSIGN expr
              | id SUBASSIGN expr
              | id MULASSIGN expr
              | id DIVASSIGN expr"""
    p[0] = Assign(p[2], p[1], p[3])


def p_rows(p):
    """rows : rows ',' row
            | row"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_row(p):
    """row : '[' cells ']'"""
    p[0] = p[2]

def p_cells(p):
    """cells : cells ',' expr
             | expr"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]

# ------------------------------------------------------------------

def p_if(p):
    """if : IF '(' expr_rel ')' instr %prec IF
          | IF '(' expr_rel ')' instr ELSE instr"""
    if len(p) == 8:
        p[0] = If(p[3], p[5], p[7])
    elif len(p) == 6:
        p[0] = If(p[3], p[5])

def p_if_inside_loop(p):
    """if_inside_loop : IF '(' expr_rel ')' inside_loop %prec IF
                      | IF '(' expr_rel ')' inside_loop ELSE inside_loop"""
    if len(p) == 8:
        p[0] = If(p[3], p[5], p[7])
    elif len(p) == 6:
        p[0] = If(p[3], p[5])

def p_for(p):
    """for : FOR ID '=' index ':' index inside_loop"""
    p[0] = For(Id(p[2]), p[4], p[6], p[7])

def p_while(p):
    """while : WHILE '(' expr_rel ')' inside_loop"""
    p[0] = While(p[3], p[5])

def p_inside_loop(p):
    """inside_loop : break_continue ';'
                   | instr_inside_loop"""
    p[0] = p[1]

def p_inside_loop_rec(p):
    """inside_loop_rec : inside_loop_rec inside_loop
                       | inside_loop"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_block_loop(p):
    """block_loop : '{' inside_loop_rec '}'"""
    p[0] = Block(p[2])

def p_block(p):
    """block : '{' instr_rec '}'"""
    p[0] = Block(p[2])

# ------------------------------------------------------------------

def p_print(p):
    """print : PRINT cells"""
    p[0] = Print(p[2])

def p_return(p):
    """return : RETURN expr"""
    p[0] = Return(p[2])

def p_id(p):
    """id : id_2
          | ref"""
    p[0] = p[1]

def p_id_2(p):
    """id_2 : ID"""
    p[0] = Id(p[1])

def p_ref(p):
    """ref : ID '[' index ',' index ']'"""
    p[0] = Ref(Id(p[1]), p[3], p[5])

def p_index(p):
    """index : ID
             | INTNUM"""
    if p[1] == "ID":
        p[0] = Id(p[1])
    else:
        p[0] = IntNum(p[1])

def p_break_continue(p):
    """break_continue : break
                      | continue"""
    p[0] = p[1]

def p_break(p):
    """break : BREAK"""
    p[0] = Break(p[1])

def p_continue(p):
    """continue : CONTINUE"""
    p[0] = Continue(p[1])

# ------------------------------------------------------------------

parser = yacc.yacc(debug=True)
