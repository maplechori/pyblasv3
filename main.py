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
            interpret(i, level)

    else:
        #print "R2", stmt

        if stmt.type == "BINOP":
                print level*"\t",stmt
        elif stmt.type == "AskQuestion":
                print level*"\t", stmt
        elif stmt.type == "FOR":
                print level*"\t","FOR", stmt.control , " := ", stmt.initial, stmt.direction, stmt.final, " DO"
                #print level*"\t","FOR", stmt.initial, stmt.direction, stmt.final

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
        elif stmt.type == "ASSIGN":
                print stmt.left
                print stmt.left, ":=", stmt.right

        else:

            return

interpret(actual,0)

print "*********** EVALUATE ***********"


def apply_op(op, left, right):
    if (op == "+"):
        return left + right
    elif (op == "-"):
        #print left, "-", right
        return left - right
    elif (op == "*"):
        #print left, "*", right
        return left * right
    elif (op == "/"):
        #print left, "/", right
        return left / right
    elif (op == "CALL"):
        print "executing CALL ",right, " ON ", left
        return
    else:
        pass



def evaluate(stmt, env):

    if stmt == None:
        return

    if isinstance(stmt, list):
        #print "R1"
        for i in stmt:
            evaluate(i, env)
    else:
        #print "R2", stmt

        if stmt.type == "BINOP":
                #print "BINOP"
                print stmt
                return apply_op(stmt.op, evaluate(stmt.left, env), evaluate(stmt.right, env))
                #print stmt

        elif stmt.type == "INTEGER":
            print stmt.value
            return stmt.value

        elif stmt.type == "METHODCALL":
            return stmt.value


        elif stmt.type == "IDENTIFIER":
                return env.getSymbol(stmt.value)

        elif stmt.type == "FOR":
                #print level*"\t","FOR", stmt.initial, stmt.direction, stmt.final


                #interpret(stmt.value, level + 1)
                pass
        elif stmt.type == "ELSE":
                print "ELSE"
                #print level*"\t", stmt.type
                pass

        elif stmt.type == "IF":
                #print level*"\t","IF", stmt.left, "THEN"
                print "evaluate: " , evaluate(stmt.left, env)
                #interpret(stmt.value, level + 1)
                pass

                #if stmt.right:
                #    print level*"\t", "ELSE"
                #    interpret(stmt.right, level + 1)
                    #print (level)*"\t\n"
                    #print "ELSE\n\r"
                    #print (level)*"\t", stmt.right, "\n"
        elif stmt.type == "EXPRESSION":
                return evaluate(stmt.value, env)

        elif stmt.type == "ASSIGN":
            return env.defSymbol(stmt.left.value, evaluate(stmt.right, env))




envGlobal = SymbolEnv()

evaluate(actual, envGlobal)

print envGlobal