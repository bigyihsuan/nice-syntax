# Generated from equation.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\5\2\25\n\2\3\2\3\2\7\2\31\n\2\f")
        buf.write("\2\16\2\34\13\2\3\2\5\2\37\n\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t.\n\t\r\t\16\t/\3\t\3")
        buf.write("\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\5\3\2")
        buf.write("\63;\3\2\62;\5\2\13\f\17\17\"\"\2\66\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\3\24\3\2\2\2\5 \3\2\2\2\7")
        buf.write("\"\3\2\2\2\t$\3\2\2\2\13&\3\2\2\2\r(\3\2\2\2\17*\3\2\2")
        buf.write("\2\21-\3\2\2\2\23\25\5\7\4\2\24\23\3\2\2\2\24\25\3\2\2")
        buf.write("\2\25\36\3\2\2\2\26\32\t\2\2\2\27\31\t\3\2\2\30\27\3\2")
        buf.write("\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\37\3")
        buf.write("\2\2\2\34\32\3\2\2\2\35\37\t\3\2\2\36\26\3\2\2\2\36\35")
        buf.write("\3\2\2\2\37\4\3\2\2\2 !\7-\2\2!\6\3\2\2\2\"#\7/\2\2#\b")
        buf.write("\3\2\2\2$%\7,\2\2%\n\3\2\2\2&\'\7\61\2\2\'\f\3\2\2\2(")
        buf.write(")\7*\2\2)\16\3\2\2\2*+\7+\2\2+\20\3\2\2\2,.\t\4\2\2-,")
        buf.write("\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2")
        buf.write("\61\62\b\t\2\2\62\22\3\2\2\2\7\2\24\32\36/\3\2\3\2")
        return buf.getvalue()


class equationLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    PLUS = 2
    MINUS = 3
    STAR = 4
    SLASH = 5
    LPAREN = 6
    RPAREN = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "PLUS", "MINUS", "STAR", "SLASH", "LPAREN", "RPAREN", 
            "WS" ]

    ruleNames = [ "INT", "PLUS", "MINUS", "STAR", "SLASH", "LPAREN", "RPAREN", 
                  "WS" ]

    grammarFileName = "equation.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


