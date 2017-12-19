import unittest

def calc(ins):
	reg = {}
	i = 0
	lastPlayedSound = 0
	while True:
		data = parseIns(ins[i])
		if reg.get(data['reg']) == None:
			reg[data['reg']] = 0
		if data.get('val') is not None and \
		not isinstance(data['val'], int) and \
		reg.get(data['val']) == None:
			reg[data['val']] = 0
		# Parse instructions
		if data['ins'] == 'snd':
			if checkInt(data['reg']):
				lastPlayedSound = data['reg']
			else:
				lastPlayedSound = reg[data['reg']]
		elif data['ins'] == 'set':
			if isinstance(data['val'], int):
				reg[data['reg']] = data['val']
			else:
				reg[data['reg']] = reg[data['val']]
		elif data['ins'] == 'add':
			if isinstance(data['val'], int):
				reg[data['reg']] += data['val']
			else:
				reg[data['reg']] += reg[data['val']]
		elif data['ins'] == 'mul':
			if isinstance(data['val'], int):
				reg[data['reg']] *= data['val']
			else:
				reg[data['reg']] *= reg[data['val']]
		elif data['ins'] == 'mod':
			if isinstance(data['val'], int):
				reg[data['reg']] %= data['val']
			else:
				reg[data['reg']] %= reg[data['val']]
		elif data['ins'] == 'rcv':
			if reg[data['reg']] != 0:
				return lastPlayedSound
		elif data['ins'] == 'jgz':
			if reg[data['reg']] > 0:
				if isinstance(data['val'], int):
					i += data['val'] - 1
				else:
					i += reg[data['val']] - 1

		i += 1
	return -1

def checkInt(s):
	if s[0] in ('-', '+'):
		return s[1:].isdigit()
	return s.isdigit()

def parseIns(line):
	line = line.replace('\n', '')
	stuff = line.split(' ')
	#print(stuff)
	data = {}
	data['ins'] = stuff[0]
	data['reg'] = stuff[1]
	if len(stuff) > 2:
		if checkInt(stuff[2]):
			data['val'] = int(stuff[2])
		else:
			data['val'] = stuff[2]
	return data

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

class TestDay14(unittest.TestCase):

	def test1(self):
		t = parseIns('snd X')
		self.assertEqual(t['ins'], 'snd')
		self.assertEqual(t['reg'], 'X')
		t = parseIns('set X Y')
		self.assertEqual(t['ins'], 'set')
		self.assertEqual(t['reg'], 'X')
		self.assertEqual(t['val'], 'Y')

	def test2(self):
		t = load('Day18Test1.txt')
		self.assertEqual(calc(t), 4)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 8600
	print(calc(load('Day18.txt')))
	# Part 2:

