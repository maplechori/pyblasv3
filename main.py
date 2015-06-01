#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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

print type(bpx.getCode())

tokensNubis = NubisLexer( bpx.getCode())

pprint.pprint(tokensNubis)
x = NubisParser(tokensNubis)

x.program()