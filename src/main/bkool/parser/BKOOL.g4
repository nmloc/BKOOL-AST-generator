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

typ: BOOLEAN | INT | FLOAT | STRING;

//classDecl
classDecl: CLASS className (EXTENDS ID)? LP classMem* RP;
className: ID;
classMem: attributeDecl | methodDecl | constructor | mainMethod;

//attributeDecl
attributeDecl: mutableAttribute | immutableAttribute | arrDecl | objDecl;
mutableAttribute: STATIC? typ ID muAttrInit (COMMA ID muAttrInit)* SEMI;
muAttrInit: (EQUAL_SIGN expr)?;
immutableAttribute: (FINAL | STATIC FINAL | FINAL STATIC) typ ID immuAttrInit (COMMA ID immuAttrInit)* SEMI;
immuAttrInit: EQUAL_SIGN expr;

//methodDecl
methodDecl: STATIC? (typ | VOID) ID LB paraList? RB (stmtBlock | stmtBlock_wo_return);
paraList: paraInit (SEMI paraInit)*;
paraInit: typ ID (COMMA ID)*;

//special method
constructor: className LB paraList? RB stmtBlock_wo_return;
mainMethod: STATIC? VOID 'main' LB RB stmtBlock_wo_return;

//arr_decl
arrDecl: arrTyp ID SEMI;

//object_decl
objDecl: className objMem SEMI;
objMem: objName (COMMA objName)*;
objName: ID (EQUAL_SIGN ID)?;

/*-------------------Type-------------------*/

//array
arrTyp: typ LSB INT_LIT RSB;

/*-------------------Expression-------------------*/
stmt: asmStmt
	| ifStmt
	| forStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| method_invo
	| invokeStmt
	| stmtBlock
	;

stmt_wo_return: asmStmt
			  | ifStmt
			  | forStmt
			  | breakStmt
			  | continueStmt
			  | method_invo
			  | invokeStmt
			  | stmtBlock
			  ;

expr: expr (LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) expr | expr1;
expr1: expr1 (EQUAL | NOT_EQUAL) expr1 								| expr2;
expr2: expr2 (AND | OR) expr3 										| expr3;
expr3: expr3 (ADDOP | SUBOP) expr4 									| expr4;
expr4: expr4 (MULOP | I_DIV | F_DIV | MOD) expr5 					| expr5;
expr5: expr5 CONCATENATION expr6 									| expr6;
expr6: NOT expr6 													| expr7;
expr7: (ADDOP | SUBOP) expr7 										| expr8;
expr8: expr8 LSB expr8 RSB 											| expr9;
expr9: expr9 DOT expr10 exprListWithBrackets? 						| expr10;
expr10: NEW expr10 LB exprList? RB 									| expr11;
expr11: atom | method_invo | asmStmt | invokeStmt;

atom: LB expr RB | literal | THIS | ID;
exprList: (expr (COMMA expr)*);
exprListWithBrackets: (LB (expr (COMMA expr)*)? RB);

/*-------------------Statement-------------------*/

//block statement
stmtBlock: LP (attributeDecl | arrDecl | objDecl | stmt)* RP;
stmtBlock_wo_return: LP (attributeDecl | arrDecl | objDecl | stmt_wo_return)* RP;

//assignment statement
asmStmt: lhs ASSIGN expr SEMI;
lhs: ID | (ID|THIS) DOT (ID|ID LSB expr RSB) | ID LSB expr RSB;

//if statement
ifStmt: IF expr THEN stmt (ELSE stmt)?;

//for statement
forStmt: FOR ID ASSIGN expr (TO|DOWNTO) expr DO stmt;

//break statement
breakStmt: BREAK SEMI;

//continue statement
continueStmt: CONTINUE SEMI;

//return statement
returnStmt: RETURN expr SEMI;

//method invocation statement
method_invo: (ID|THIS) DOT expr exprListWithBrackets? SEMI;

//invoke statement
invokeStmt: ID LB arguList? RB;
arguList: expr (COMMA expr)*;

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