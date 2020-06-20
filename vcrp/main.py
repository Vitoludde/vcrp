from src import mywrite, myread, myencrypt, mydecrypt
import os

while True:
	os.system("clear")

	prompt = input("1 - write, 2 - read, 3 - encrypt, 4 - decrypt, 5 - quit: ")
	if prompt == "1":
		mywrite.mainwrite()
	elif prompt == "2":
		myread.mainread()
	elif prompt == "3":
		myencrypt.mainencrypt()
	elif prompt == "4":
		mydecrypt.maindecrypt()
	elif prompt == "5":
		quit()
