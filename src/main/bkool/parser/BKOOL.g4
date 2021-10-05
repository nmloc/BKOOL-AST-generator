/*
 * Student's name: Nguyen Minh Loc
 * Student ID: 1852554
 */
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}
/*-------------------Program Structure-------------------*/
program: (classDecl)+ EOF;

typ: BOOLEAN | INT | FLOAT | STRING | arrTyp;
arrTyp: (BOOLEAN | INT | FLOAT | STRING | objTyp) LSB INT_LIT RSB;

//classDecl
classDecl: CLASS className (EXTENDS ID)? LP classMem* RP;
className: ID;
classMem: attributeDecl | methodDecl | constructor | mainMethod | voidMethod;

//attributeDecl
attributeDecl: mutableAttribute | immutableAttribute | objAttribute;
mutableAttribute: STATIC? typ ID muInit (COMMA ID muInit)* SEMI;
muInit: (EQUAL_SIGN exp)?;
immutableAttribute: (FINAL | STATIC FINAL | FINAL STATIC) typ ID immuInit (COMMA ID immuInit)* SEMI;
immuInit: EQUAL_SIGN exp;
objAttribute: STATIC? objTyp ID objInit (COMMA ID objInit)* SEMI;
objTyp: ID;
objInit: (EQUAL_SIGN exp10)?;

//methodDecl
methodDecl: STATIC? typ ID LB paraList? RB stmtBlock;
paraList: paraInit (SEMI paraInit)*;
paraInit: typ ID (COMMA ID)*;

//special method
constructor: className LB paraList? RB stmtBlock_constructor;
mainMethod: STATIC? VOID 'main' LB RB stmtBlock_wo_return;
voidMethod: STATIC? VOID ID LB paraList? RB stmtBlock_wo_return;


/*-------------------expession-------------------*/
stmt: asmStmt
	| ifStmt
	| forStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| method_invo
	| stmtBlock
	;

stmt_wo_return: asmStmt
			  | ifStmt
			  | forStmt
			  | breakStmt
			  | continueStmt
			  | method_invo
			  | stmtBlock_wo_return
			  ;

exp: exp (LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) exp	| exp1;
exp1: exp1 (EQUAL | NOT_EQUAL) exp1 								| exp2;
exp2: exp2 (AND | OR) exp3 											| exp3;
exp3: exp3 (ADDOP | SUBOP) exp4 									| exp4;
exp4: exp4 (MULOP | I_DIV | F_DIV | MOD) exp5 						| exp5;
exp5: exp5 CONCATENATION exp6 										| exp6;
exp6: NOT exp6 														| exp7;
exp7: (ADDOP | SUBOP) exp7 											| exp8;
exp8: exp8 LSB exp8 RSB 											| exp9;
exp9: exp9 DOT exp10 expListWithBrackets? 							| exp10;
exp10: NEW exp10 LB expList? RB 									| exp11;
exp11: atom | method_invo | asmStmt;

atom: LB expList RB | literal | THIS | ID;
expList: (exp (COMMA exp)*);
expListWithBrackets: (LB (exp (COMMA exp)*)? RB);


/*-------------------VarDecl-------------------*/

varDecl: mutableVar | immutableVar | objVar;
mutableVar: typ ID muInit (COMMA ID muInit)* SEMI;
immutableVar: FINAL? typ ID immuInit (COMMA ID immuInit)* SEMI;
objVar: objTyp ID objInit (COMMA ID objInit)* SEMI;


/*-------------------VarDecl for constructor-------------------*/

varDecl_constructor: mutableVar_constructor | immutableVar | objVar;
mutableVar_constructor: typ ID cstInit (COMMA ID cstInit)* SEMI;
cstInit: (EQUAL_SIGN exp)?;


/*-------------------Statement-------------------*/

//block statement
stmtBlock: LP (varDecl | stmt)* RP;
stmtBlock_wo_return: LP (varDecl | stmt_wo_return)* RP;
stmtBlock_constructor: LP (varDecl_constructor | stmt_wo_return)* RP;

//assignment statement
asmStmt: lhs ASSIGN exp SEMI;
lhs: ID | (ID|THIS) DOT (ID|ID LSB exp RSB) | ID LSB exp RSB;

//if statement
ifStmt: IF exp THEN stmt (ELSE stmt)?;

//for statement
forStmt: FOR ID ASSIGN exp (TO|DOWNTO) exp DO stmt;

//break statement
breakStmt: BREAK SEMI;

//continue statement
continueStmt: CONTINUE SEMI;

//return statement
returnStmt: RETURN exp SEMI;

//method invocation statement
method_invo: (ID|THIS) DOT exp expListWithBrackets? SEMI;

/*-------------------Lexical Structure-------------------*/

//comment
COMMENT_LINE   : '#' ~ [\r\n]* ('\r'? '\n' | EOF) -> skip ;
COMMENT_BLOCK  : '/*' .*? '*/' -> skip;

//keyword
BOOLEAN: 'boolean';
INT: 'int';
FLOAT: 'float';
VOID: 'void';
STRING: 'string';
NEW: 'new';
IF: 'if';
ELSE: 'else';
THEN: 'then';
CONTINUE: 'continue';
BREAK: 'break';
FOR: 'for';
DO: 'do';
TO: 'to';
DOWNTO: 'downto';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
CLASS: 'class';
EXTENDS: 'extends';
STATIC: 'static';
FINAL: 'final';
NIL: 'nil';
THIS: 'this';

//operator
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
I_DIV: '/';
F_DIV: '\\';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LESS: '<'	;
GREATER: '>';
LESS_OR_EQUAL: '<=';
GREATER_OR_EQUAL: '>=';	
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
EQUAL_SIGN: '=';
ASSIGN: ':=';

//separator
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

//literal
literal: FLOAT_LIT | INT_LIT | bool_lit | STRING_LIT | arr_lit;
INT_LIT: DIGIT+;
bool_lit: TRUE | FALSE;
arr_lit: LP arr_value (COMMA arr_value)* RP;
arr_value: (INT_LIT | FLOAT_LIT | bool_lit | STRING_LIT);
FLOAT_LIT: INT_LIT DECIMAL? EXPONENT?;

STRING_LIT: '"' CHAR* '"'
{
	temp = str(self.text)
	self.text = temp[1:-1]
};

//character set
fragment EXPONENT: [eE] (ADDOP | SUBOP)? DIGIT+;
fragment DECIMAL: DOT DIGIT*;
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];
fragment CHAR: ESC | ~ [\r\n\\"];
fragment ESC: '\\' ([btnfr"\\]);
fragment ILL_ESC: '\\' ~([btnfr"\\]) | ~'\\';
ID: (UNDERSCORE | LETTER) (UNDERSCORE | LETTER | DIGIT)*;
WS: [ \t\n\f\r] -> skip;

/*-------------------Lexical Errors-------------------*/

UNCLOSE_STRING: '"' CHAR* ([\r\nEOF] | ~'"')
{
	err_char = ['\r','\n',EOFError]
	if self.text[-1] in err_char:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' CHAR* ILL_ESC
{
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . 
{
	raise ErrorToken(self.text)
};