#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import sys
import re



def lex(chars, token_express, flags = re.UNICODE | re.IGNORECASE |  re.MULTILINE | re.DOTALL):
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
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            print chars[position-20:position], "|", chars[position], "|" , chars[position:position+20]
            sys.stderr.write('Unexpected character: %s %s Position: %d\n' % (chars[position], tag, position ))
            sys.exit(1)
        else:
            position = match.end(0)
    return tokens