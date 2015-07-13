__author__ = 'adrianmo'


import string
import re
import codecs,sys, unicodedata
import pprint
import MySQLdb
import os

xuser = "root"
xpasswd = "cRe33Eth"
xhost = '127.0.0.1'
xport = 3334


class MMICProgram():



    def openFile(self, fileName):


        with codecs.open (fileName, "r", "utf-8") as line:
            f = line.read()
            self.code = f.splitlines()
            print self.code



    def getField(self, table, field, syid=1):
        mega = MySQLdb.connect(host=xhost,port=xport,user=xuser, passwd=xpasswd,db='charls')
        mega.autocommit(False)
        c = mega.cursor()

        c.execute("SET CHARACTER SET utf8")
        c.execute("SET collation_connection = 'utf8_general_ci'")
        c.execute("""SELECT %s FROM %s WHERE syid=%s  order by reid asc """ % (field, table, syid))

        mega.close()

        rst = c.fetchall()

        stringify = ""

        for i in range(0,len(rst)):
            stringify += rst[i][0] + "\n\r"

        return stringify







    def getCode(self):
        file = ""
        for i in self.code:
            if isinstance(i, unicode):
                file +=   "\n"  + i





        return file
