grammar equation;

expression: term | expression PLUS term | expression MINUS term;
term: factor | term STAR factor | term SLASH factor;
factor: primary | MINUS factor | PLUS factor;
primary: INT | LPAREN expression RPAREN;

INT: MINUS? ([1-9][0-9]* | [0-9]);

PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
LPAREN: '(';
RPAREN: ')';

WS: [ \r\n\t]+ -> channel (HIDDEN);