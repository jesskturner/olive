import sys

from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker

from olive.listeners import OliveListener
from olive.parsers.v1.OliveLexer import OliveLexer
from olive.parsers.v1.OliveParser import OliveParser


def main(argv=None):
    if argv is None:
        argv = sys.argv
    input = FileStream(argv[1])
    lexer = OliveLexer(input)
    stream = CommonTokenStream(lexer)
    parser = OliveParser(stream)
    tree = parser.tasklist()
    tasks = []
    listener = OliveListener(tasks)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    sys.stdout.write(str([task for task in tasks]) + '\n')


if __name__ == '__main__':
    sys.exit(main())
