# Generated from equation.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .equationParser import equationParser
else:
    from equationParser import equationParser

# This class defines a complete generic visitor for a parse tree produced by equationParser.

class equationVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by equationParser#expression.
    def visitExpression(self, ctx:equationParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by equationParser#term.
    def visitTerm(self, ctx:equationParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by equationParser#factor.
    def visitFactor(self, ctx:equationParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by equationParser#primary.
    def visitPrimary(self, ctx:equationParser.PrimaryContext):
        return self.visitChildren(ctx)



del equationParser