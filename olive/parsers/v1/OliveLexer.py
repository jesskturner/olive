# Generated from olive/parsers/v1/Olive.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("S\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\6\r:\n\r\r\r\16\r;\3\16\3\16\3\16\3\16")
        buf.write("\6\16B\n\16\r\16\16\16C\3\17\6\17G\n\17\r\17\16\17H\3")
        buf.write("\20\5\20L\n\20\3\20\3\20\6\20P\n\20\r\20\16\20Q\2\2\21")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\2\27\2\31")
        buf.write("\n\33\13\35\f\37\r\3\2\b\3\2\62;\3\2c|\3\2C\\\b\2$$)+")
        buf.write(".\60<=AAaa\4\2++__\4\2\13\13\"\"\2W\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2")
        buf.write("\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23")
        buf.write("\61\3\2\2\2\25\63\3\2\2\2\27\65\3\2\2\2\31\67\3\2\2\2")
        buf.write("\33A\3\2\2\2\35F\3\2\2\2\37O\3\2\2\2!\"\7]\2\2\"\4\3\2")
        buf.write("\2\2#$\7_\2\2$\6\3\2\2\2%&\7*\2\2&\b\3\2\2\2\'(\7+\2\2")
        buf.write("(\n\3\2\2\2)*\7#\2\2*\f\3\2\2\2+,\7@\2\2,\16\3\2\2\2-")
        buf.write(".\7%\2\2.\20\3\2\2\2/\60\t\2\2\2\60\22\3\2\2\2\61\62\t")
        buf.write("\3\2\2\62\24\3\2\2\2\63\64\t\4\2\2\64\26\3\2\2\2\65\66")
        buf.write("\t\5\2\2\66\30\3\2\2\2\679\6\r\2\28:\n\6\2\298\3\2\2\2")
        buf.write(":;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\32\3\2\2\2=B\5\23\n\2")
        buf.write(">B\5\25\13\2?B\5\27\f\2@B\5\21\t\2A=\3\2\2\2A>\3\2\2\2")
        buf.write("A?\3\2\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\34")
        buf.write("\3\2\2\2EG\t\7\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2")
        buf.write("\2\2I\36\3\2\2\2JL\7\17\2\2KJ\3\2\2\2KL\3\2\2\2LM\3\2")
        buf.write("\2\2MP\7\f\2\2NP\7\17\2\2OK\3\2\2\2ON\3\2\2\2PQ\3\2\2")
        buf.write("\2QO\3\2\2\2QR\3\2\2\2R \3\2\2\2\n\2;ACHKOQ\2")
        return buf.getvalue()


class OliveLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    TEXT = 8
    WORD = 9
    WHITESPACE = 10
    NEWLINE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'('", "')'", "'!'", "'>'", "'#'" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "WORD", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "DIGITS", "LOWERCASE", "UPPERCASE", "PUNCT", "TEXT", "WORD", 
                  "WHITESPACE", "NEWLINE" ]

    grammarFileName = "Olive.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[11] = self.TEXT_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def TEXT_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self._input.LA(-1) == ord('[') or self._input.LA(-1) == ord('(')
         


