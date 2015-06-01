__author__ = 'adrianmo'

from SymbolEnv import *
from NubisLexer import *
from Parser import *


SymbolTable = []

class Node(object):
    def __init__(self, value):
         self.value = value
         self.type = None
         self.attributes = []
    def __repr__(self):
        return ('{0}: {1} ').format( self.__class__.__name__ , self.value)


class Identifier(Node):
    pass


class MethodCall(Node):
    pass



class AskQuestion(Node):
    pass


class TreeNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return ('{0}: {1} {2} {3} ').format( self.__class__.__name__ , self.left,self.op, self.right)


class NumberOpNode(Node):

    def __init__(self, value, typeOf):
        self.typeOf = typeOf
        self.value = value
    def __repr__(self):
        return ('N:{0}').format(self.value)


class DateType(Node):
    pass

class ArrayType(Node):
    def __init__(self, typeOf, lower, higher):
        self.lower = lower
        self.higher = higher
        self.typeOf = typeOf

    def __repr__(self):
        return ('Array[{0}..{1}] of {2} ').format( self.lower,self.higher, self.typeOf)

class RangeType(Node):
    def __init__(self,  lower, higher):
        self.lower = lower
        self.higher = higher


    def __repr__(self):
        return ('Range[{0}..{1}]').format( self.lower,self.higher)



class ExpressionNode(Node):
    def __init__(self, value):
        self.value = value

class NotExpression(Node):
    pass

class BinOp(TreeNode):

    def __init__(self, op, left, right):
        self.left = left
        self.right =right
        self.op = op

    def __str__(self, level=0):

        retr = ""
        retl = ""

        if (isinstance(self.left, TreeNode)):
            retl +=  self.left.__str__(level+1) + ""
        else:
            retl +=  self.left.value + ""

        if (isinstance(self.right, TreeNode)):
            retr += self.right.__str__(level+1) + ""
        else:
            retr += self.right.value + ""

        return  "(" + self.op +  " " + retl + " " + retr + ")"


    def __repr__(self):
        return ('BinOp: {0} {1} {2} ').format( self.left,self.op, self.right)

class AssignmentNode(BinOp):
    def __repr__(self):
        return ('Assignment: {0} {1} {2} ').format( self.left,self.op, self.right)


class ArrayAccess(BinOp):
    pass

class IfCondition(BinOp):

    def __init__(self, op, left, value, right):
        self.value = value
        self.left = left
        self.right =right
        self.op = op

    def __str__(self, level=0):
        return ('Condition: {0} {1} {2} ').format( self.left,self.op, self.value)


    def __repr__(self):
        return ('Condition: {0} {1} {2} ').format( self.left,self.op, self.value)




class NubisParser(Parser):
    _dm = None

    def __init__(self, tokenStream):
        self.tokenStream = tokenStream

    def program(self):
        self.getSym()
        se = SymbolEnv()
        se.addSymbol(self.getCurr(), "PROGRAM")
        SymbolTable.insert(0,se)
        return self.statement()


    def factor(self):
        value = 0
        if self.accept("ID"):

            value = Identifier(self.getPrev())
        elif self.accept("COUNT"):
            value = NumberOpNode(self.getPrev(), int)
        elif self.accept("LPAREN"):
            value = ExpressionNode(self.expression())
            self.expect("RPAREN")
        else:
            print "factor: syntax error", self.getPrev(), self.getCurr()
            self.getSym()

        return value

    def term(self):
        left = self.factor()
        #print "term: ", left

        while self.getCurr() == "*" or self.getCurr() == "/" or self.getCurr() == "MOD":
            op = self.getCurr()
            self.getSym()
            rval = self.factor()
            left = BinOp(op, left, rval)
            #print left

        return left

    def unary(self):

        if self.accept("-") or self.accept("+"):
            symbolChange = self.getPrev()

            trm = self.term()
            if symbolChange == "-":
                trm.value =  symbolChange + trm.value
            return trm
        else:
            return self.term()



    def expression(self):
        left = self.unary()

        while self.getCurr() == "+" or self.getCurr() == "-" or  self.getCurr() == "=" or self.getCurr() == '<>'  or self.getCurr() == "!=" or self.getCurr() ==  "<" or self.getCurr() == "<=" or self.getCurr() == ">" or self.getCurr() == ">=":
            op = self.getCurr()
            self.getSym()
            left = BinOp(op, left, self.unary())
            print left

        #self.PushBack()
        return left

    def and_or_expression(self):
        left = self.expression()
        #self.getSym()
        while self.getCurr() == "AND" or self.getCurr() == "OR" or self.getCurr() == "IN" :
            op = self.getCurr()
            self.getSym()

            if self.getCurr() == "AND" or self.getCurr() == "OR" or self.getCurr() == "IN":
                right = self.and_or_expression()
            else:
                right = self.expression()
            left = BinOp(op, left, right)

        return left



    def condition(self):
        right = None
        if self.accept("NOT"):

            if self.accept("("):
                left = NotExpression(self.and_or_expression())
                self.accept(")")
            else:
                left = NotExpression(self.and_or_expression())

        else:
            left = ExpressionNode(self.and_or_expression())


        if self.accept("THEN"):
            value = self.statement()

            if self.accept("ELSEIF"):
                right = self.condition()
            elif self.accept("ELSE"):

                if self.accept("ENDIF"):
                    right = None
                else:
                    right = self.statement()

            else:
                pass


            self.accept("ENDIF")

            print  IfCondition("IF", left, value, right)
            return IfCondition("IF", left, value, right)

        else:
            print "condition: invalid operator", self.current_token[0], self.current_token[1], self.getPrev(), self.getCurr()
            self.getSym()

    def statement(self):

        print "statement(", self.current_token[0] , self.getCurr() , ")"

        if self.accept("ID"):
            identifier = Identifier(self.getPrev())
            print identifier
            if (self.accept(".")): # method

                if (self.accept("KEEP")):

                    return BinOp("MethodCall", identifier, MethodCall("KEEP"))

            elif(self.accept("[")):
                    sexp = self.expression()
                    arr = ArrayAccess("ArrayAccesss", identifier, sexp)
                    self.expect("]")
                    return arr
            elif self.accept(":="):
                return AssignmentNode(":=", identifier, self.expression())
            else:
                return AskQuestion(identifier)

        elif self.accept("IF"):
            return self.condition()


        elif self.accept("FOR"):#self.current_token[1] == "FOR":
            self.accept("ID")
            _control = Identifier(self.getPrev())
            self.accept("ASSIGN")
            self.accept("COUNT")
            _initial = self.getPrev()

            if self.accept("TO"):
                _direction = self.getPrev()
            elif self.accept("DOWNTO"):
                _direction = self.getPrev()
            else:
                print "Unexpected token in FOR STATEMENT"

            if self.accept("COUNT"):
                _final = self.getPrev()
            elif self.accept("("):
                return self.expression()
                self.accept(")")


            self.accept("DO")
            stmt = self.statement()
            self.accept("ENDDO")



            forstmt =  ForStatement(_control, _initial, _direction, _final, stmt)
            return forstmt


    def enumerated_type(self):
        tt = []
        v = 1
        while not self.getPrev() == "ENDBLOCK":

            if self.accept("ID"):
                print self.getPrev()
                userType = Identifier(self.getPrev())


                if (self.accept("(")):
                    self.expect("COUNT")
                    print self.getPrev()
                    # put this value instead of v
                    self.accept(")")

                    if self.accept("LITERAL"):
                        print self.getPrev()
                elif self.accept("LITERAL"):
                    print self.getPrev()

            tt.append(userType)
            if self.accept("COMMA"):
                    v += 1

            else:
                    print self.getCurr()
                    break

        return tt



    def array_type(self):
        print "ARRAY TYPE"
        self.expect("[")
        self.expect("COUNT")
        lower = self.getPrev()
        self.expect("DOTDOT")
        self.expect("COUNT")
        higher = self.getPrev()
        self.expect("]")
        self.expect("OF")
        aType = ArrayType(self.type_denoter(), lower, higher)
        return aType



    def type_denoter(self):
        print "TYPE DENOTER"

        if (self.accept("ID")):
            print self.getPrev()
            return Identifier(self.getPrev())

        elif (self.accept("INTEGER")):

            if (self.accept("[")):
                self.expect("COUNT")
                #print "INTEGER[" + self.getPrev() + "]"
                count = self.getPrev()
                self.accept("]")
                return ArrayType(int, 0, count)

            else:
                return int

        elif (self.accept("COUNT")):

            low =  self.getPrev()

            if (self.accept("DOTDOT")):
                self.accept("COUNT")
                high = self.getPrev()

                return RangeType(low, high)
            else:
                print "Error: no higher range"
                self.getSym()


        elif (self.accept("DATETYPE")):
            dt = DateType(self.getPrev())
            print dt
            return dt

        elif (self.accept("STRING")):
            print "STRING"

            if (self.accept("[")):
                self.expect("COUNT")
                cntType = self.getPrev()
                print "STRING[" + self.getPrev() + "]"
                self.accept("]")
                return ArrayType(str, 0, cntType)
            else:
                print "STRING"

        elif (self.accept("ARRAY")):
            return self.array_type()


        elif (self.accept("(")):
            print "ENUMERATED TYPE"
            enum = self.enumerated_type()
            self.accept(")")
            return enum
















