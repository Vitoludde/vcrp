import os

def mainwrite():
	os.system("clear")
	print("Write _quit_ to return")

	configfile = open("./data.vcrp","w")

	def writeline(textt):
		configfile.write(textt + "\n")
	while True:
		text = input("")
		if text == "_quit_":
			configfile.close()
			break
		writeline(text)
