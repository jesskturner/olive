grammar Olive;

/*
 * Parser Rules
 */

tasklist			: task+ EOF ;

task				: description (NEWLINE | EOF) ;

description			: (link | priority | size | tag | WORD | WHITESPACE)+ ;

link                : '[' TEXT ']' '(' TEXT ')' ;

priority			: WHITESPACE '!'+;

size				: WHITESPACE '>' WORD;

tag                 : WHITESPACE '#' WORD;


/*
 * Lexer Rules
 */

fragment DIGITS     : [0-9] ;
fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;
fragment PUNCT      : [-_"',;:.?()] ;

TEXT				: {self._input.LA(-1) == ord('[') or self._input.LA(-1) == ord('(')}? ~[\])]+ ;

WORD				: (LOWERCASE | UPPERCASE | PUNCT | DIGITS)+ ;

WHITESPACE			: (' ' | '\t')+ ;

NEWLINE				: ('\r'? '\n' | '\r')+ ;
