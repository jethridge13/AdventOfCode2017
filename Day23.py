import unittest

def calc(ins):
	reg = { 'a': 0, 'b': 0, 'c': 0,
		'd': 0, 'e': 0, 'f': 0, 'h': 0
	}
	i = 0
	mulCount = 0
	while i < len(ins):
		data = parseIns(ins[i])
		# Parse instructions
		if data['ins'] == 'set':
			if isinstance(data['val'], int):
				reg[data['reg']] = data['val']
			else:
				reg[data['reg']] = reg[data['val']]
		elif data['ins'] == 'sub':
			if isinstance(data['val'], int):
				reg[data['reg']] -= data['val']
			else:
				reg[data['reg']] -= reg[data['val']]
		elif data['ins'] == 'mul':
			mulCount += 1
			if isinstance(data['val'], int):
				reg[data['reg']] *= data['val']
			else:
				reg[data['reg']] *= reg[data['val']]
		elif data['ins'] == 'jnz':
			if (checkInt(data['reg'])):
				n = data['reg']
			else:
				n = reg[data['reg']]
			if n != 0:
				if isinstance(data['val'], int):
					i += data['val'] - 1
				else:
					i += reg[data['val']] - 1
		i += 1
	return mulCount

def parseIns(line):
	line = line.replace('\n', '')
	stuff = line.split(' ')
	data = {}
	data['ins'] = stuff[0]
	data['reg'] = stuff[1]
	if len(stuff) > 2:
		if checkInt(stuff[2]):
			data['val'] = int(stuff[2])
		else:
			data['val'] = stuff[2]
	return data

def checkInt(s):
	if type(s) == int:
		return True
	if s[0] in ('-', '+'):
		return s[1:].isdigit()
	return s.isdigit()

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

class TestDay23(unittest.TestCase):

	def test1(self):
		t = parseIns('set X Y')
		self.assertEqual(t['ins'], 'set')
		self.assertEqual(t['reg'], 'X')
		self.assertEqual(t['val'], 'Y')


if __name__ == '__main__':
	#unittest.main()
	# Part 1: 8281
	print(calc(load('Day23.txt')))
	# Part 2:

