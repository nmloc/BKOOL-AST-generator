grammar BKOOL;

@lexer::header {
from lexererr import *
}


program  : classdecl+ EOF ;

classdecl: 'class' ID LP memdecl* RP ;

memdecl: ID COLON bkooltype SEMI;

bkooltype: INTTYPE | VOIDTYPE ;

INTTYPE: 'integer' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

LP: '{';

RP: '}';

SEMI: ';' ;

COLON: ':';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};