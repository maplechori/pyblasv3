# -*- coding: UTF-8 -*-
__author__ = 'adrianmo'

from Lexer import lex
import re
RESERVED = 'RESERVED'
IF = "IF"
DOT = "DOT"
DK = "DK"
RF = "RF"
EMPTY = "EMPTY"
FIELDS = "FIELDS"
RULES = "RULES"
COLON = "COLON"
SEMICOLON = "SEMICOLON"

tokens_ex = [
    (r'//.*(?=[\n|\r])?', None),  # COMMENTS
    (r'[ \n\r\t]+', None),  # SPACES AND WHITE SPACE
    (r'(?:{.*?})', None),  # COMMENTS
    (r'\:=', 'ASSIGN'),
    (r'\.INSPECT', RESERVED),
    (r'MOVEBACKWARD', RESERVED),
    (r'MOVEFORWARD', RESERVED),
    (r'\.INLINE', RESERVED),
    (r'\.FILL', RESERVED),
    (r';', RESERVED),
    (r'\+', RESERVED),
    (r'-', RESERVED),
    (r'\*\*', RESERVED),
    (r'DIV(?=\s)',RESERVED),
    (r'\*', RESERVED),
    (r'/', RESERVED),
    (r'<=', RESERVED),
    (r'<', RESERVED),
    (r'>=', RESERVED),
    (r':', COLON),
    (r'\.KEEP', 'KEEP'),
    (r'\,', 'COMMA'),
    (r'>', RESERVED),
    (r'=', RESERVED),
    (r'\|', RESERVED),
    (r'<>', RESERVED),
    (r'!=', RESERVED),
    (r'ENDIF', RESERVED),
    (r'AND', RESERVED),
    ( r'\[', RESERVED),
    ( r'\]', RESERVED),
    ( r'\(', RESERVED),
    ( r'\)', RESERVED),
    ( r'\.', r'DECIMAL'),
    (r'THEN', RESERVED),
    (r'FOR', RESERVED),
    (r'OR\s', RESERVED),
    (r'NOT\s', RESERVED),
    (r'IF\s', IF),
    (r'ELSE\s', RESERVED),
    (r'ELSEIF\s', RESERVED),
    (r'DO(?=\s)', RESERVED),
    (r'GROUP\.', RESERVED),
    (r'ENDGROUP', RESERVED),
    (r'SUBGROUP\.', RESERVED),
    (r'ENDSUBGROUP', RESERVED),
    (r'ENDDO', RESERVED),
    (r'EMPTY', EMPTY),
    (r'TO(?=\s)', RESERVED),
    (r'OF(?=\s)', RESERVED),
    (r'EXIT', RESERVED),
    (r'EXITFOR', RESERVED),
    (r'IN(?=\s)', RESERVED),
    (r'\*\*', 'MULTMULT'),
    (r'[0-9]+\.[0-9]+', 'FLOAT'),
    (r'[0-9]+', 'COUNT'),
    (r'\"(\\.|[^"])*\"|\'(\\.|[^\'])*\'|(\'\')', 'LITERAL'),
    (r"[a-zA-Z_][a-zA-Zñáéíóúü0-9_]*" , 'ID'),
]


def NubisLexer(characters):
    return lex(characters, tokens_ex, re.UNICODE | re.IGNORECASE )