# Generated from olive/parsers/v1/Olive.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\6\4!\n\4\r\4\16\4\"\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\6\6.\n\6\r\6\16\6/\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3")
        buf.write("\3\r\r\2:\2\21\3\2\2\2\4\27\3\2\2\2\6 \3\2\2\2\b$\3\2")
        buf.write("\2\2\n+\3\2\2\2\f\61\3\2\2\2\16\65\3\2\2\2\20\22\5\4\3")
        buf.write("\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2")
        buf.write("\2\2\24\25\3\2\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\5")
        buf.write("\6\4\2\30\31\t\2\2\2\31\5\3\2\2\2\32!\5\b\5\2\33!\5\n")
        buf.write("\6\2\34!\5\f\7\2\35!\5\16\b\2\36!\7\13\2\2\37!\7\f\2\2")
        buf.write(" \32\3\2\2\2 \33\3\2\2\2 \34\3\2\2\2 \35\3\2\2\2 \36\3")
        buf.write("\2\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\7")
        buf.write("\3\2\2\2$%\7\3\2\2%&\7\n\2\2&\'\7\4\2\2\'(\7\5\2\2()\7")
        buf.write("\n\2\2)*\7\6\2\2*\t\3\2\2\2+-\7\f\2\2,.\7\7\2\2-,\3\2")
        buf.write("\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\13\3\2\2\2\61")
        buf.write("\62\7\f\2\2\62\63\7\b\2\2\63\64\7\13\2\2\64\r\3\2\2\2")
        buf.write("\65\66\7\f\2\2\66\67\7\t\2\2\678\7\13\2\28\17\3\2\2\2")
        buf.write("\6\23 \"/")
        return buf.getvalue()


class OliveParser ( Parser ):

    grammarFileName = "Olive.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'('", "')'", "'!'", "'>'", 
                     "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "WORD", "WHITESPACE", "NEWLINE" ]

    RULE_tasklist = 0
    RULE_task = 1
    RULE_description = 2
    RULE_link = 3
    RULE_priority = 4
    RULE_size = 5
    RULE_tag = 6

    ruleNames =  [ "tasklist", "task", "description", "link", "priority", 
                   "size", "tag" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    TEXT=8
    WORD=9
    WHITESPACE=10
    NEWLINE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TasklistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OliveParser.EOF, 0)

        def task(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OliveParser.TaskContext)
            else:
                return self.getTypedRuleContext(OliveParser.TaskContext,i)


        def getRuleIndex(self):
            return OliveParser.RULE_tasklist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTasklist" ):
                listener.enterTasklist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTasklist" ):
                listener.exitTasklist(self)




    def tasklist(self):

        localctx = OliveParser.TasklistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tasklist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.task()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OliveParser.T__0) | (1 << OliveParser.WORD) | (1 << OliveParser.WHITESPACE))) != 0)):
                    break

            self.state = 19
            self.match(OliveParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TaskContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def description(self):
            return self.getTypedRuleContext(OliveParser.DescriptionContext,0)


        def NEWLINE(self):
            return self.getToken(OliveParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(OliveParser.EOF, 0)

        def getRuleIndex(self):
            return OliveParser.RULE_task

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask" ):
                listener.enterTask(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask" ):
                listener.exitTask(self)




    def task(self):

        localctx = OliveParser.TaskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_task)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.description()
            self.state = 22
            _la = self._input.LA(1)
            if not(_la==OliveParser.EOF or _la==OliveParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OliveParser.LinkContext)
            else:
                return self.getTypedRuleContext(OliveParser.LinkContext,i)


        def priority(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OliveParser.PriorityContext)
            else:
                return self.getTypedRuleContext(OliveParser.PriorityContext,i)


        def size(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OliveParser.SizeContext)
            else:
                return self.getTypedRuleContext(OliveParser.SizeContext,i)


        def tag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OliveParser.TagContext)
            else:
                return self.getTypedRuleContext(OliveParser.TagContext,i)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(OliveParser.WORD)
            else:
                return self.getToken(OliveParser.WORD, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(OliveParser.WHITESPACE)
            else:
                return self.getToken(OliveParser.WHITESPACE, i)

        def getRuleIndex(self):
            return OliveParser.RULE_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescription" ):
                listener.enterDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescription" ):
                listener.exitDescription(self)




    def description(self):

        localctx = OliveParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_description)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 24
                    self.link()
                    pass

                elif la_ == 2:
                    self.state = 25
                    self.priority()
                    pass

                elif la_ == 3:
                    self.state = 26
                    self.size()
                    pass

                elif la_ == 4:
                    self.state = 27
                    self.tag()
                    pass

                elif la_ == 5:
                    self.state = 28
                    self.match(OliveParser.WORD)
                    pass

                elif la_ == 6:
                    self.state = 29
                    self.match(OliveParser.WHITESPACE)
                    pass


                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OliveParser.T__0) | (1 << OliveParser.WORD) | (1 << OliveParser.WHITESPACE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(OliveParser.TEXT)
            else:
                return self.getToken(OliveParser.TEXT, i)

        def getRuleIndex(self):
            return OliveParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = OliveParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(OliveParser.T__0)
            self.state = 35
            self.match(OliveParser.TEXT)
            self.state = 36
            self.match(OliveParser.T__1)
            self.state = 37
            self.match(OliveParser.T__2)
            self.state = 38
            self.match(OliveParser.TEXT)
            self.state = 39
            self.match(OliveParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PriorityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(OliveParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return OliveParser.RULE_priority

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPriority" ):
                listener.enterPriority(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPriority" ):
                listener.exitPriority(self)




    def priority(self):

        localctx = OliveParser.PriorityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_priority)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(OliveParser.WHITESPACE)
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.match(OliveParser.T__4)
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==OliveParser.T__4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(OliveParser.WHITESPACE, 0)

        def WORD(self):
            return self.getToken(OliveParser.WORD, 0)

        def getRuleIndex(self):
            return OliveParser.RULE_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize" ):
                listener.enterSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize" ):
                listener.exitSize(self)




    def size(self):

        localctx = OliveParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(OliveParser.WHITESPACE)
            self.state = 48
            self.match(OliveParser.T__5)
            self.state = 49
            self.match(OliveParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(OliveParser.WHITESPACE, 0)

        def WORD(self):
            return self.getToken(OliveParser.WORD, 0)

        def getRuleIndex(self):
            return OliveParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)




    def tag(self):

        localctx = OliveParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(OliveParser.WHITESPACE)
            self.state = 52
            self.match(OliveParser.T__6)
            self.state = 53
            self.match(OliveParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





