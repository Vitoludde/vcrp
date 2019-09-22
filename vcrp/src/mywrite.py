def mainwrite():
	try:
		configfile = open("./data.fcnf","w")
	except Exception as e:
		configfile = open("./data.fcnf","w")

	def writeline(one, two):
		configfile.write(one + ": " + two + "\n")
	while True:
		one = input("First: ")
		if one == "quit":
			configfile.close()
			break
		two = input("Second: ")
		writeline(one, two)
		print("Writing to config")
