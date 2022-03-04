# Generated from nice.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\6\4)\n\4\r\4\16\4*\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\6\rI\n\r\r\r\16\rJ\3\16\5\16")
        buf.write("N\n\16\3\16\3\16\7\16R\n\16\f\16\16\16U\13\16\3\16\5\16")
        buf.write("X\n\16\3\17\3\17\3\17\7\17]\n\17\f\17\16\17`\13\17\3\20")
        buf.write("\3\20\7\20d\n\20\f\20\16\20g\13\20\3\20\3\20\3e\2\21\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21\3\2\7\5\2\13\f\17\17\"\"\4\2C\\c|\3")
        buf.write("\2\63;\3\2\62;\3\2\60\60\2p\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\3!\3\2\2\2\5%\3\2\2\2\7(\3\2\2\2\t.\3\2\2\2\13\61\3")
        buf.write("\2\2\2\r\67\3\2\2\2\17<\3\2\2\2\21?\3\2\2\2\23A\3\2\2")
        buf.write("\2\25C\3\2\2\2\27E\3\2\2\2\31H\3\2\2\2\33M\3\2\2\2\35")
        buf.write("Y\3\2\2\2\37a\3\2\2\2!\"\7x\2\2\"#\7c\2\2#$\7t\2\2$\4")
        buf.write("\3\2\2\2%&\7?\2\2&\6\3\2\2\2\')\t\2\2\2(\'\3\2\2\2)*\3")
        buf.write("\2\2\2*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\b\4\2\2-\b\3\2")
        buf.write("\2\2./\7c\2\2/\60\7v\2\2\60\n\3\2\2\2\61\62\7g\2\2\62")
        buf.write("\63\7x\2\2\63\64\7g\2\2\64\65\7t\2\2\65\66\7{\2\2\66\f")
        buf.write("\3\2\2\2\678\7h\2\289\7t\2\29:\7q\2\2:;\7o\2\2;\16\3\2")
        buf.write("\2\2<=\7v\2\2=>\7q\2\2>\20\3\2\2\2?@\7.\2\2@\22\3\2\2")
        buf.write("\2AB\7]\2\2B\24\3\2\2\2CD\7_\2\2D\26\3\2\2\2EF\7=\2\2")
        buf.write("F\30\3\2\2\2GI\t\3\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2J")
        buf.write("K\3\2\2\2K\32\3\2\2\2LN\7/\2\2ML\3\2\2\2MN\3\2\2\2NW\3")
        buf.write("\2\2\2OS\t\4\2\2PR\t\5\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2")
        buf.write("\2ST\3\2\2\2TX\3\2\2\2US\3\2\2\2VX\t\5\2\2WO\3\2\2\2W")
        buf.write("V\3\2\2\2X\34\3\2\2\2YZ\5\33\16\2Z^\t\6\2\2[]\t\5\2\2")
        buf.write("\\[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\36\3\2\2\2")
        buf.write("`^\3\2\2\2ae\7$\2\2bd\13\2\2\2cb\3\2\2\2dg\3\2\2\2ef\3")
        buf.write("\2\2\2ec\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\7$\2\2i \3\2\2")
        buf.write("\2\n\2*JMSW^e\3\2\3\2")
        return buf.getvalue()


class niceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    AT = 4
    EVERY = 5
    FROM = 6
    TO = 7
    COMMA = 8
    LSQBRT = 9
    RSQBRT = 10
    SEMICOLON = 11
    IDENTIFIER = 12
    INT = 13
    FLOAT = 14
    STRING = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'='", "'at'", "'every'", "'from'", "'to'", "','", 
            "'['", "']'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "AT", "EVERY", "FROM", "TO", "COMMA", "LSQBRT", "RSQBRT", 
            "SEMICOLON", "IDENTIFIER", "INT", "FLOAT", "STRING" ]

    ruleNames = [ "T__0", "T__1", "WS", "AT", "EVERY", "FROM", "TO", "COMMA", 
                  "LSQBRT", "RSQBRT", "SEMICOLON", "IDENTIFIER", "INT", 
                  "FLOAT", "STRING" ]

    grammarFileName = "nice.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


