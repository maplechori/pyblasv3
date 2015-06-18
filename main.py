#!/usr/bin/env python
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

import pprint



from BlaiseParser import *
from BlaiseProgram import *
from NubisParser import *
from NubisProgram import *



#bp = BlaiseProgram()
#bp.open("IndFfw.bla")

#tokens = BlaiseLexer(bp.getCode())
#pprint.pprint(tokens)
#p = BlaiseParser(tokens)


#print p
#pprint.pprint( getattr(p, "tokenStream"))
#prg = p.program()

#if prg.rules:
#    print prg.rules[0]


bpx = NubisProgram()
bpx.open("nubis.bla")

#print type(bpx.getCode())

tokensNubis = NubisLexer( bpx.getCode())
tokensNubis.append((u"END", "RESERVED"))
pprint.pprint(tokensNubis)
x = NubisParser(tokensNubis)

actual = x.program()

print "******************"


def interpret(stmt, level):

    if stmt == None:
        return

    if isinstance(stmt, list):
        #print "R1"
        for i in stmt:

            if i.type == "BINOP":
                print level*"\t",i
            elif i.type == "AskQuestion":
                print level*"\t",i
            elif i.type == "FOR":
                 print level*"\t","FOR", i.control , " := ", i.initial, i.direction, i.final, " DO"
                 interpret(i.value, level + 1)
            elif i.type == "ELSE":
                print "ELSE"
                print level*"\t", i.type

                interpret(i.value, level + 1)
            elif i.type == "IF":
                print (level)*"\t", "IF", i.left, "THEN"


                interpret(i.value, level + 1)
                if i.right:
                    print level*"\t", "ELSE"
                    interpret(i.right, level + 1)
                    #print level*"\t"
                    #print "ELSE\n\r",(level)*"\t"
                    #print i.right, "\n"
            elif stmt.type == "EXPRESSION":
                print "exp"
                interpret(stmt.value, level + 1)
    else:
        #print "R2", stmt

        if stmt.type == "BINOP":
                print stmt
        elif stmt.type == "AskQuestion":
                print level*"\t", stmt
        elif stmt.type == "FOR":
                print level*"\t","FOR", stmt.initial, stmt.direction, stmt.final

                interpret(stmt.value, level + 1)
        elif stmt.type == "ELSE":
                print "ELSE"
                print level*"\t", stmt.type

        elif stmt.type == "IF":
                print level*"\t","IF", stmt.left, "THEN"
                interpret(stmt.value, level + 1)

                if stmt.right:
                    print level*"\t", "ELSE"
                    interpret(stmt.right, level + 1)
                    #print (level)*"\t\n"
                    #print "ELSE\n\r"
                    #print (level)*"\t", stmt.right, "\n"
        elif stmt.type == "EXPRESSION":
                print "exp"
                interpret(stmt.value, level + 1)

interpret(actual,0)