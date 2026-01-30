# -- encoding:utf-8 --
import os

os.system("chcp 866 >nul")
os.system("cls")
print("input a string:")
strLine1 = input()
nLen = len(strLine1)
strLine2 = strLine1[nLen - 1] + strLine1[1:nLen - 1] + strLine1[0]
print("Exchange the first and the last symbol in the string")
print("Source string: " + strLine1)
print("Destination string: " + strLine2)