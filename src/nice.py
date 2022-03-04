from pprint import pprint
from antlr4 import *
from antlr4.tree.Trees import Trees
from niceLexer import niceLexer
from niceListener import niceListener
from niceParser import niceParser
import sys
import re

from pprint import pprint


class nicePrintListener(niceListener):
    def enterStmt(self, ctx: ParserRuleContext):
        print(f"nice: {ctx.toStringTree()}")


def toTree(s):
    s = s.replace('(', '( ').replace(')', ' ) ').split()
    l = ""
    for e in s:
        if e == '(':
            l += '('
        elif e == ')':
            l += ')'
        else:
            l += '"' + e + '",'
    l = re.sub(r",\)", ")", l)
    l = l.replace(')(', '),(').replace(')"', '),"')
    l = '[' + l[1:-1] + ']'
    return eval(l)


def main():
    # lexer = niceLexer(FileStream(sys.argv[1]))
    while True:
        # lexer = niceLexer(InputStream("alpha at 3;"))
        # lexer = niceLexer(StdinStream())
        lexer = niceLexer(InputStream(input("nice> ")))
        stream = CommonTokenStream(lexer)
        parser = niceParser(stream)
        tree = parser.code()
        printer = nicePrintListener()
        walker = ParseTreeWalker()
        # walker.walk(printer, tree)

        t = Trees.toStringTree(tree, None, parser)
        print(t)
        print()
        pprint(toTree(t), compact=True)

    # nest = 0
    # for c in t:
    #     if c == '(':
    #         nest += 1
    #     elif c == ')':
    #         nest -= 1
    #     if c == ' ':
    #         print('\n' + ('  ' * nest), end='')
    #     elif c == ',':
    #         print(c, end='')
    #     else:
    #         print(c, end='')
    # print()


if __name__ == '__main__':
    main()
