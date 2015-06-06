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

print type(bpx.getCode())

tokensNubis = NubisLexer( bpx.getCode())
tokensNubis.append((u"END", "RESERVED"))
pprint.pprint(tokensNubis)
x = NubisParser(tokensNubis)

actual = x.program()