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
__author__ = 'adrianmo'
"""

class DataModel(object):

    def __init__(self,id, literal = None):
        self.type = "DATAMODEL"
        self.name = id
        self.primary = []
        self.attributes = []
        self.fields = []
        self.locals = []
        self.literal = literal
        self.blocks = []
        self.rules = []

    def __repr__(self):
        return u"%s: %s Attributes: [%s] Primary: %s [Blocks: %s] Rules:[%s], Fields[%s], Locals[%s]" % ( self.type, self.name, self.attributes, self.primary, self.blocks, self.rules, self.fields, self.locals)



class Block(object):

    def __init__(self,id, literal = None):
        self.type = "BLOCK"
        self.name = id
        self.primary = []
        self.attributes = []
        self.literal = literal
        self.fields = []
        self.rules = []

    def __repr__(self):
        return u"%s: %s Attributes: [%s] " % ( self.type, self.name, self.attributes)



class ForStatement(object):

    def __init__(self, control, initial, direction, final, statements):
        self.type = "FOR"
        self.control = control
        self.initial = initial
        self.direction = direction
        self.final = final
        self.value = statements


    def __repr__(self):
        return ('FOR: {0} {1} {2} {3} DO {4}').format(self.control, self.initial, self.direction, self.final, self.value)


class Field(object):
        def __init__(self, name):
            self.type = "FIELD"
            self.name  = name
            self.tag = None
            self.languages = []
            self.description = None
            self.typeOf = None
            self.attributes = []
        def __repr__(self):
            return ('FIELD: {0} {1}').format(self.name, self.languages )
