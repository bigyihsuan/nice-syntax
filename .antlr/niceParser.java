// Generated from /mnt/d/Programming/GithubRepos/nice-syntax/nice.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class niceParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, WS=7, AT=8, EVERY=9, FROM=10, 
		TO=11, IDENTIFIER=12, INT=13, FLOAT=14, STRING=15;
	public static final int
		RULE_code = 0, RULE_statement = 1, RULE_assignment = 2, RULE_expr = 3, 
		RULE_listSlice = 4, RULE_lSlice = 5, RULE_lAt = 6, RULE_lFrom = 7, RULE_lFromTo = 8, 
		RULE_lIdxes = 9, RULE_value = 10, RULE_literalList = 11, RULE_lElements = 12, 
		RULE_literal = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"code", "statement", "assignment", "expr", "listSlice", "lSlice", "lAt", 
			"lFrom", "lFromTo", "lIdxes", "value", "literalList", "lElements", "literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'var'", "'='", "','", "'['", "']'", null, "'at'", "'every'", 
			"'from'", "'to'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "WS", "AT", "EVERY", "FROM", 
			"TO", "IDENTIFIER", "INT", "FLOAT", "STRING"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "nice.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public niceParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class CodeContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_code; }
	}

	public final CodeContext code() throws RecognitionException {
		CodeContext _localctx = new CodeContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_code);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(28);
				statement();
				}
				}
				setState(31); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << IDENTIFIER))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				{
				setState(33);
				assignment();
				}
				break;
			case T__4:
			case IDENTIFIER:
				{
				setState(34);
				expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(37);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(T__1);
			setState(40);
			value();
			setState(41);
			match(T__2);
			setState(42);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ListSliceContext listSlice() {
			return getRuleContext(ListSliceContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			listSlice();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListSliceContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ListSliceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listSlice; }
	}

	public final ListSliceContext listSlice() throws RecognitionException {
		ListSliceContext _localctx = new ListSliceContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_listSlice);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LSliceContext extends ParserRuleContext {
		public LAtContext lAt() {
			return getRuleContext(LAtContext.class,0);
		}
		public LFromContext lFrom() {
			return getRuleContext(LFromContext.class,0);
		}
		public LFromToContext lFromTo() {
			return getRuleContext(LFromToContext.class,0);
		}
		public LSliceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lSlice; }
	}

	public final LSliceContext lSlice() throws RecognitionException {
		LSliceContext _localctx = new LSliceContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_lSlice);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AT) {
				{
				setState(48);
				lAt();
				}
			}

			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FROM) {
				{
				setState(51);
				lFrom();
				}
			}

			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TO) {
				{
				setState(54);
				lFromTo();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LAtContext extends ParserRuleContext {
		public TerminalNode AT() { return getToken(niceParser.AT, 0); }
		public LIdxesContext lIdxes() {
			return getRuleContext(LIdxesContext.class,0);
		}
		public TerminalNode EVERY() { return getToken(niceParser.EVERY, 0); }
		public TerminalNode INT() { return getToken(niceParser.INT, 0); }
		public LAtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lAt; }
	}

	public final LAtContext lAt() throws RecognitionException {
		LAtContext _localctx = new LAtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_lAt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(AT);
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EVERY:
				{
				{
				setState(58);
				match(EVERY);
				setState(59);
				match(INT);
				}
				}
				break;
			case INT:
				{
				setState(60);
				lIdxes();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LFromContext extends ParserRuleContext {
		public TerminalNode FROM() { return getToken(niceParser.FROM, 0); }
		public TerminalNode INT() { return getToken(niceParser.INT, 0); }
		public LFromContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lFrom; }
	}

	public final LFromContext lFrom() throws RecognitionException {
		LFromContext _localctx = new LFromContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_lFrom);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(FROM);
			setState(64);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LFromToContext extends ParserRuleContext {
		public TerminalNode TO() { return getToken(niceParser.TO, 0); }
		public TerminalNode INT() { return getToken(niceParser.INT, 0); }
		public LFromToContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lFromTo; }
	}

	public final LFromToContext lFromTo() throws RecognitionException {
		LFromToContext _localctx = new LFromToContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_lFromTo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(TO);
			setState(67);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LIdxesContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(niceParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(niceParser.INT, i);
		}
		public LIdxesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lIdxes; }
	}

	public final LIdxesContext lIdxes() throws RecognitionException {
		LIdxesContext _localctx = new LIdxesContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_lIdxes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(INT);
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(70);
				match(T__3);
				setState(71);
				match(INT);
				}
				}
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(niceParser.IDENTIFIER, 0); }
		public LiteralListContext literalList() {
			return getRuleContext(LiteralListContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_value);
		try {
			setState(79);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(IDENTIFIER);
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				literalList();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralListContext extends ParserRuleContext {
		public LElementsContext lElements() {
			return getRuleContext(LElementsContext.class,0);
		}
		public LiteralListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalList; }
	}

	public final LiteralListContext literalList() throws RecognitionException {
		LiteralListContext _localctx = new LiteralListContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_literalList);
		try {
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				match(T__4);
				setState(82);
				match(T__5);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				match(T__4);
				setState(84);
				lElements();
				setState(85);
				match(T__5);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LElementsContext extends ParserRuleContext {
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public LElementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lElements; }
	}

	public final LElementsContext lElements() throws RecognitionException {
		LElementsContext _localctx = new LElementsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_lElements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			literal();
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(90);
				match(T__3);
				setState(91);
				literal();
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(niceParser.INT, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21f\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\6\2 \n\2\r\2\16\2!\3\3\3\3\5\3"+
		"&\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\5\7\64\n\7\3\7\5"+
		"\7\67\n\7\3\7\5\7:\n\7\3\b\3\b\3\b\3\b\5\b@\n\b\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\7\13K\n\13\f\13\16\13N\13\13\3\f\3\f\5\fR\n\f\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\5\rZ\n\r\3\16\3\16\3\16\7\16_\n\16\f\16\16\16b\13\16"+
		"\3\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2\2a\2\37"+
		"\3\2\2\2\4%\3\2\2\2\6)\3\2\2\2\b.\3\2\2\2\n\60\3\2\2\2\f\63\3\2\2\2\16"+
		";\3\2\2\2\20A\3\2\2\2\22D\3\2\2\2\24G\3\2\2\2\26Q\3\2\2\2\30Y\3\2\2\2"+
		"\32[\3\2\2\2\34c\3\2\2\2\36 \5\4\3\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2"+
		"\2!\"\3\2\2\2\"\3\3\2\2\2#&\5\6\4\2$&\5\b\5\2%#\3\2\2\2%$\3\2\2\2&\'\3"+
		"\2\2\2\'(\7\3\2\2(\5\3\2\2\2)*\7\4\2\2*+\5\26\f\2+,\7\5\2\2,-\5\b\5\2"+
		"-\7\3\2\2\2./\5\n\6\2/\t\3\2\2\2\60\61\5\26\f\2\61\13\3\2\2\2\62\64\5"+
		"\16\b\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\67\5\20\t\2\66\65"+
		"\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28:\5\22\n\298\3\2\2\29:\3\2\2\2:\r\3"+
		"\2\2\2;?\7\n\2\2<=\7\13\2\2=@\7\17\2\2>@\5\24\13\2?<\3\2\2\2?>\3\2\2\2"+
		"@\17\3\2\2\2AB\7\f\2\2BC\7\17\2\2C\21\3\2\2\2DE\7\r\2\2EF\7\17\2\2F\23"+
		"\3\2\2\2GL\7\17\2\2HI\7\6\2\2IK\7\17\2\2JH\3\2\2\2KN\3\2\2\2LJ\3\2\2\2"+
		"LM\3\2\2\2M\25\3\2\2\2NL\3\2\2\2OR\7\16\2\2PR\5\30\r\2QO\3\2\2\2QP\3\2"+
		"\2\2R\27\3\2\2\2ST\7\7\2\2TZ\7\b\2\2UV\7\7\2\2VW\5\32\16\2WX\7\b\2\2X"+
		"Z\3\2\2\2YS\3\2\2\2YU\3\2\2\2Z\31\3\2\2\2[`\5\34\17\2\\]\7\6\2\2]_\5\34"+
		"\17\2^\\\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a\33\3\2\2\2b`\3\2\2\2c"+
		"d\7\17\2\2d\35\3\2\2\2\f!%\63\669?LQY`";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}