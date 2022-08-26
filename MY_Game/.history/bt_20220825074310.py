class InputOutString(object):
   def __init__(self):
       self.s = ""

   def getString(self):
       self.s = input("Nhập chuỗi:")
# Code by Quantrimang.com
   def printString(self):
       print (self.s)

strObj = InputOutString()
strObj.getString()
strObj.printString()