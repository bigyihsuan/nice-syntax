// Generated from /mnt/d/Programming/GithubRepos/nice-syntax/nice.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class niceLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, WS=7, AT=8, EVERY=9, FROM=10, 
		TO=11, IDENTIFIER=12, INT=13, FLOAT=14, STRING=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "WS", "AT", "EVERY", 
			"FROM", "TO", "IDENTIFIER", "INT", "FLOAT", "STRING"
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


	public niceLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "nice.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21j\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\3"+
		"\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b\61\n\b\r\b\16\b\62\3\b\3"+
		"\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3"+
		"\f\3\f\3\r\6\rI\n\r\r\r\16\rJ\3\16\5\16N\n\16\3\16\3\16\7\16R\n\16\f\16"+
		"\16\16U\13\16\3\16\5\16X\n\16\3\17\3\17\3\17\7\17]\n\17\f\17\16\17`\13"+
		"\17\3\20\3\20\7\20d\n\20\f\20\16\20g\13\20\3\20\3\20\3e\2\21\3\3\5\4\7"+
		"\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2"+
		"\7\5\2\13\f\17\17\"\"\4\2C\\c|\3\2\63;\3\2\62;\3\2\60\60\2p\2\3\3\2\2"+
		"\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3"+
		"\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2"+
		"\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7\'\3"+
		"\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17\60\3\2\2\2\21\66\3\2\2\2\23"+
		"9\3\2\2\2\25?\3\2\2\2\27D\3\2\2\2\31H\3\2\2\2\33M\3\2\2\2\35Y\3\2\2\2"+
		"\37a\3\2\2\2!\"\7=\2\2\"\4\3\2\2\2#$\7x\2\2$%\7c\2\2%&\7t\2\2&\6\3\2\2"+
		"\2\'(\7?\2\2(\b\3\2\2\2)*\7.\2\2*\n\3\2\2\2+,\7]\2\2,\f\3\2\2\2-.\7_\2"+
		"\2.\16\3\2\2\2/\61\t\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62"+
		"\63\3\2\2\2\63\64\3\2\2\2\64\65\b\b\2\2\65\20\3\2\2\2\66\67\7c\2\2\67"+
		"8\7v\2\28\22\3\2\2\29:\7g\2\2:;\7x\2\2;<\7g\2\2<=\7t\2\2=>\7{\2\2>\24"+
		"\3\2\2\2?@\7h\2\2@A\7t\2\2AB\7q\2\2BC\7o\2\2C\26\3\2\2\2DE\7v\2\2EF\7"+
		"q\2\2F\30\3\2\2\2GI\t\3\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\32"+
		"\3\2\2\2LN\7/\2\2ML\3\2\2\2MN\3\2\2\2NW\3\2\2\2OS\t\4\2\2PR\t\5\2\2QP"+
		"\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TX\3\2\2\2US\3\2\2\2VX\t\5\2\2W"+
		"O\3\2\2\2WV\3\2\2\2X\34\3\2\2\2YZ\5\33\16\2Z^\t\6\2\2[]\t\5\2\2\\[\3\2"+
		"\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\36\3\2\2\2`^\3\2\2\2ae\7$\2\2bd\13"+
		"\2\2\2cb\3\2\2\2dg\3\2\2\2ef\3\2\2\2ec\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\7"+
		"$\2\2i \3\2\2\2\n\2\62JMSW^e\3\2\3\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}