from vcrp import mywrite
from vcrp import myread
from vcrp import myencrypt

while True:
	prompt = input("1 - read, 2 - quit: ")
	if prompt == "1":
		myread.mainread()
	elif prompt == "2":
		quit()