
import sys
# import ply.lex as lex
import scanner  # scanner.py is a file you create, (it is not an external library)
import Mparser
from TreePrinter import TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "../txt/plik.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = scanner.lexer  
    lexer.input(text) # Give the lexer some input

    # parser = Mparser.parser
    # text = file.read()
    # parser.parse(text, lexer=scanner.lexer)
    # Tokenize
    # while True:
    #     tok = lexer.token()
    #     if not tok: 
    #         break    # No more input
    #     column = Z
    #     print("(%d,%d): %s(%s)" %(tok.lineno, column, tok.type, tok.value))

    parser = Mparser.parser
    p = parser.parse(text, lexer=lexer)
    ast = p
    for i in ast:
        i.printTree()
    
    # i = 0
    # while (i < len(p)):
    #     a = p[i]
    #     print(a[0])
    #     j = 1
    #     while (j < len(a)):
    #         print('  ', a[j])
    #         j += 1
    #     i += 1

    # ast.printTree()


