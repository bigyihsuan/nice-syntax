# Generated from equation.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .equationParser import equationParser
else:
    from equationParser import equationParser

# This class defines a complete listener for a parse tree produced by equationParser.
class equationListener(ParseTreeListener):

    # Enter a parse tree produced by equationParser#expression.
    def enterExpression(self, ctx:equationParser.ExpressionContext):
        pass

    # Exit a parse tree produced by equationParser#expression.
    def exitExpression(self, ctx:equationParser.ExpressionContext):
        pass


    # Enter a parse tree produced by equationParser#term.
    def enterTerm(self, ctx:equationParser.TermContext):
        pass

    # Exit a parse tree produced by equationParser#term.
    def exitTerm(self, ctx:equationParser.TermContext):
        pass


    # Enter a parse tree produced by equationParser#factor.
    def enterFactor(self, ctx:equationParser.FactorContext):
        pass

    # Exit a parse tree produced by equationParser#factor.
    def exitFactor(self, ctx:equationParser.FactorContext):
        pass


    # Enter a parse tree produced by equationParser#primary.
    def enterPrimary(self, ctx:equationParser.PrimaryContext):
        pass

    # Exit a parse tree produced by equationParser#primary.
    def exitPrimary(self, ctx:equationParser.PrimaryContext):
        pass



del equationParser