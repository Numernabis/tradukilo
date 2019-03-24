#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
    ('nonassoc', '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ('nonassoc', 'GTE', 'LTE', 'NEQ', 'EQ', 'GT', 'LT'),
    ('left', '+', '-', 'DOTADD', 'DOTSUB'),
    ('left', '*', '/', 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS'),    # Unary minus operator
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

def p_expr_1(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '/' expr
            | expr '*' expr"""
    p[0] = (p[2], p[1], p[3])

def p_expr_2(p):
    """expr : INTNUM
            | FLOATNUM
            | STRING
            | ID"""
    p[0] = p[1]

def p_expr_3(p):
    """expr : ZEROS '(' INTNUM ')'
            | ONES '(' INTNUM ')'
            | EYE '(' INTNUM ')'"""
    p[0] = (p[1], p[3], p[3])

def p_expr_4(p):
    """expr : expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTDIV expr
            | expr DOTMUL expr"""
    p[0] = (p[2], p[1], p[3])

def p_expr_5(p):
    """expr : '(' expr ')'"""
    p[0] = p[2]

def p_expr_6(p):
    """expr : '-' expr %prec UMINUS"""
    p[0] = ('UMINUS', p[2])

def p_expr_7(p):
    """expr : expr '\\''"""
    p[0] = ('TRANSPOSE', p[1])

def p_expr_8(p):
    """expr : '[' rows ']'"""
    p[0] = p[2]

def p_expr_rel(p):
    """expr_rel : expr GTE expr
                | expr LTE expr
                | expr NEQ expr
                | expr EQ expr
                | expr GT expr
                | expr LT expr"""
    p[0] = (p[2], p[1], p[3])

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

def p_if(p):
    """if : IF '(' expr_rel ')' instr ELSE instr
          | IF '(' expr_rel ')' instr"""
    if len(p) == 8:
        p[0] = ('IF', p[3], p[5], 'ELSE', p[7])
    elif len(p) == 6:
        p[0] = ('IF', p[3], p[5])

def p_if_inside_loop(p):
    """if_inside_loop : IF '(' expr_rel ')' inside_loop ELSE inside_loop
                      | IF '(' expr_rel ')' inside_loop"""
    if len(p) == 8:
        p[0] = ('IF', p[3], p[5], 'ELSE', p[7])
    elif len(p) == 6:
        p[0] = ('IF', p[3], p[5])

def p_for(p):
    """for : FOR ID '=' index ':' index inside_loop"""
    p[0] = ('FOR', p[2], p[4], p[6], p[7])

def p_while(p):
    """while : WHILE '(' expr_rel ')' inside_loop"""
    p[0] = ('WHILE', p[3], p[5])

def p_inside_loop(p):
    """inside_loop : break_continue ';'
                   | instr_inside_loop"""
    p[0] = p[1]

def p_block_loop(p):
    """block_loop : '{' inside_loop_rec '}'"""
    p[0] = p[2]

def p_inside_loop_rec(p):
    """inside_loop_rec : inside_loop_rec inside_loop
                       | inside_loop"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_print(p):
    """print : PRINT cells"""
    p[0] = ('PRINT', p[2])

def p_block(p):
    """block : '{' instr_rec '}'"""
    p[0] = p[2]

def p_assign(p):
    """assign : id '=' expr
              | id ADDASSIGN expr
              | id SUBASSIGN expr
              | id MULASSIGN expr
              | id DIVASSIGN expr"""
    p[0] = (p[2], p[1], p[3])

def p_cells(p):
    """cells : cells ',' expr
             | expr"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_return(p):
    """return : RETURN expr"""
    p[0] = ('RETURN', p[2])

def p_id(p):
    """id : ID
          | cell"""
    p[0] = p[1]

def p_cell(p):
    """cell : ID '[' index ',' index ']'"""
    p[0] = ('CELL', p[1], p[3], p[5])

def p_index(p):
    """index : ID
             | INTNUM"""
    p[0] = p[1]   

def p_break_continue(p):
    """break_continue : BREAK
                      | CONTINUE"""
    p[0] = p[1]

parser = yacc.yacc()
