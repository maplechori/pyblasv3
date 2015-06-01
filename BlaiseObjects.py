__author__ = 'adrianmo'

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
        global levelScope
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
