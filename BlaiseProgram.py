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
import os, re, codecs


class BlaiseProgram():
    code = None


    def open(self, fileName):

        with codecs.open (fileName, "r", "utf-8") as line:
            f = line.read()
            self.code = f.splitlines()

            for i in range(0, len(self.code)):
                self.code[i] = self.processIncludes(self.code[i])




    def openInner(self, fileName):
        with codecs.open(fileName, "r", "utf-8") as imf:
            combined = []
            g = imf.read()
            plines = g.splitlines()
            for i in range(0, len(plines)):
                plines[i] = self.processIncludes(plines[i])

            return plines

    def processIncludes(self, fileContents):

        include_list = re.findall("INCLUDE \"([A-Za-z0-9\.]+)\"",fileContents)
        if include_list:
                import_file = include_list[0]
                contents = self.openInner(import_file)
                return contents
        else:
            return fileContents

    def getCode(self):
        file = ""

        for i in self.code:
            if isinstance(i, unicode):
                file += " \r " + i
            elif isinstance(i, list):
                for j in i:

                    file += " \r " + j

        shirtPlate = file.splitlines()
        #for i in range(0, len(shirtPlate)):
        #    print i, shirtPlate[i]
        return file




