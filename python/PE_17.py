#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?

_digits = [(1, 'one', ''), (2, 'two', ''), (3, 'three', ''), (4, 'four', ''), (5, 'five', ''),
		 (6, 'six', ''), (7, 'seven', ''), (8, 'eight', ''), (9, 'nine', '')]
		 
_sub20 = [(11, 'eleven', ''), (12, 'twelve', ''), (13, 'thirteen', ''), (14, 'fourteen', ''),
		 (15, 'fifteen', ''), (16, 'sixteen', ''), (17, 'seventeen', ''), (18, 'eighteen', ''), (19, 'nineteen', '')]
		 
_tens = [(1, 'ten', ''), (2, 'twenty', ''), (3, 'thirty', ''), (4, 'forty', ''), (5, 'fifty', ''), (6, 'sixty', ''), 
		 (7, 'seventy', ''), (8, 'eighty', ''), (9, 'ninety', '')]
		 
_hundthou = [ (100, 'hundred', 'hundredand'), (1000, 'thousand')]

def get_digit(num, switch):
	if switch == 0:
		for i in xrange(0, 9):
			if num == _digits[i][0]:
				return _digits[i][1]
	elif switch == 1:
		for i in xrange(0, 9):
			if num == _sub20[i][0]:
				return _sub20[i][1]
	elif switch == 2:
		for i in xrange(0, 9):
			if num == _tens[i][0]:
				return _tens[i][1]
	elif switch == 3:
		if len(str(num)) == 3:
			return _hundthou[0][1]
		else:
			return _hundthou[1][1]
	elif switch == 4:
		if len(str(num)) == 3:
			return _hundthou[0][2]
		else:
			return _hundthou[1][1]			

def partition(inp):
	part_list = ''
	if  len(inp) == 1:  	
		part_list = get_digit(int(inp[0]), 0)
	elif len(inp) == 2: 
		#x-0
		if int(inp[1]) == 0: part_list = get_digit(int(inp[0]), 2)
		#sub20x
		elif int(inp) > 10 and int(inp) < 20: part_list = get_digit(int(inp[0:2]), 1)
		#x(ty)y
		else: part_list = get_digit(int(inp[0]), 2) + get_digit(int(inp[1]), 0)
		
	elif len(inp) == 3:
		#x-00
		if inp[1:3] == '00': part_list = get_digit(int(inp[0]), 0) + get_digit(int(inp[0:3]), 3)
		#x-hundred and y-ty
		elif inp[2] == '0':	part_list = get_digit(int(inp[0]), 0) + get_digit(int(inp[0:3]), 4) + get_digit(int(inp[1]), 2)
		#x-hundred and sub10y
		elif int(inp[1:3]) < 10 and int(inp[1:3]) > 0:	part_list = get_digit(int(inp[0]), 0) + get_digit(int(inp[0:3]), 4) + get_digit(int(inp[2]), 0)
		#x-hundred and sub20y
		elif int(inp[1:3]) < 20 and int(inp[1:3]) > 10:	part_list = get_digit(int(inp[0]), 0) + get_digit(int(inp[0:3]), 4) + get_digit(int(inp[1:3]), 1)
		#x-hundred and y(ty)-z
		else: part_list = get_digit(int(inp[0]), 0) + get_digit(int(inp[0:3]), 4) + get_digit(int(inp[1]), 2) + get_digit(int(inp[2]), 0)
	else: part_list = get_digit(int(inp[0]), 0) + get_digit(int(inp[0:4]), 4)     
	return part_list

grand = 0
for i in range(1,1001):
	grand = grand + len(partition(str(i)))
	
print grand