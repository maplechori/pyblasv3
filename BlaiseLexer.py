# -*- coding: UTF-8 -*-
__author__ = 'adrianmo'

from Lexer import lex

RESERVED = 'RESERVED'
IF = "IF"
DOT = "DOT"
DK = "DK"
RF = "RF"
EMPTY = "EMPTY"
DONTKNOW = "DONTKNOW"
NODONTKNOW = "NODONTKNOW"
REFUSAL = "REFUSAL"
NORF = "NORF"
NODK = "NODK"
NOREFUSAL = "NOREFUSAL"
NOEMPTY = "NOEMPTY"
AUXFIELDS = "AUXFIELDS"
DATAMODEL = "DATAMODEL"
ENDMODEL = "ENDMODEL"
FIELDS = "FIELDS"
RULES = "RULES"
COLON = "COLON"
SEMICOLON = "SEMICOLON"

field_attributes = [ "DK", "RF", "NODK", "NORF", "EMPTY", "NOEMPTY" ]

tokens_ex = [
    (r'[ \n\r\t]+', None),  # SPACES AND WHITE SPACE
    (r'(?:{.*?})', None),  # COMMENTS
    (r'//.*[\n|\r]', None),  # COMMENTS
    (r'\:=', 'ASSIGN'),
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
    (r'KEEP', 'KEEP'),
    (r'\,', 'COMMA'),
    (r'>', RESERVED),
    (r'=', RESERVED),
    (r'\|', RESERVED),
    (r'<>', RESERVED),
    (r'!=', RESERVED),
    (r'ENDIF', RESERVED),
    (r'AND', RESERVED),
    (r'\.\.', 'DOTDOT'),
    (r'\.', DOT),
    (r'COLON', '\:'),
    (r'AUXFIELDS', AUXFIELDS),
    (r'DATAMODEL', DATAMODEL),
    (r'ENDMODEL', ENDMODEL),
    (r'FIELDS', FIELDS),
    ( r'\[', RESERVED),
    ( r'\]', RESERVED),
    ( r'\(', RESERVED),
    ( r'\)', RESERVED),
    ( r'\.', r'DECIMAL'),
    (r'REAL', RESERVED),
    (r'THEN', RESERVED),
    (r'OR\s', RESERVED),
    (r'NOT\s', RESERVED),
    (r'IF\s', IF),
    (r'ELSE\s', RESERVED),
    (r'WHILE\s', RESERVED),
    (r'DO(?=\s)', RESERVED),
    (r'INTEGER', RESERVED ),
    (r'DATETYPE', RESERVED),
    (r'TIMETYPE', RESERVED),
    (r'LANGUAGES', RESERVED),
    (r'TLANGUAGE', RESERVED),
    (r'BLOCK', RESERVED),
    (r'SETTINGS', RESERVED),
    (r'STRING', RESERVED),
    (r'RULES', RESERVED),
    (r'RESERVECHECK', RESERVED),
    (r'ENDTABLE', RESERVED),
    (r'ENDBLOCK', RESERVED),
    (r'ENDPROCEDURE', RESERVED),
    (r'LIBRARY', RESERVED),
    (r'ENDLIBRARY', RESERVED),
    (r'ENDDO', RESERVED),
    (r'END', RESERVED),
    (r'INCLUDE', RESERVED),
    (r'SHOW', RESERVED),
    (r'NEWPAGE', RESERVED),
    (r'NONRESPONSE', RESERVED),
    (r'FIELDPANE', RESERVED),
    (r'TO(?=\s)', RESERVED),
    (r'OF(?=\s)', RESERVED),
    (r'DOWNTO(?=\s)', RESERVED),
    (r'LAYOUT', RESERVED),
    (r'FROM', RESERVED),
    (r'SIGNAL', RESERVED),
    (r'FOR', RESERVED),
    (r'SET', RESERVED),
    (r'TYPE', RESERVED),
    (r'LOCALS', RESERVED),
    (r'ATTRIBUTES', RESERVED),
    (r'DK\s|DONTKNOW', DK),
    (r'RF\s|REFUSAL', RF),
    (r'NODK|NODONTKNOW', NODK),
    (r'NORF|NOREFUSAL', NORF),
    (r'EMPTY', EMPTY),
    (r'NOEMPTY', NOEMPTY),
    (r'PRIMARY', RESERVED),
    (r'IN(?=\s)', RESERVED),
    (r'ARRAY', RESERVED),

    (r'\*\*', 'MULTMULT'),
    (r'[0-9]+\.[0-9]+', 'FLOAT'),
    (r'[0-9]+', 'COUNT'),
    (r'\"(\\.|[^"])*\"|\'(\\.|[^\'])*\'|(\'\')', 'LITERAL'),
    ( r"[a-zA-Z_][a-zA\.-Zñáéíóúü0-9_]*" , 'ID'),



]


def BlaiseLexer(characters):
    return lex(characters, tokens_ex)