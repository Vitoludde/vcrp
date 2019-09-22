from src import mywrite
from src import myread
from src import myencrypt

while True:
	prompt = input("1 - read, 2 - quit: ")
	if prompt == "1":
		myread.mainread()
	elif prompt == "2":
		quit()
