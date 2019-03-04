from io import StringIO

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from olive.error_listeners import OliveErrorListener
from olive.listeners import OliveListener
from olive.parsers.v1.OliveLexer import OliveLexer
from olive.parsers.v1.OliveParser import OliveParser


class TestOliveParser(object):

    def setup_parser(self, text):
        lexer = OliveLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = OliveParser(stream)
        self.tasks = []
        self.error = StringIO()
        parser.removeErrorListeners()
        errorListener = OliveErrorListener(self.error)
        parser.addErrorListener(errorListener)
        self.errorListener = errorListener
        return parser

    def walk(self, parser):
        tree = parser.description()
        listener = OliveListener(self.tasks)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_valid_description(self):
        parser = self.setup_parser("Here is a task >s ! #personal")
        self.walk(parser)
        assert len(self.errorListener.symbol) == 0

    def test_invalid_description(self):
        parser = self.setup_parser("! Here is an invalid task")
        self.walk(parser)
        assert self.errorListener.symbol == '!'
