
import sys
# import ply.lex as lex
import scanner  # scanner.py is a file you create, (it is not an external library)
import Mparser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "../txt/plik.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    # ---------------- skaner ----------------
    text = file.read()
    lexer = scanner.lexer
    lexer.input(text) # Give the lexer some input

    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break    # No more input
    #     column = Z
    #     print("(%d,%d): %s(%s)" %(tok.lineno, column, tok.type, tok.value))

    # ---------------- parser ----------------
    parser = Mparser.parser
    p = parser.parse(text, lexer=lexer)

    # ----------- drzewo skladni -------------
    ast = p
    # for i in ast:
    #     i.printTree()

    # -------- analiza semantyczna -----------
    analisisPositive = True
    typeChecker = TypeChecker()
    for node in ast:
        if typeChecker.visit(node) == None:
            analisisPositive = False

    # ------------- interpreter --------------
    if (analisisPositive):
        interpreter = Interpreter()
        for node in ast:
            interpreter.visit(node)
    # ----------------------------------------
