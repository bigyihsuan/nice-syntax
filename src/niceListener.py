# Generated from nice.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .niceParser import niceParser
else:
    from niceParser import niceParser

# This class defines a complete listener for a parse tree produced by niceParser.
class niceListener(ParseTreeListener):

    # Enter a parse tree produced by niceParser#code.
    def enterCode(self, ctx:niceParser.CodeContext):
        pass

    # Exit a parse tree produced by niceParser#code.
    def exitCode(self, ctx:niceParser.CodeContext):
        pass


    # Enter a parse tree produced by niceParser#statement.
    def enterStatement(self, ctx:niceParser.StatementContext):
        pass

    # Exit a parse tree produced by niceParser#statement.
    def exitStatement(self, ctx:niceParser.StatementContext):
        pass


    # Enter a parse tree produced by niceParser#assignment.
    def enterAssignment(self, ctx:niceParser.AssignmentContext):
        pass

    # Exit a parse tree produced by niceParser#assignment.
    def exitAssignment(self, ctx:niceParser.AssignmentContext):
        pass


    # Enter a parse tree produced by niceParser#expr.
    def enterExpr(self, ctx:niceParser.ExprContext):
        pass

    # Exit a parse tree produced by niceParser#expr.
    def exitExpr(self, ctx:niceParser.ExprContext):
        pass


    # Enter a parse tree produced by niceParser#listSlice.
    def enterListSlice(self, ctx:niceParser.ListSliceContext):
        pass

    # Exit a parse tree produced by niceParser#listSlice.
    def exitListSlice(self, ctx:niceParser.ListSliceContext):
        pass


    # Enter a parse tree produced by niceParser#lSlice.
    def enterLSlice(self, ctx:niceParser.LSliceContext):
        pass

    # Exit a parse tree produced by niceParser#lSlice.
    def exitLSlice(self, ctx:niceParser.LSliceContext):
        pass


    # Enter a parse tree produced by niceParser#lAt.
    def enterLAt(self, ctx:niceParser.LAtContext):
        pass

    # Exit a parse tree produced by niceParser#lAt.
    def exitLAt(self, ctx:niceParser.LAtContext):
        pass


    # Enter a parse tree produced by niceParser#lFrom.
    def enterLFrom(self, ctx:niceParser.LFromContext):
        pass

    # Exit a parse tree produced by niceParser#lFrom.
    def exitLFrom(self, ctx:niceParser.LFromContext):
        pass


    # Enter a parse tree produced by niceParser#lFromTo.
    def enterLFromTo(self, ctx:niceParser.LFromToContext):
        pass

    # Exit a parse tree produced by niceParser#lFromTo.
    def exitLFromTo(self, ctx:niceParser.LFromToContext):
        pass


    # Enter a parse tree produced by niceParser#lIdxes.
    def enterLIdxes(self, ctx:niceParser.LIdxesContext):
        pass

    # Exit a parse tree produced by niceParser#lIdxes.
    def exitLIdxes(self, ctx:niceParser.LIdxesContext):
        pass


    # Enter a parse tree produced by niceParser#value.
    def enterValue(self, ctx:niceParser.ValueContext):
        pass

    # Exit a parse tree produced by niceParser#value.
    def exitValue(self, ctx:niceParser.ValueContext):
        pass


    # Enter a parse tree produced by niceParser#literalList.
    def enterLiteralList(self, ctx:niceParser.LiteralListContext):
        pass

    # Exit a parse tree produced by niceParser#literalList.
    def exitLiteralList(self, ctx:niceParser.LiteralListContext):
        pass


    # Enter a parse tree produced by niceParser#lElements.
    def enterLElements(self, ctx:niceParser.LElementsContext):
        pass

    # Exit a parse tree produced by niceParser#lElements.
    def exitLElements(self, ctx:niceParser.LElementsContext):
        pass


    # Enter a parse tree produced by niceParser#literal.
    def enterLiteral(self, ctx:niceParser.LiteralContext):
        pass

    # Exit a parse tree produced by niceParser#literal.
    def exitLiteral(self, ctx:niceParser.LiteralContext):
        pass



del niceParser