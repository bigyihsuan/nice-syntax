# Generated from nice.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .niceParser import niceParser
else:
    from niceParser import niceParser

# This class defines a complete generic visitor for a parse tree produced by niceParser.

class niceVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by niceParser#code.
    def visitCode(self, ctx:niceParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#statement.
    def visitStatement(self, ctx:niceParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#assignment.
    def visitAssignment(self, ctx:niceParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#expr.
    def visitExpr(self, ctx:niceParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#listSlice.
    def visitListSlice(self, ctx:niceParser.ListSliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#lSlice.
    def visitLSlice(self, ctx:niceParser.LSliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#lAt.
    def visitLAt(self, ctx:niceParser.LAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#lFrom.
    def visitLFrom(self, ctx:niceParser.LFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#lFromTo.
    def visitLFromTo(self, ctx:niceParser.LFromToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#lIdxes.
    def visitLIdxes(self, ctx:niceParser.LIdxesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#value.
    def visitValue(self, ctx:niceParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#literalList.
    def visitLiteralList(self, ctx:niceParser.LiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#lElements.
    def visitLElements(self, ctx:niceParser.LElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by niceParser#literal.
    def visitLiteral(self, ctx:niceParser.LiteralContext):
        return self.visitChildren(ctx)



del niceParser