
import os, re, codecs


class NubisProgram():
    code = None


    def open(self, fileName):

        with codecs.open (fileName, "r", "utf-8") as line:
            f = line.read()
            self.code = f.splitlines()
            print self.code


    def getCode(self):
        file = ""
        for i in self.code:
            if isinstance(i, unicode):
                file +=   "\n"  + i





        return file




