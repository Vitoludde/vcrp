import os

def mainwrite():
	os.system("clear")
	print("Write -quit to return")

	configfile = open("./data.vcrp","w")

	def writeline(textt):
		configfile.write(textt + "\n")
	while True:
		text = input("")
		if text == "-quit":
			configfile.close()
			break
		writeline(text)
