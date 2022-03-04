grammar nice;

code: statement;
statement: (assignment | expr) SEMICOLON;
assignment: 'var' value '=' expr;
expr: listSlice;

listSlice: value lSlice+;

lSlice: lAt | lFrom lFromTo | lFrom | lFromTo;
lAt: AT ((EVERY INT) | lIdxes);
lFrom: FROM INT;
lFromTo: TO INT;

lIdxes: INT (COMMA INT)*;

value: IDENTIFIER | literalList;

literalList: LSQBRT RSQBRT | LSQBRT lElements RSQBRT;

lElements: literal (COMMA literal)*;

literal: INT;

WS: [ \r\n\t]+ -> channel (HIDDEN);
// KEYWORDS
AT: 'at';
EVERY: 'every';
FROM: 'from';
TO: 'to';

// SYMBOLS
COMMA: ',';
LSQBRT: '[';
RSQBRT: ']';
SEMICOLON: ';';

// ignore whitespace
IDENTIFIER: [A-Za-z]+;
INT: '-'? ([1-9][0-9]* | [0-9]);
FLOAT: INT [.][0-9]*;
STRING: '"' .*? '"';