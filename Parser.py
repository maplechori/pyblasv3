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





class Parser(object):
    tokenStream = []
    current_token = None
    prev_token = None

    def __init__(self):
        self.counter = 0

    def getSym(self):
        if self.current_token:
            self.prev_token = self.current_token
        if len(self.tokenStream) > 0:
            self.current_token = self.tokenStream.pop(0)

    def accept(self, sym):

        if (sym == self.current_token[0] or sym == self.current_token[1]):
            self.getSym()
            return True
        return False

    def expect(self, sym):
        if (self.accept(sym)):
            return True
        print "Error: unexpected symbol", sym
        print "Current Token", self.getCurr()
        print "Previous Token: ", self.getPrev()
        print "Next Token: ", self.LookAhead()
        exit(1)
        return False

    def getPrev(self):
        return self.prev_token[0]

    def getCurr(self):
        return self.current_token[0]

    def LookAhead(self):
        return self.tokenStream[0]

    def PushBack(self):
        self.tokenStream.insert(0, self.current_token)
        self.current_token = self.prev_token


