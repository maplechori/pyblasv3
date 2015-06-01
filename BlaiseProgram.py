
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




