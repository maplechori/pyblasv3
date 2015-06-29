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


class SymbolEnv:


    def __init__(self, parent = None):

        self.parent = parent

        self._envContext = {}

    def lookupSymbol(self, name):
        scope = self

        while(scope):
            if scope.getSymbol(name):
                return self
            else:
                return self.parent

    def defSymbol(self, name, value):
        print "[", name, "] := ", value
        self._envContext[name]  = value

    def setSymbol(self, name, value):
        scope = self.lookupSymbol(name)

        if not scope and self.parent:
            print "Error: Key %s on context already exists" % ( name )
        else:
            print "[", name, "] = ", value
            if (scope):
                scope.defSymbol(name, value)
            else:
                self.defSymbol(name, value)

    def getSymbol(self, name):
        if self._envContext.has_key(name):
            print "[", name, "]"
            return self._envContext[name]
        else:
            print "Error: Undefined variable ", name





    def __repr__(self):
        return u"%s" % ( self._envContext)