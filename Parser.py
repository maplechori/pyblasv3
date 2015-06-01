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


