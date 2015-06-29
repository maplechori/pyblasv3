# -*- coding: UTF-8 -*-
"""

The MIT License (MIT)

Copyright (c) 2015 Adrian Montero - CESR USC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
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
LBRACKET = "["
RBRACKET = "]"
ELSE = "ELSE"
ELSEIF = "ELSEIF"

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
    (r'\.RESPONSE', RESERVED),
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
    ( r'\[', LBRACKET),
    ( r'\]', RBRACKET),
    ( r'\(', RESERVED),
    ( r'\)', RESERVED),
    ( r'\.', r'DECIMAL'),
    (r'THEN', RESERVED),
    (r'FOR', RESERVED),
    (r'OR\s', RESERVED),
    (r'NOT\s', RESERVED),
    (r'IF\s', IF),
    (r'ELSEIF\s', ELSEIF),
    (r'ELSE[\s\n]?', ELSE),

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