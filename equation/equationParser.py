# Generated from equation.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\"\n\3\f\3\16\3%\13\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\63\n\5\3\5\2\4\2\4\6\2\4\6\b\2\2\2\67\2\n\3\2\2\2\4\30")
        buf.write("\3\2\2\2\6+\3\2\2\2\b\62\3\2\2\2\n\13\b\2\1\2\13\f\5\4")
        buf.write("\3\2\f\25\3\2\2\2\r\16\f\4\2\2\16\17\7\4\2\2\17\24\5\4")
        buf.write("\3\2\20\21\f\3\2\2\21\22\7\5\2\2\22\24\5\4\3\2\23\r\3")
        buf.write("\2\2\2\23\20\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26")
        buf.write("\3\2\2\2\26\3\3\2\2\2\27\25\3\2\2\2\30\31\b\3\1\2\31\32")
        buf.write("\5\6\4\2\32#\3\2\2\2\33\34\f\4\2\2\34\35\7\6\2\2\35\"")
        buf.write("\5\6\4\2\36\37\f\3\2\2\37 \7\7\2\2 \"\5\6\4\2!\33\3\2")
        buf.write("\2\2!\36\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\5\3\2")
        buf.write("\2\2%#\3\2\2\2&,\5\b\5\2\'(\7\5\2\2(,\5\6\4\2)*\7\4\2")
        buf.write("\2*,\5\6\4\2+&\3\2\2\2+\'\3\2\2\2+)\3\2\2\2,\7\3\2\2\2")
        buf.write("-\63\7\3\2\2./\7\b\2\2/\60\5\2\2\2\60\61\7\t\2\2\61\63")
        buf.write("\3\2\2\2\62-\3\2\2\2\62.\3\2\2\2\63\t\3\2\2\2\b\23\25")
        buf.write("!#+\62")
        return buf.getvalue()


class equationParser ( Parser ):

    grammarFileName = "equation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "PLUS", "MINUS", "STAR", "SLASH", 
                      "LPAREN", "RPAREN", "WS" ]

    RULE_expression = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_primary = 3

    ruleNames =  [ "expression", "term", "factor", "primary" ]

    EOF = Token.EOF
    INT=1
    PLUS=2
    MINUS=3
    STAR=4
    SLASH=5
    LPAREN=6
    RPAREN=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(equationParser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(equationParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(equationParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(equationParser.MINUS, 0)

        def getRuleIndex(self):
            return equationParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = equationParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 17
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = equationParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 11
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 12
                        self.match(equationParser.PLUS)
                        self.state = 13
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = equationParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 14
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 15
                        self.match(equationParser.MINUS)
                        self.state = 16
                        self.term(0)
                        pass

             
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(equationParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(equationParser.TermContext,0)


        def STAR(self):
            return self.getToken(equationParser.STAR, 0)

        def SLASH(self):
            return self.getToken(equationParser.SLASH, 0)

        def getRuleIndex(self):
            return equationParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = equationParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = equationParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 25
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 26
                        self.match(equationParser.STAR)
                        self.state = 27
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = equationParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 28
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 29
                        self.match(equationParser.SLASH)
                        self.state = 30
                        self.factor()
                        pass

             
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(equationParser.PrimaryContext,0)


        def MINUS(self):
            return self.getToken(equationParser.MINUS, 0)

        def factor(self):
            return self.getTypedRuleContext(equationParser.FactorContext,0)


        def PLUS(self):
            return self.getToken(equationParser.PLUS, 0)

        def getRuleIndex(self):
            return equationParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = equationParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [equationParser.INT, equationParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.primary()
                pass
            elif token in [equationParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(equationParser.MINUS)
                self.state = 38
                self.factor()
                pass
            elif token in [equationParser.PLUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(equationParser.PLUS)
                self.state = 40
                self.factor()
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


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(equationParser.INT, 0)

        def LPAREN(self):
            return self.getToken(equationParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(equationParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(equationParser.RPAREN, 0)

        def getRuleIndex(self):
            return equationParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = equationParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primary)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [equationParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(equationParser.INT)
                pass
            elif token in [equationParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(equationParser.LPAREN)
                self.state = 45
                self.expression(0)
                self.state = 46
                self.match(equationParser.RPAREN)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        self._predicates[1] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




