import os

def mainread():
	os.system("clear")

	f = open("./data.vcrp", "r")

	print(f.read())

	f.close()
