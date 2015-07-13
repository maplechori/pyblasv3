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
from __future__ import unicode_literals
import sys
import re



def lex(chars, token_express, flags = re.UNICODE | re.IGNORECASE |  re.MULTILINE | re.DOTALL, debug = 0):
    position = 0
    lines = 0
    tokens = []
    while position < len(chars):
        match = None
        for token_expr in token_express:
            pattern, tag = token_expr
            regex = re.compile(pattern, flags)

            match = regex.match(chars, position)
            if match:

                lines += 1
                text = match.group(0)
                if debug and tag:
                    print "[" , lines , "] (", text, tag, ")"
                if tag != "LITERAL":
                    text = str.upper(text)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            print chars[position-20:position], "|", chars[position], "|" , chars[position:position+20]
            sys.stderr.write('Unexpected character: Line %s %s %s Position: %d\n' % (lines, chars[position], tag, position ))
            sys.exit(1)
        else:
            position = match.end(0)


    return tokens