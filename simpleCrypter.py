#@author: AlphaSierraASH
#@version: 2.0

from easygui import *
import sys

#start of GUI
msg = "Enter the message you to encrypt/decrypt and the key for the same"
title = "Simple cipher by AlphaSierraASH"
fieldNames = ["Message to encrypt/decrypt", "Key for encrypting/decrypting"]
fieldValues = multenterbox(msg, title, fieldNames)
if fieldValues is None:
	sys.exit(0)
# make sure that none of the fields were left blank
while 1:
	errmsg = ""
	for i, name in enumerate(fieldNames):
		if fieldValues[i].strip() == "":
			errmsg += "{} is a required field.\n\n".format(name)
	if errmsg == "":
		break
	fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
	if fieldValues is None:
		break
dataIn = fieldValues

#logic part starts here
alph = ("abcdefghijklmnopqrstuvwxyz")
msg = dataIn[0]
strKey = dataIn[1]
key = int(strKey)
newMsg = ""
for char in msg:
	if char in alph:
		pos = alph.find(char)
		newPos = (pos + key) % 26
		newChar = alph[newPos]
		newMsg += newChar
	else:
		newMsg += char
#display the crypted message
msgbox(msg = newMsg)
