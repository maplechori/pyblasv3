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

from SymbolEnv import *
from NubisLexer import *
from BlaiseObjects import *
from Parser import *


SymbolTable = []



class AskQuestion(Node):

     def __init__(self, value):
         self.value = value
         self.type = "AskQuestion"

     def __repr__(self):
         return ('ASK {0}').format( self.value)




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




class ArrayAccess(BinOp):
    pass


class BeginCombine(Node):

    def __init__(self, name, params):
        self.name = name
        self.type = "BEGINCOMBINE"
        self.value = params

    def __repr__(self):
        return ('BeginCombine {0} Params: {1}').format(self.name, self.value)



class JumpBack(Node):

    def __init__(self, tag):
        self.name = tag
        self.type = "JUMPBACK"
        self.value = tag

    def __repr__(self):
        return ('Jumpback {0} Params: {1}').format(self.name, self.value)









class MMICParser(Parser):
    _dm = None

    def __init__(self, tokenStream):
        self.tokenStream = tokenStream

    def program(self):
        self.getSym()
        se = SymbolEnv()
        #se.setSymbol(self.getCurr(), "PROGRAM")
        #SymbolTable.insert(0,se)
        return self.statement_list()



    def factor(self):
        value = 0

        if self.accept("NOT") or self.accept("!"):
            value = NotExpression(self.factor())

        elif self.accept("ID"):
            value = Identifier(self.getPrev())

            if(self.accept("[")):

                sexp = self.expression()
                arr = ArrayAccess("ArrayAccess",  value, sexp)
                self.expect("]")
                return arr

            if self.accept("("):
                print "FUNCTION CALL"
                if self.accept(")"):
                    value = Call(value, None)
                else:
                    value = Call(value, self.params_list())
                    self.expect(")")
                print value

                return value




        elif self.accept("COUNT"):

            value = NumberOpNode(int(self.getPrev()), "INTEGER")
        elif self.accept("EMPTY"):
            value = Identifier("EMPTY")

        elif self.accept("("):
            value = ExpressionNode(self.and_or_expression())
            self.expect(")")
        elif self.accept("LITERAL"):
            value = Literal(self.getPrev())
        else:
            print "factor: syntax error", self.getPrev(), self.getCurr()
            self.getSym()

        return value

    def params_list(self):
        paramsList = []
        paramsList.append(self.expression())

        while(self.accept("COMMA"))  :
            paramsList.append(self.expression())


        return paramsList






    def term(self):
        left = self.factor()
        print "term: ", left

        while self.getCurr() == "*" or self.getCurr() == "/" or self.getCurr() == "MOD":
            op = self.getCurr()
            self.getSym()
            rval = self.factor()
            left = BinOp(op, left, rval)
            #print left
        print "returning-->", left
        return left

    def unary(self):

        if self.accept("-") or self.accept("+"):
            symbolChange = self.getPrev()

            trm = self.term()
            if symbolChange == "-":
                trm.value =  symbolChange + trm.value
                print "SYMBOL CHANGE **"
            return trm
        else:
            return self.term()



    def expression(self):
        left = self.unary()

        while self.getCurr() == "DECIMAL" or self.getCurr() == "." or self.getCurr() == "+" or self.getCurr() == "-" or  self.getCurr() == "=" or self.getCurr() == '<>'  or self.getCurr() == "!=" or self.getCurr() ==  "<" or self.getCurr() == "<=" or self.getCurr() == ">" or self.getCurr() == ">=":
            op = self.getCurr()
            self.getSym()
            left = BinOp(op, left, self.unary())
            print left

        #self.PushBack()
        return left

    def and_or_expression(self):
        left = self.expression()

        #self.getSym()
        while str.strip(self.getCurr()) == "AND" or str.strip(self.getCurr()) == "and" or str.strip(self.getCurr()) == "OR" or str.strip(self.getCurr()) == "IN" or str.strip(self.getCurr()) == "in":

            if  self.getCurr() == "IN":
                   print "IN >>>"


            op = self.getCurr()

            self.getSym()

            if self.getCurr() == "AND" or self.getCurr() == "OR" or self.getCurr() == "IN" or str.strip(self.getCurr()) == "and" or str.strip(self.getCurr()) == "in":


                right = self.and_or_expression()
                #right = self.condition()

            else:
                right = self.expression()
            left = BinOp(op, left, right)

        return left



    def condition(self):
        right = None
        #if self.accept("NOT") or self.accept("!"):
        #    if self.accept("("):
        #        left = NotExpression(self.condition())
        #        self.accept(")")
        #    else:
        #        left = NotExpression(self.condition())



        #else:
        left = ExpressionNode(self.and_or_expression())

        if self.accept("THEN"):

            statements = []
            while self.getCurr() != "ENDIF":
                stmt = self.statement()

                if (stmt):
                    statements.append(stmt)

                if self.accept("ELSEIF"):
                    print "ELSEIF"
                    right = self.condition()
                    print "LEFT ", right

                elif self.accept("ELSE"):

                    if self.accept("ENDIF"):
                        right = None
                    else:
                        right = self.statement()
                else:
                    pass





            print  IfCondition("IF", left, statements, right)
            return IfCondition("IF", left, statements, right)

        else:

            print "condition: invalid operator", self.current_token[0], self.current_token[1], self.getPrev(), self.getCurr()
            self.getSym()

    def statement_list(self):
        stmtList = []
        stmtList.append(self.statement())
        while(self.current_token[0] != "END" and self.current_token[0] != "ENDDO" and self.current_token[0] != "ENDCOMBINE")  :
            stmtList.append(self.statement())
        return stmtList


    def statement(self):

        print "statement(", self.current_token[0] , self.getCurr() , ")"

        if self.accept("ID"):

            identifier = Identifier(self.getPrev())
            print identifier

            if (self.accept(".FILL")):
                print BinOp("CALL", identifier, MethodCall("FILL"))
                return BinOp("CALL", identifier, MethodCall("FILL"))
            elif (self.accept(".KEEP")):
                print BinOp("CALL", identifier, MethodCall("KEEP"))
                return BinOp("CALL", identifier, MethodCall("KEEP"))
            elif(self.accept("[")):
                    sexp = self.expression()
                    print "array access", sexp
                    arr = ArrayAccess("ArrayAccess", identifier, sexp)
                    self.expect("]")


                    if (self.accept(".KEEP")):
                        arr = BinOp("CALL", arr, MethodCall("KEEP"))

                    if self.accept(":="):
                        assign = AssignmentNode(":=", arr, self.expression())
                        return assign
                    else:
                        return arr
            elif self.accept(":="):

                print identifier
                exp = self.expression()
                print exp

                assign = AssignmentNode(":=", identifier,exp  )
                print "ASSIGN: ", assign
                return assign
            elif self.accept("("):

                import sys
                sys.exit(1)
                #while not self.accept(")"):
                #    self.getSym()
            else:
                return identifier

        elif self.accept("IF") or self.accept("if"):
            print "IF"
            condition =  self.condition()
            print condition
            self.expect("ENDIF")
            return condition


        elif self.accept("JUMPBACK"):
            print "JUMPBACK"
            self.accept("(")
            self.accept("ID")
            value = Identifier(self.getPrev())
            self.accept(")")

            return JumpBack(value)



        elif self.accept("BEGINCOMBINE"):
            print "BEGINCOMBINE"
            self.accept("(")
            self.accept("ID")
            value = Identifier(self.getPrev())
            self.expect(")")
            stmts =  self.statement_list()
            self.accept("ENDCOMBINE")

            bc = BeginCombine(value, stmts)
            return bc


        elif self.accept("COMBINE"):
            print "COMBINE"
            self.accept("(")
            params = self.params_list()
            value = params[len(params)-1]
            self.expect(")")
            print value
            stmts = []
            for i in range(0,len(params) - 2):
                stmts.append(self.statement())

            bc =  BeginCombine(value, stmts)
            return bc







        elif self.accept("FOR"):#self.current_token[1] == "FOR":
            self.accept("ID")
            _control = Identifier(self.getPrev())
            self.accept("ASSIGN")
            self.accept("COUNT")
            _initial = NumberOpNode(self.getPrev(), "INTEGER")

            if self.accept("TO"):
                _direction = self.getPrev()
            elif self.accept("DOWNTO"):
                _direction = self.getPrev()
            else:
                print "Unexpected token in FOR STATEMENT"

            if self.accept("COUNT"):
                _final = NumberOpNode(self.getPrev(), "INTEGER")
            elif self.accept("("):
                _final = self.expression()
                self.accept(")")
            elif self.accept("ID"):
                _final = Identifier(self.getPrev())


            self.accept("DO")
            print "DO"
            stmt = self.statement_list()
            print "ENDDO"
            self.accept("ENDDO")


            forstmt =  ForStatement(_control, _initial, _direction, _final, stmt)
            print forstmt
            return forstmt

        elif self.accept("EXITFOR"):
            return Identifier("EXITFOR")


    def enumerated_type(self):
        tt = []
        v = 1
        while not self.getPrev() == "ENDBLOCK":

            if self.accept("ID"):
                print self.getPrev()
                userType = Identifier(self.getPrev())


                if (self.accept("(")):
                    self.expect("COUNT")
                    print NumberOpNode(self.getPrev(), "INTEGER")
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
        lower = NumberOpNode(self.getPrev(), "INTEGER")

        self.expect("DOTDOT")
        self.expect("COUNT")
        higher = NumberOpNode(self.getPrev(), "INTEGER")
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
                count = NumberOpNode(self.getPrev(), "INTEGER")
                self.accept("]")
                return ArrayType(int, 0, count)

            else:
                return int

        elif (self.accept("COUNT")):

            low =  NumberOpNode(self.getPrev(), "INTEGER")


            if (self.accept("DOTDOT")):
                self.accept("COUNT")
                high = NumberOpNode(self.getPrev(), "INTEGER")

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
                cntType = NumberOpNode(self.getPrev(), "INTEGER")
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
















