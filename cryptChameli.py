#!/usr/bin/python3
from hashlib import md5
from codecs import getencoder,getdecoder
from pyfiglet import figlet_format
from sys import argv
import argparse

class ROT_13:
	def __init__(self,text):
		self.text = text
		self.rot13 = lambda : getencoder("rot-13")(self.text)[0]
		print(self.rot13)

class ROT_47:
	def __init__(self,text):
		self.text = list(text)
		self.flag = 0

		while self.flag < len(self.text):
			if ord(self.text[self.flag]) >= 33 and ord(self.text[self.flag]) <= 126:
				self.text[self.flag] = chr(33 + ((ord(self.text[self.flag]) + 14)) % 94)

			self.flag += 1
		self.encoded_text = ''.join(self.text)
		print(self.encoded_text)

parser = argparse.ArgumentParser(description="A Tool mainly made for cryptoGraphy in CTFs",
	epilog="EXAMPLE : python3 %(prog)s --rot13-decode uryyb"
	)
parser.add_argument(
	"--rot13-decode", help="Decodes ROT 13 encoding",
	dest="rot_13_encode", nargs="+")
parser.add_argument("--from-hex", help="Hex to string conversion",dest="from_hex", nargs="+")

if len(argv) == 1:
	parser.print_help()
	exit(0)

print(figlet_format("crypt chameli",font="cosmic"))
print("\t"*3 + "\033[1;34m\033[1;36m-by twitter:@whoamiPwns\033[1;34m\033[0m, \033[1;33mGithub:@whoami546\033[0m\n")

class Hex:
	def __init__(self,text):
		self.text = text.encode()
		self.toHex = lambda : getencoder("hex")(self.text)[0].decode()
		self.fromHex = lambda : getdecoder("hex")(self.text)[0].decode()

class Decimal:
	def __init__(self,text):
		self.text = list(text)

	def toDecimal(self):
		for i in self.text:
			self.text[self.text.index(i)] = f"{ord(i)}"
		return ' '.join(self.text)

print(Decimal("hello").toDecimal())
class Morse_code:
	def __init__(self,text):
		self.text_morse = text
		self.morses = {""}
