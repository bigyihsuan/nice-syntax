# Generated from nice.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\3\3\3\5\3#\n\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\6\3\6\6\6\60\n\6\r\6\16\6\61\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\5\7:\n\7\3\b\3\b\3\b\3\b\5\b@\n")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\7\13K\n\13\f")
        buf.write("\13\16\13N\13\13\3\f\3\f\5\fR\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\rZ\n\r\3\16\3\16\3\16\7\16_\n\16\f\16\16\16b\13")
        buf.write("\16\3\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\2\2\2a\2\36\3\2\2\2\4\"\3\2\2\2\6&\3\2\2\2\b+\3")
        buf.write("\2\2\2\n-\3\2\2\2\f9\3\2\2\2\16;\3\2\2\2\20A\3\2\2\2\22")
        buf.write("D\3\2\2\2\24G\3\2\2\2\26Q\3\2\2\2\30Y\3\2\2\2\32[\3\2")
        buf.write("\2\2\34c\3\2\2\2\36\37\5\4\3\2\37\3\3\2\2\2 #\5\6\4\2")
        buf.write("!#\5\b\5\2\" \3\2\2\2\"!\3\2\2\2#$\3\2\2\2$%\7\r\2\2%")
        buf.write("\5\3\2\2\2&\'\7\3\2\2\'(\5\26\f\2()\7\4\2\2)*\5\b\5\2")
        buf.write("*\7\3\2\2\2+,\5\n\6\2,\t\3\2\2\2-/\5\26\f\2.\60\5\f\7")
        buf.write("\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62")
        buf.write("\13\3\2\2\2\63:\5\16\b\2\64\65\5\20\t\2\65\66\5\22\n\2")
        buf.write("\66:\3\2\2\2\67:\5\20\t\28:\5\22\n\29\63\3\2\2\29\64\3")
        buf.write("\2\2\29\67\3\2\2\298\3\2\2\2:\r\3\2\2\2;?\7\6\2\2<=\7")
        buf.write("\7\2\2=@\7\17\2\2>@\5\24\13\2?<\3\2\2\2?>\3\2\2\2@\17")
        buf.write("\3\2\2\2AB\7\b\2\2BC\7\17\2\2C\21\3\2\2\2DE\7\t\2\2EF")
        buf.write("\7\17\2\2F\23\3\2\2\2GL\7\17\2\2HI\7\n\2\2IK\7\17\2\2")
        buf.write("JH\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\25\3\2\2\2N")
        buf.write("L\3\2\2\2OR\7\16\2\2PR\5\30\r\2QO\3\2\2\2QP\3\2\2\2R\27")
        buf.write("\3\2\2\2ST\7\13\2\2TZ\7\f\2\2UV\7\13\2\2VW\5\32\16\2W")
        buf.write("X\7\f\2\2XZ\3\2\2\2YS\3\2\2\2YU\3\2\2\2Z\31\3\2\2\2[`")
        buf.write("\5\34\17\2\\]\7\n\2\2]_\5\34\17\2^\\\3\2\2\2_b\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2a\33\3\2\2\2b`\3\2\2\2cd\7\17\2\2")
        buf.write("d\35\3\2\2\2\n\"\619?LQY`")
        return buf.getvalue()


class niceParser ( Parser ):

    grammarFileName = "nice.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'='", "<INVALID>", "'at'", "'every'", 
                     "'from'", "'to'", "','", "'['", "']'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "AT", 
                      "EVERY", "FROM", "TO", "COMMA", "LSQBRT", "RSQBRT", 
                      "SEMICOLON", "IDENTIFIER", "INT", "FLOAT", "STRING" ]

    RULE_code = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_listSlice = 4
    RULE_lSlice = 5
    RULE_lAt = 6
    RULE_lFrom = 7
    RULE_lFromTo = 8
    RULE_lIdxes = 9
    RULE_value = 10
    RULE_literalList = 11
    RULE_lElements = 12
    RULE_literal = 13

    ruleNames =  [ "code", "statement", "assignment", "expr", "listSlice", 
                   "lSlice", "lAt", "lFrom", "lFromTo", "lIdxes", "value", 
                   "literalList", "lElements", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    AT=4
    EVERY=5
    FROM=6
    TO=7
    COMMA=8
    LSQBRT=9
    RSQBRT=10
    SEMICOLON=11
    IDENTIFIER=12
    INT=13
    FLOAT=14
    STRING=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(niceParser.StatementContext,0)


        def getRuleIndex(self):
            return niceParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = niceParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(niceParser.SEMICOLON, 0)

        def assignment(self):
            return self.getTypedRuleContext(niceParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(niceParser.ExprContext,0)


        def getRuleIndex(self):
            return niceParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = niceParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [niceParser.T__0]:
                self.state = 30
                self.assignment()
                pass
            elif token in [niceParser.LSQBRT, niceParser.IDENTIFIER]:
                self.state = 31
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 34
            self.match(niceParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(niceParser.ValueContext,0)


        def expr(self):
            return self.getTypedRuleContext(niceParser.ExprContext,0)


        def getRuleIndex(self):
            return niceParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = niceParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(niceParser.T__0)
            self.state = 37
            self.value()
            self.state = 38
            self.match(niceParser.T__1)
            self.state = 39
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listSlice(self):
            return self.getTypedRuleContext(niceParser.ListSliceContext,0)


        def getRuleIndex(self):
            return niceParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = niceParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.listSlice()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListSliceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(niceParser.ValueContext,0)


        def lSlice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(niceParser.LSliceContext)
            else:
                return self.getTypedRuleContext(niceParser.LSliceContext,i)


        def getRuleIndex(self):
            return niceParser.RULE_listSlice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListSlice" ):
                listener.enterListSlice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListSlice" ):
                listener.exitListSlice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListSlice" ):
                return visitor.visitListSlice(self)
            else:
                return visitor.visitChildren(self)




    def listSlice(self):

        localctx = niceParser.ListSliceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listSlice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.value()
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.lSlice()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << niceParser.AT) | (1 << niceParser.FROM) | (1 << niceParser.TO))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LSliceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lAt(self):
            return self.getTypedRuleContext(niceParser.LAtContext,0)


        def lFrom(self):
            return self.getTypedRuleContext(niceParser.LFromContext,0)


        def lFromTo(self):
            return self.getTypedRuleContext(niceParser.LFromToContext,0)


        def getRuleIndex(self):
            return niceParser.RULE_lSlice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLSlice" ):
                listener.enterLSlice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLSlice" ):
                listener.exitLSlice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLSlice" ):
                return visitor.visitLSlice(self)
            else:
                return visitor.visitChildren(self)




    def lSlice(self):

        localctx = niceParser.LSliceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lSlice)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.lAt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.lFrom()
                self.state = 51
                self.lFromTo()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.lFrom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.lFromTo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LAtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(niceParser.AT, 0)

        def lIdxes(self):
            return self.getTypedRuleContext(niceParser.LIdxesContext,0)


        def EVERY(self):
            return self.getToken(niceParser.EVERY, 0)

        def INT(self):
            return self.getToken(niceParser.INT, 0)

        def getRuleIndex(self):
            return niceParser.RULE_lAt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLAt" ):
                listener.enterLAt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLAt" ):
                listener.exitLAt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLAt" ):
                return visitor.visitLAt(self)
            else:
                return visitor.visitChildren(self)




    def lAt(self):

        localctx = niceParser.LAtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lAt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(niceParser.AT)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [niceParser.EVERY]:
                self.state = 58
                self.match(niceParser.EVERY)
                self.state = 59
                self.match(niceParser.INT)
                pass
            elif token in [niceParser.INT]:
                self.state = 60
                self.lIdxes()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LFromContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(niceParser.FROM, 0)

        def INT(self):
            return self.getToken(niceParser.INT, 0)

        def getRuleIndex(self):
            return niceParser.RULE_lFrom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLFrom" ):
                listener.enterLFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLFrom" ):
                listener.exitLFrom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLFrom" ):
                return visitor.visitLFrom(self)
            else:
                return visitor.visitChildren(self)




    def lFrom(self):

        localctx = niceParser.LFromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lFrom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(niceParser.FROM)
            self.state = 64
            self.match(niceParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LFromToContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TO(self):
            return self.getToken(niceParser.TO, 0)

        def INT(self):
            return self.getToken(niceParser.INT, 0)

        def getRuleIndex(self):
            return niceParser.RULE_lFromTo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLFromTo" ):
                listener.enterLFromTo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLFromTo" ):
                listener.exitLFromTo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLFromTo" ):
                return visitor.visitLFromTo(self)
            else:
                return visitor.visitChildren(self)




    def lFromTo(self):

        localctx = niceParser.LFromToContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lFromTo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(niceParser.TO)
            self.state = 67
            self.match(niceParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LIdxesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(niceParser.INT)
            else:
                return self.getToken(niceParser.INT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(niceParser.COMMA)
            else:
                return self.getToken(niceParser.COMMA, i)

        def getRuleIndex(self):
            return niceParser.RULE_lIdxes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLIdxes" ):
                listener.enterLIdxes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLIdxes" ):
                listener.exitLIdxes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLIdxes" ):
                return visitor.visitLIdxes(self)
            else:
                return visitor.visitChildren(self)




    def lIdxes(self):

        localctx = niceParser.LIdxesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lIdxes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(niceParser.INT)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==niceParser.COMMA:
                self.state = 70
                self.match(niceParser.COMMA)
                self.state = 71
                self.match(niceParser.INT)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(niceParser.IDENTIFIER, 0)

        def literalList(self):
            return self.getTypedRuleContext(niceParser.LiteralListContext,0)


        def getRuleIndex(self):
            return niceParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = niceParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [niceParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(niceParser.IDENTIFIER)
                pass
            elif token in [niceParser.LSQBRT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.literalList()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQBRT(self):
            return self.getToken(niceParser.LSQBRT, 0)

        def RSQBRT(self):
            return self.getToken(niceParser.RSQBRT, 0)

        def lElements(self):
            return self.getTypedRuleContext(niceParser.LElementsContext,0)


        def getRuleIndex(self):
            return niceParser.RULE_literalList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralList" ):
                listener.enterLiteralList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralList" ):
                listener.exitLiteralList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralList" ):
                return visitor.visitLiteralList(self)
            else:
                return visitor.visitChildren(self)




    def literalList(self):

        localctx = niceParser.LiteralListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literalList)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(niceParser.LSQBRT)
                self.state = 82
                self.match(niceParser.RSQBRT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(niceParser.LSQBRT)
                self.state = 84
                self.lElements()
                self.state = 85
                self.match(niceParser.RSQBRT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(niceParser.LiteralContext)
            else:
                return self.getTypedRuleContext(niceParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(niceParser.COMMA)
            else:
                return self.getToken(niceParser.COMMA, i)

        def getRuleIndex(self):
            return niceParser.RULE_lElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLElements" ):
                listener.enterLElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLElements" ):
                listener.exitLElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLElements" ):
                return visitor.visitLElements(self)
            else:
                return visitor.visitChildren(self)




    def lElements(self):

        localctx = niceParser.LElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_lElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.literal()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==niceParser.COMMA:
                self.state = 90
                self.match(niceParser.COMMA)
                self.state = 91
                self.literal()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(niceParser.INT, 0)

        def getRuleIndex(self):
            return niceParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = niceParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(niceParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





