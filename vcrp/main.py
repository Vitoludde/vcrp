from src import mywrite
from src import myread
from src import myencrypt
from src import mydecrypt

while True:
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
