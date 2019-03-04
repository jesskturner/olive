# Generated from olive/parsers/v1/Olive.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OliveParser import OliveParser
else:
    from OliveParser import OliveParser

# This class defines a complete listener for a parse tree produced by OliveParser.
class OliveListener(ParseTreeListener):

    # Enter a parse tree produced by OliveParser#tasklist.
    def enterTasklist(self, ctx:OliveParser.TasklistContext):
        pass

    # Exit a parse tree produced by OliveParser#tasklist.
    def exitTasklist(self, ctx:OliveParser.TasklistContext):
        pass


    # Enter a parse tree produced by OliveParser#task.
    def enterTask(self, ctx:OliveParser.TaskContext):
        pass

    # Exit a parse tree produced by OliveParser#task.
    def exitTask(self, ctx:OliveParser.TaskContext):
        pass


    # Enter a parse tree produced by OliveParser#description.
    def enterDescription(self, ctx:OliveParser.DescriptionContext):
        pass

    # Exit a parse tree produced by OliveParser#description.
    def exitDescription(self, ctx:OliveParser.DescriptionContext):
        pass


    # Enter a parse tree produced by OliveParser#link.
    def enterLink(self, ctx:OliveParser.LinkContext):
        pass

    # Exit a parse tree produced by OliveParser#link.
    def exitLink(self, ctx:OliveParser.LinkContext):
        pass


    # Enter a parse tree produced by OliveParser#priority.
    def enterPriority(self, ctx:OliveParser.PriorityContext):
        pass

    # Exit a parse tree produced by OliveParser#priority.
    def exitPriority(self, ctx:OliveParser.PriorityContext):
        pass


    # Enter a parse tree produced by OliveParser#size.
    def enterSize(self, ctx:OliveParser.SizeContext):
        pass

    # Exit a parse tree produced by OliveParser#size.
    def exitSize(self, ctx:OliveParser.SizeContext):
        pass


    # Enter a parse tree produced by OliveParser#tag.
    def enterTag(self, ctx:OliveParser.TagContext):
        pass

    # Exit a parse tree produced by OliveParser#tag.
    def exitTag(self, ctx:OliveParser.TagContext):
        pass


