from antlr4 import *
from antlr4.tree.Trees import Trees
from equationLexer import equationLexer
from equationListener import equationListener
from equationParser import equationParser
import sys
import re


class equationPrintListener(equationListener):
    def enterExpression(self, ctx: ParserRuleContext):
        print(f"equation: {ctx.toStringTree()}")


def main():
    lexer = equationLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = equationParser(stream)
    tree = parser.expression()
    printer = equationPrintListener()
    walker = ParseTreeWalker()
    # walker.walk(printer, tree)

    t = Trees.toStringTree(tree, None, parser)
    nest = 0
    for c in t:
        if c == '(':
            nest += 1
        elif c == ')':
            nest -= 1
        if c == ' ':
            print('\n' + (' ' * nest), end='')
        else:
            print(c, end='')
    print()


if __name__ == '__main__':
    main()
