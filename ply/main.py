
import sys
# import ply.lex as lex
import scanner  # scanner.py is a file you create, (it is not an external library)
import Mparser


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "plik.txt"
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
    parser.parse(text, lexer=lexer)
        