def mainencrypt():
	fin = open("./data.fcnf", "rt")
	data = fin.read()
	data = data.replace('a', '634 ')
	data = data.replace('A', '_634 ')
	data = data.replace('b', '822 ')
	data = data.replace('B', '_822 ')
	data = data.replace('c', '348 ')
	data = data.replace('C', '_348 ')
	data = data.replace('d', '523 ')
	data = data.replace('D', '_523 ')
	data = data.replace('e', '743 ')
	data = data.replace('E', '_743 ')
	data = data.replace('f', '247 ')
	data = data.replace('F', '_247 ')
	data = data.replace('g', '389 ')
	data = data.replace('G', '_389 ')
	data = data.replace('h', '745 ')
	data = data.replace('H', '_745 ')
	data = data.replace('i', '725 ')
	data = data.replace('I', '_725 ')
	data = data.replace('j', '981 ')
	data = data.replace('J', '_981 ')
	data = data.replace('k', '135 ')
	data = data.replace('K', '_135 ')
	data = data.replace('l', '936 ')
	data = data.replace('L', '_936 ')
	data = data.replace('m', '832 ')
	data = data.replace('M', '_832 ')
	data = data.replace('n', '2456 ')
	data = data.replace('N', '_2456 ')
	data = data.replace('o', '7268 ')
	data = data.replace('O', '_7268 ')
	data = data.replace('p', '2496 ')
	data = data.replace('P', '_2496 ')
	data = data.replace('q', '1368 ')
	data = data.replace('Q', '_1368 ')
	data = data.replace('r', '365 ')
	data = data.replace('R', '_365 ')
	data = data.replace('s', '5656 ')
	data = data.replace('S', '_5656 ')
	data = data.replace('t', '2364 ')
	data = data.replace('T', '_2364 ')
	data = data.replace('u', '5032 ')
	data = data.replace('U', '_5032 ')
	data = data.replace('v', '5485 ')
	data = data.replace('V', '_5485 ')
	data = data.replace('w', '7415 ')
	data = data.replace('W', '_7415 ')
	data = data.replace('x', '3642 ')
	data = data.replace('X', '_3642 ')
	data = data.replace('y', '4756 ')
	data = data.replace('Y', '_4756 ')
	data = data.replace('z', '3645 ')
	data = data.replace('Z', '_3645 ')
	data = data.replace('å', '9576 ')
	data = data.replace('Å', '_9576 ')
	data = data.replace('ä', '5234 ')
	data = data.replace('Ä', '_5234 ')
	data = data.replace('ö', '8576 ')
	data = data.replace('Ö', '_8576 ')
	fin.close()

	fin = open("./data.fcnf", "wt")
	fin.write(data)
	fin.close()