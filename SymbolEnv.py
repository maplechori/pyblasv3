


class SymbolEnv:

    def __init__(self):
        self._envContext = {}

    def addSymbol(self, name, value, size = 1, offset = 0):
        if self._envContext.has_key(name):
            print "Error: Key %s on context already exists" % ( name )
        else:
            self._envContext[name] = value

    def getSymbol(self, name, offset):
        return self._envContext['name']

    def __repr__(self):
        return u"%s" % ( self._envContext)