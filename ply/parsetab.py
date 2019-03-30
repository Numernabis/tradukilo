
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassoc=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNnonassocGTELTENEQEQGTLTleft+-DOTADDDOTSUBleft*/DOTMULDOTDIVrightUMINUS'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GT GTE ID IF INTNUM LT LTE MULASSIGN NEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instr_rec\n               | instr_rec : instr_rec instr\n                 | instrinstr : instr_colon ';'\n             | instr_coloffinstr_colon : assign\n                   | expr\n                   | print\n                   | returninstr_coloff : for\n                    | while\n                    | block\n                    | ifinstr_inside_loop : instr_colon ';'\n                         | instr_coloff_inside_loopinstr_coloff_inside_loop : for\n                                | while\n                                | block_loop\n                                | if_inside_loopexpr : expr '+' expr\n            | expr '-' expr\n            | expr '/' expr\n            | expr '*' exprexpr : INTNUM\n            | FLOATNUM\n            | STRING\n            | ID\n            | expr_relexpr : ZEROS '(' INTNUM ')'\n            | ONES '(' INTNUM ')'\n            | EYE '(' INTNUM ')'expr : expr DOTADD expr\n            | expr DOTSUB expr\n            | expr DOTDIV expr\n            | expr DOTMUL exprexpr : '(' expr ')'expr : '-' expr %prec UMINUSexpr : expr '\\''expr : '[' rows ']'expr_rel : expr GTE expr\n                | expr LTE expr\n                | expr NEQ expr\n                | expr EQ expr\n                | expr GT expr\n                | expr LT exprrows : rows ',' row\n            | rowrow : '[' cells ']'if : IF '(' expr_rel ')' instr ELSE instr\n          | IF '(' expr_rel ')' instrif_inside_loop : IF '(' expr_rel ')' inside_loop ELSE inside_loop\n                      | IF '(' expr_rel ')' inside_loopfor : FOR ID '=' index ':' index inside_loopwhile : WHILE '(' expr_rel ')' inside_loopinside_loop : break_continue ';'\n                   | instr_inside_loopblock_loop : '{' inside_loop_rec '}'inside_loop_rec : inside_loop_rec inside_loop\n                       | inside_loopprint : PRINT cellsblock : '{' instr_rec '}'assign : id '=' expr\n              | id ADDASSIGN expr\n              | id SUBASSIGN expr\n              | id MULASSIGN expr\n              | id DIVASSIGN exprcells : cells ',' expr\n             | exprreturn : RETURN exprid : ID\n          | cellcell : ID '[' index ',' index ']'index : ID\n             | INTNUMbreak_continue : BREAK\n                      | CONTINUE"
    
_lr_action_items = {'$end':([0,1,2,3,5,10,11,12,13,33,34,105,119,121,125,126,127,128,129,132,135,136,141,142,145,147,149,],[-2,0,-1,-4,-6,-11,-12,-13,-14,-3,-5,-62,-55,-57,-16,-17,-18,-19,-20,-51,-56,-15,-54,-58,-50,-53,-52,]),'INTNUM':([0,2,3,5,10,11,12,13,15,22,26,27,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,57,58,60,61,62,69,70,71,91,93,101,102,105,107,115,116,118,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[16,16,-4,-6,-11,-12,-13,-14,16,16,16,16,16,-3,-5,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,93,94,96,97,16,16,16,16,-74,-75,16,93,-62,93,16,16,93,-55,-57,-16,-17,-18,-19,-20,16,-51,16,-56,-15,16,-60,16,16,-54,-58,-59,-50,16,-53,16,-52,]),'FLOATNUM':([0,2,3,5,10,11,12,13,15,22,26,27,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,91,93,101,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[17,17,-4,-6,-11,-12,-13,-14,17,17,17,17,17,-3,-5,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-74,-75,17,-62,17,17,-55,-57,-16,-17,-18,-19,-20,17,-51,17,-56,-15,17,-60,17,17,-54,-58,-59,-50,17,-53,17,-52,]),'STRING':([0,2,3,5,10,11,12,13,15,22,26,27,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,91,93,101,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[18,18,-4,-6,-11,-12,-13,-14,18,18,18,18,18,-3,-5,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-74,-75,18,-62,18,18,-55,-57,-16,-17,-18,-19,-20,18,-51,18,-56,-15,18,-60,18,18,-54,-58,-59,-50,18,-53,18,-52,]),'ID':([0,2,3,5,10,11,12,13,15,22,26,27,28,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,57,62,69,70,71,91,93,101,102,105,107,115,116,118,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[19,19,-4,-6,-11,-12,-13,-14,56,56,56,56,68,19,-3,-5,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,91,56,56,19,56,-74,-75,56,91,-62,91,19,19,91,-55,-57,-16,-17,-18,-19,-20,19,-51,19,-56,-15,19,-60,56,19,-54,-58,-59,-50,19,-53,19,-52,]),'ZEROS':([0,2,3,5,10,11,12,13,15,22,26,27,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,91,93,101,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[21,21,-4,-6,-11,-12,-13,-14,21,21,21,21,21,-3,-5,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-74,-75,21,-62,21,21,-55,-57,-16,-17,-18,-19,-20,21,-51,21,-56,-15,21,-60,21,21,-54,-58,-59,-50,21,-53,21,-52,]),'ONES':([0,2,3,5,10,11,12,13,15,22,26,27,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,91,93,101,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[23,23,-4,-6,-11,-12,-13,-14,23,23,23,23,23,-3,-5,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-74,-75,23,-62,23,23,-55,-57,-16,-17,-18,-19,-20,23,-51,23,-56,-15,23,-60,23,23,-54,-58,-59,-50,23,-53,23,-52,]),'EYE':([0,2,3,5,10,11,12,13,15,22,26,27,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,91,93,101,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[24,24,-4,-6,-11,-12,-13,-14,24,24,24,24,24,-3,-5,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-74,-75,24,-62,24,24,-55,-57,-16,-17,-18,-19,-20,24,-51,24,-56,-15,24,-60,24,24,-54,-58,-59,-50,24,-53,24,-52,]),'(':([0,2,3,5,10,11,12,13,15,21,22,23,24,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,91,93,101,105,115,116,119,121,125,126,127,128,129,130,131,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[22,22,-4,-6,-11,-12,-13,-14,22,58,22,60,61,22,22,69,22,71,-3,-5,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-74,-75,22,-62,22,22,-55,-57,-16,-17,-18,-19,-20,22,139,-51,22,-56,-15,22,-60,22,22,-54,-58,-59,-50,22,-53,22,-52,]),'-':([0,2,3,5,7,10,11,12,13,15,16,17,18,19,20,22,26,27,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,62,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,95,99,101,103,104,105,106,108,109,110,113,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,],[15,15,-4,-6,36,-11,-12,-13,-14,15,-25,-26,-27,-28,-29,15,15,15,15,-3,-5,15,15,15,15,15,15,15,15,-39,15,15,15,15,15,15,15,15,15,15,15,-38,-28,36,15,36,36,15,15,15,-21,-22,-23,-24,-33,-34,-35,-36,36,36,36,36,36,36,36,36,36,36,36,-74,-75,-37,-40,15,-29,36,-62,-29,-30,-31,-32,36,15,15,-55,-57,-16,-17,-18,-19,-20,15,-51,15,-56,-15,15,-60,15,15,-54,-58,-59,-29,-50,15,-53,15,-52,]),'[':([0,2,3,5,10,11,12,13,15,19,22,25,26,27,30,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,91,93,100,101,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,],[25,25,-4,-6,-11,-12,-13,-14,25,57,25,62,25,25,25,-3,-5,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-74,-75,62,25,-62,25,25,-55,-57,-16,-17,-18,-19,-20,25,-51,25,-56,-15,25,-60,25,25,-54,-58,-59,-50,25,-53,25,-52,]),'PRINT':([0,2,3,5,10,11,12,13,30,33,34,70,91,93,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,140,141,142,143,145,146,147,148,149,],[26,26,-4,-6,-11,-12,-13,-14,26,-3,-5,26,-74,-75,-62,26,26,-55,-57,-16,-17,-18,-19,-20,26,-51,26,-56,-15,26,-60,26,-54,-58,-59,-50,26,-53,26,-52,]),'RETURN':([0,2,3,5,10,11,12,13,30,33,34,70,91,93,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,140,141,142,143,145,146,147,148,149,],[27,27,-4,-6,-11,-12,-13,-14,27,-3,-5,27,-74,-75,-62,27,27,-55,-57,-16,-17,-18,-19,-20,27,-51,27,-56,-15,27,-60,27,-54,-58,-59,-50,27,-53,27,-52,]),'FOR':([0,2,3,5,10,11,12,13,30,33,34,70,91,93,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,140,141,142,143,145,146,147,148,149,],[28,28,-4,-6,-11,-12,-13,-14,28,-3,-5,28,-74,-75,-62,28,28,-55,-57,-16,-17,-18,-19,-20,28,-51,28,-56,-15,28,-60,28,-54,-58,-59,-50,28,-53,28,-52,]),'WHILE':([0,2,3,5,10,11,12,13,30,33,34,70,91,93,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,140,141,142,143,145,146,147,148,149,],[29,29,-4,-6,-11,-12,-13,-14,29,-3,-5,29,-74,-75,-62,29,29,-55,-57,-16,-17,-18,-19,-20,29,-51,29,-56,-15,29,-60,29,-54,-58,-59,-50,29,-53,29,-52,]),'{':([0,2,3,5,10,11,12,13,30,33,34,70,91,93,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,140,141,142,143,145,146,147,148,149,],[30,30,-4,-6,-11,-12,-13,-14,30,-3,-5,30,-74,-75,-62,130,30,-55,-57,-16,-17,-18,-19,-20,130,-51,130,-56,-15,130,-60,30,-54,-58,-59,-50,130,-53,130,-52,]),'IF':([0,2,3,5,10,11,12,13,30,33,34,70,91,93,105,115,116,119,121,125,126,127,128,129,130,132,134,135,136,137,138,140,141,142,143,145,146,147,148,149,],[31,31,-4,-6,-11,-12,-13,-14,31,-3,-5,31,-74,-75,-62,131,31,-55,-57,-16,-17,-18,-19,-20,131,-51,131,-56,-15,131,-60,31,-54,-58,-59,-50,131,-53,131,-52,]),'}':([3,5,10,11,12,13,33,34,70,105,119,121,125,126,127,128,129,132,135,136,137,138,141,142,143,145,147,149,],[-4,-6,-11,-12,-13,-14,-3,-5,105,-62,-55,-57,-16,-17,-18,-19,-20,-51,-56,-15,142,-60,-54,-58,-59,-50,-53,-52,]),';':([4,6,7,8,9,16,17,18,19,20,43,55,56,65,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,108,109,110,113,120,122,123,124,],[34,-7,-8,-9,-10,-25,-26,-27,-28,-29,-39,-38,-28,-61,-69,-70,-21,-22,-23,-24,-33,-34,-35,-36,-41,-42,-43,-44,-45,-46,-63,-64,-65,-66,-67,-37,-40,-30,-31,-32,-68,135,-76,-77,136,]),'ELSE':([5,10,11,12,13,34,105,119,121,125,126,127,128,129,132,135,136,141,142,145,147,149,],[-6,-11,-12,-13,-14,-5,-62,-55,-57,-16,-17,-18,-19,-20,140,-56,-15,-54,-58,-50,148,-52,]),'+':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[35,-25,-26,-27,-28,-29,-39,-38,-28,35,35,35,-21,-22,-23,-24,-33,-34,-35,-36,35,35,35,35,35,35,35,35,35,35,35,-37,-40,-29,35,-29,-30,-31,-32,35,-29,]),'/':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[37,-25,-26,-27,-28,-29,-39,-38,-28,37,37,37,37,37,-23,-24,37,37,-35,-36,37,37,37,37,37,37,37,37,37,37,37,-37,-40,-29,37,-29,-30,-31,-32,37,-29,]),'*':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[38,-25,-26,-27,-28,-29,-39,-38,-28,38,38,38,38,38,-23,-24,38,38,-35,-36,38,38,38,38,38,38,38,38,38,38,38,-37,-40,-29,38,-29,-30,-31,-32,38,-29,]),'DOTADD':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[39,-25,-26,-27,-28,-29,-39,-38,-28,39,39,39,-21,-22,-23,-24,-33,-34,-35,-36,39,39,39,39,39,39,39,39,39,39,39,-37,-40,-29,39,-29,-30,-31,-32,39,-29,]),'DOTSUB':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[40,-25,-26,-27,-28,-29,-39,-38,-28,40,40,40,-21,-22,-23,-24,-33,-34,-35,-36,40,40,40,40,40,40,40,40,40,40,40,-37,-40,-29,40,-29,-30,-31,-32,40,-29,]),'DOTDIV':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[41,-25,-26,-27,-28,-29,-39,-38,-28,41,41,41,41,41,-23,-24,41,41,-35,-36,41,41,41,41,41,41,41,41,41,41,41,-37,-40,-29,41,-29,-30,-31,-32,41,-29,]),'DOTMUL':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[42,-25,-26,-27,-28,-29,-39,-38,-28,42,42,42,42,42,-23,-24,42,42,-35,-36,42,42,42,42,42,42,42,42,42,42,42,-37,-40,-29,42,-29,-30,-31,-32,42,-29,]),"'":([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[43,-25,-26,-27,-28,-29,-39,43,-28,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-37,-40,-29,43,-29,-30,-31,-32,43,-29,]),'GTE':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[44,-25,-26,-27,-28,-29,-39,-38,-28,44,44,44,-21,-22,-23,-24,-33,-34,-35,-36,None,None,None,None,None,None,44,44,44,44,44,-37,-40,-29,44,-29,-30,-31,-32,44,-29,]),'LTE':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[45,-25,-26,-27,-28,-29,-39,-38,-28,45,45,45,-21,-22,-23,-24,-33,-34,-35,-36,None,None,None,None,None,None,45,45,45,45,45,-37,-40,-29,45,-29,-30,-31,-32,45,-29,]),'NEQ':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[46,-25,-26,-27,-28,-29,-39,-38,-28,46,46,46,-21,-22,-23,-24,-33,-34,-35,-36,None,None,None,None,None,None,46,46,46,46,46,-37,-40,-29,46,-29,-30,-31,-32,46,-29,]),'EQ':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[47,-25,-26,-27,-28,-29,-39,-38,-28,47,47,47,-21,-22,-23,-24,-33,-34,-35,-36,None,None,None,None,None,None,47,47,47,47,47,-37,-40,-29,47,-29,-30,-31,-32,47,-29,]),'GT':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[48,-25,-26,-27,-28,-29,-39,-38,-28,48,48,48,-21,-22,-23,-24,-33,-34,-35,-36,None,None,None,None,None,None,48,48,48,48,48,-37,-40,-29,48,-29,-30,-31,-32,48,-29,]),'LT':([7,16,17,18,19,20,43,55,56,59,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,99,103,104,106,108,109,110,113,144,],[49,-25,-26,-27,-28,-29,-39,-38,-28,49,49,49,-21,-22,-23,-24,-33,-34,-35,-36,None,None,None,None,None,None,49,49,49,49,49,-37,-40,-29,49,-29,-30,-31,-32,49,-29,]),'=':([14,19,32,68,133,],[50,-71,-72,102,-73,]),'ADDASSIGN':([14,19,32,133,],[51,-71,-72,-73,]),'SUBASSIGN':([14,19,32,133,],[52,-71,-72,-73,]),'MULASSIGN':([14,19,32,133,],[53,-71,-72,-73,]),'DIVASSIGN':([14,19,32,133,],[54,-71,-72,-73,]),')':([16,17,18,20,43,55,56,59,72,73,74,75,76,77,78,79,80,81,82,83,84,85,94,95,96,97,99,103,106,108,109,110,144,],[-25,-26,-27,-29,-39,-38,-28,95,-21,-22,-23,-24,-33,-34,-35,-36,-41,-42,-43,-44,-45,-46,108,-37,109,110,-40,115,116,-30,-31,-32,146,]),',':([16,17,18,20,43,55,56,63,64,65,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,92,93,95,98,99,108,109,110,111,112,113,],[-25,-26,-27,-29,-39,-38,-28,100,-48,101,-69,-21,-22,-23,-24,-33,-34,-35,-36,-41,-42,-43,-44,-45,-46,-74,107,-75,-37,101,-40,-30,-31,-32,-49,-47,-68,]),']':([16,17,18,20,43,55,56,63,64,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,93,95,98,99,108,109,110,111,112,113,117,],[-25,-26,-27,-29,-39,-38,-28,99,-48,-69,-21,-22,-23,-24,-33,-34,-35,-36,-41,-42,-43,-44,-45,-46,-74,-75,-37,111,-40,-30,-31,-32,-49,-47,-68,133,]),':':([91,93,114,],[-74,-75,118,]),'BREAK':([91,93,115,119,121,125,126,127,128,129,130,134,135,136,137,138,141,142,143,146,147,148,149,],[-74,-75,122,-55,-57,-16,-17,-18,-19,-20,122,122,-56,-15,122,-60,-54,-58,-59,122,-53,122,-52,]),'CONTINUE':([91,93,115,119,121,125,126,127,128,129,130,134,135,136,137,138,141,142,143,146,147,148,149,],[-74,-75,123,-55,-57,-16,-17,-18,-19,-20,123,123,-56,-15,123,-60,-54,-58,-59,123,-53,123,-52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instr_rec':([0,30,],[2,70,]),'instr':([0,2,30,70,116,140,],[3,33,3,33,132,145,]),'instr_colon':([0,2,30,70,115,116,130,134,137,140,146,148,],[4,4,4,4,124,4,124,124,124,4,124,124,]),'instr_coloff':([0,2,30,70,116,140,],[5,5,5,5,5,5,]),'assign':([0,2,30,70,115,116,130,134,137,140,146,148,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'expr':([0,2,15,22,26,27,30,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,101,115,116,130,134,137,139,140,146,148,],[7,7,55,59,66,67,7,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,66,104,7,104,113,7,7,7,7,7,104,7,7,7,]),'print':([0,2,30,70,115,116,130,134,137,140,146,148,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'return':([0,2,30,70,115,116,130,134,137,140,146,148,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'for':([0,2,30,70,115,116,130,134,137,140,146,148,],[10,10,10,10,126,10,126,126,126,10,126,126,]),'while':([0,2,30,70,115,116,130,134,137,140,146,148,],[11,11,11,11,127,11,127,127,127,11,127,127,]),'block':([0,2,30,70,116,140,],[12,12,12,12,12,12,]),'if':([0,2,30,70,116,140,],[13,13,13,13,13,13,]),'id':([0,2,30,70,115,116,130,134,137,140,146,148,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'expr_rel':([0,2,15,22,26,27,30,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,62,69,70,71,101,115,116,130,134,137,139,140,146,148,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,103,20,106,20,20,20,20,20,20,144,20,20,20,]),'cell':([0,2,30,70,115,116,130,134,137,140,146,148,],[32,32,32,32,32,32,32,32,32,32,32,32,]),'rows':([25,],[63,]),'row':([25,100,],[64,112,]),'cells':([26,62,],[65,98,]),'index':([57,102,107,118,],[92,114,117,134,]),'inside_loop':([115,130,134,137,146,148,],[119,138,141,143,147,149,]),'break_continue':([115,130,134,137,146,148,],[120,120,120,120,120,120,]),'instr_inside_loop':([115,130,134,137,146,148,],[121,121,121,121,121,121,]),'instr_coloff_inside_loop':([115,130,134,137,146,148,],[125,125,125,125,125,125,]),'block_loop':([115,130,134,137,146,148,],[128,128,128,128,128,128,]),'if_inside_loop':([115,130,134,137,146,148,],[129,129,129,129,129,129,]),'inside_loop_rec':([130,],[137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instr_rec','program',1,'p_program','Mparser.py',26),
  ('program -> <empty>','program',0,'p_program','Mparser.py',27),
  ('instr_rec -> instr_rec instr','instr_rec',2,'p_instr_rec','Mparser.py',31),
  ('instr_rec -> instr','instr_rec',1,'p_instr_rec','Mparser.py',32),
  ('instr -> instr_colon ;','instr',2,'p_instr','Mparser.py',39),
  ('instr -> instr_coloff','instr',1,'p_instr','Mparser.py',40),
  ('instr_colon -> assign','instr_colon',1,'p_instr_colon','Mparser.py',44),
  ('instr_colon -> expr','instr_colon',1,'p_instr_colon','Mparser.py',45),
  ('instr_colon -> print','instr_colon',1,'p_instr_colon','Mparser.py',46),
  ('instr_colon -> return','instr_colon',1,'p_instr_colon','Mparser.py',47),
  ('instr_coloff -> for','instr_coloff',1,'p_instr_coloff','Mparser.py',51),
  ('instr_coloff -> while','instr_coloff',1,'p_instr_coloff','Mparser.py',52),
  ('instr_coloff -> block','instr_coloff',1,'p_instr_coloff','Mparser.py',53),
  ('instr_coloff -> if','instr_coloff',1,'p_instr_coloff','Mparser.py',54),
  ('instr_inside_loop -> instr_colon ;','instr_inside_loop',2,'p_instr_inside_loop','Mparser.py',58),
  ('instr_inside_loop -> instr_coloff_inside_loop','instr_inside_loop',1,'p_instr_inside_loop','Mparser.py',59),
  ('instr_coloff_inside_loop -> for','instr_coloff_inside_loop',1,'p_instr_coloff_inside_loop','Mparser.py',63),
  ('instr_coloff_inside_loop -> while','instr_coloff_inside_loop',1,'p_instr_coloff_inside_loop','Mparser.py',64),
  ('instr_coloff_inside_loop -> block_loop','instr_coloff_inside_loop',1,'p_instr_coloff_inside_loop','Mparser.py',65),
  ('instr_coloff_inside_loop -> if_inside_loop','instr_coloff_inside_loop',1,'p_instr_coloff_inside_loop','Mparser.py',66),
  ('expr -> expr + expr','expr',3,'p_expr_1','Mparser.py',70),
  ('expr -> expr - expr','expr',3,'p_expr_1','Mparser.py',71),
  ('expr -> expr / expr','expr',3,'p_expr_1','Mparser.py',72),
  ('expr -> expr * expr','expr',3,'p_expr_1','Mparser.py',73),
  ('expr -> INTNUM','expr',1,'p_expr_2','Mparser.py',78),
  ('expr -> FLOATNUM','expr',1,'p_expr_2','Mparser.py',79),
  ('expr -> STRING','expr',1,'p_expr_2','Mparser.py',80),
  ('expr -> ID','expr',1,'p_expr_2','Mparser.py',81),
  ('expr -> expr_rel','expr',1,'p_expr_2','Mparser.py',82),
  ('expr -> ZEROS ( INTNUM )','expr',4,'p_expr_3','Mparser.py',87),
  ('expr -> ONES ( INTNUM )','expr',4,'p_expr_3','Mparser.py',88),
  ('expr -> EYE ( INTNUM )','expr',4,'p_expr_3','Mparser.py',89),
  ('expr -> expr DOTADD expr','expr',3,'p_expr_4','Mparser.py',94),
  ('expr -> expr DOTSUB expr','expr',3,'p_expr_4','Mparser.py',95),
  ('expr -> expr DOTDIV expr','expr',3,'p_expr_4','Mparser.py',96),
  ('expr -> expr DOTMUL expr','expr',3,'p_expr_4','Mparser.py',97),
  ('expr -> ( expr )','expr',3,'p_expr_5','Mparser.py',102),
  ('expr -> - expr','expr',2,'p_expr_6','Mparser.py',107),
  ("expr -> expr '",'expr',2,'p_expr_7','Mparser.py',112),
  ('expr -> [ rows ]','expr',3,'p_expr_8','Mparser.py',117),
  ('expr_rel -> expr GTE expr','expr_rel',3,'p_expr_rel','Mparser.py',122),
  ('expr_rel -> expr LTE expr','expr_rel',3,'p_expr_rel','Mparser.py',123),
  ('expr_rel -> expr NEQ expr','expr_rel',3,'p_expr_rel','Mparser.py',124),
  ('expr_rel -> expr EQ expr','expr_rel',3,'p_expr_rel','Mparser.py',125),
  ('expr_rel -> expr GT expr','expr_rel',3,'p_expr_rel','Mparser.py',126),
  ('expr_rel -> expr LT expr','expr_rel',3,'p_expr_rel','Mparser.py',127),
  ('rows -> rows , row','rows',3,'p_rows','Mparser.py',132),
  ('rows -> row','rows',1,'p_rows','Mparser.py',133),
  ('row -> [ cells ]','row',3,'p_row','Mparser.py',140),
  ('if -> IF ( expr_rel ) instr ELSE instr','if',7,'p_if','Mparser.py',144),
  ('if -> IF ( expr_rel ) instr','if',5,'p_if','Mparser.py',145),
  ('if_inside_loop -> IF ( expr_rel ) inside_loop ELSE inside_loop','if_inside_loop',7,'p_if_inside_loop','Mparser.py',152),
  ('if_inside_loop -> IF ( expr_rel ) inside_loop','if_inside_loop',5,'p_if_inside_loop','Mparser.py',153),
  ('for -> FOR ID = index : index inside_loop','for',7,'p_for','Mparser.py',160),
  ('while -> WHILE ( expr_rel ) inside_loop','while',5,'p_while','Mparser.py',165),
  ('inside_loop -> break_continue ;','inside_loop',2,'p_inside_loop','Mparser.py',169),
  ('inside_loop -> instr_inside_loop','inside_loop',1,'p_inside_loop','Mparser.py',170),
  ('block_loop -> { inside_loop_rec }','block_loop',3,'p_block_loop','Mparser.py',174),
  ('inside_loop_rec -> inside_loop_rec inside_loop','inside_loop_rec',2,'p_inside_loop_rec','Mparser.py',178),
  ('inside_loop_rec -> inside_loop','inside_loop_rec',1,'p_inside_loop_rec','Mparser.py',179),
  ('print -> PRINT cells','print',2,'p_print','Mparser.py',186),
  ('block -> { instr_rec }','block',3,'p_block','Mparser.py',190),
  ('assign -> id = expr','assign',3,'p_assign','Mparser.py',194),
  ('assign -> id ADDASSIGN expr','assign',3,'p_assign','Mparser.py',195),
  ('assign -> id SUBASSIGN expr','assign',3,'p_assign','Mparser.py',196),
  ('assign -> id MULASSIGN expr','assign',3,'p_assign','Mparser.py',197),
  ('assign -> id DIVASSIGN expr','assign',3,'p_assign','Mparser.py',198),
  ('cells -> cells , expr','cells',3,'p_cells','Mparser.py',203),
  ('cells -> expr','cells',1,'p_cells','Mparser.py',204),
  ('return -> RETURN expr','return',2,'p_return','Mparser.py',211),
  ('id -> ID','id',1,'p_id','Mparser.py',215),
  ('id -> cell','id',1,'p_id','Mparser.py',216),
  ('cell -> ID [ index , index ]','cell',6,'p_cell','Mparser.py',221),
  ('index -> ID','index',1,'p_index','Mparser.py',225),
  ('index -> INTNUM','index',1,'p_index','Mparser.py',226),
  ('break_continue -> BREAK','break_continue',1,'p_break_continue','Mparser.py',231),
  ('break_continue -> CONTINUE','break_continue',1,'p_break_continue','Mparser.py',232),
]
