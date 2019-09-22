def mainread():
	f = open("./data.fcnf", "r")

	contents = f.read()
	print(contents)

	f.close()