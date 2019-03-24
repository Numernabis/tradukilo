#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
   # to fill ...
   # to fill ...
   ("left", '+', '-'),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, p.lexpos, p.type, p.value))
    else:
        print("Unexpected end of input")

def p_program(p):
    """program : instr_rec
               | """

def p_instr_rec(p):
    """instr_rec : instr_rec instr
                 | instr"""

def p_instr(p):
    """instr : instr_colon ';'
             | instr_coloff"""

def p_instr_colon(p):
    """instr_colon : assign
                   | expr
                   | print
                   | return"""

def p_instr_coloff(p):
    """instr_coloff : for
                    | while
                    | block
                    | if"""

def p_instr_inside_loop(p):
    """instr_inside_loop : instr_colon ';'
                         | instr_coloff_inside_loop"""

def p_instr_coloff_inside_loop(p):
    """instr_coloff_inside_loop : for
                                | while
                                | block_loop
                                | if_inside_loop"""

def p_expr_1(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '/' expr
            | expr '*' expr"""

def p_expr_2(p):
    """expr : INTNUM
            | FLOATNUM
            | STRING
            | ID"""

def p_expr_3(p):
    """expr : ZEROS '(' INTNUM ')'
            | ONES '(' INTNUM ')'
            | EYE '(' INTNUM ')'"""

def p_expr_4(p):
    """expr : expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTDIV expr
            | expr DOTMUL expr"""

def p_expr_5(p):
    """expr : '-' expr
            | '(' expr ')'
            | expr '\\'' """

def p_expr_6(p):
    """expr : '[' rows ']'"""

def p_expr_rel(p):
    """expr_rel : expr GTE expr
                | expr LTE expr
                | expr NEQ expr
                | expr EQ expr
                | expr GT expr
                | expr LT expr"""

def p_rows(p):
    """rows : rows ',' row
            | row"""

def p_row(p):
    """row : '[' cells ']'"""

def p_if(p):
    """if : IF '(' expr_rel ')' instr
          | IF '(' expr_rel ')' instr ELSE instr"""

def p_if_inside_loop(p):
    """if_inside_loop : IF '(' expr_rel ')' inside_loop
                      | IF '(' expr_rel ')' inside_loop ELSE inside_loop"""

def p_for(p):
    """for : FOR ID '=' id_or_intnum ':' id_or_intnum inside_loop"""

def p_while(p):
    """while : WHILE '(' expr_rel ')' inside_loop"""

def p_inside_loop(p):
    """inside_loop : break_continue ';'
                   | instr_inside_loop"""

def p_block_loop(p):
    """block_loop : '{' inside_loop_rec '}'"""

def p_inside_loop_rec(p):
    """inside_loop_rec : inside_loop_rec inside_loop
                       | inside_loop"""

def p_print(p):
    """print : PRINT cells"""

def p_block(p):
    """block : '{' instr_rec '}'"""

def p_assign(p):
    """assign : id '=' expr
              | id ADDASSIGN expr
              | id SUBASSIGN expr
              | id MULASSIGN expr
              | id DIVASSIGN expr"""

def p_cells(p):
    """cells : cells ',' expr
             | expr"""

def p_return(p):
    """return : RETURN expr"""

def p_id(p):
    """id : ID
          | cell"""

def p_cell(p):
    """cell : ID '[' index ',' index ']'"""

def p_index(p):
    """index : ID
             | INTNUM"""    

# potrzebne do for'a
def p_id_or_intnum(p):
    """id_or_intnum : INTNUM
                    | ID"""

def p_break_continue(p):
    """break_continue : BREAK
                      | CONTINUE"""

parser = yacc.yacc()
