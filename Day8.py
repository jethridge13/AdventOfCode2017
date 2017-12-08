import unittest

def calc(array):
	registers = {}
	for i in array:
		line = parseLine(i)
		if registers.get(line['reg']) == None:
			registers[line['reg']] = 0
		condition = parseConditoin(line['con'])
	return

def parseLine(line):
	line = line.replace('\n', '')
	ins, con = line.split(' if ')
	reg, ins, val = ins.split(' ')
	d = {}
	d['reg'] = reg
	d['ins'] = ins
	d['val'] = int(val)
	d['con'] = con
	return d

def parseCondition(ins):
	reg, con, val = ins.split(' ')
	d = {}
	d['reg'] = reg
	d['con'] = con
	d['val'] = int(val)
	return d

def evalCondition(con, d):
	c = con['con']
	reg = d[con['reg']]
	val = con['val']
	return {
		'>': lambda : reg > val,
		'<': lambda : reg < val,
		'>=': lambda: reg >= val,
		'<=': lambda: reg <= val,
		'==': lambda: reg == val,
		'!=': lambda: reg != val
	}[c]

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

class TestDay8(unittest.TestCase):

	def test1(self):
		data = load('Day8Test1.txt')
		i1 = parseLine(data[0])
		self.assertEqual(i1['reg'], 'b')
		self.assertEqual(i1['ins'], 'inc')
		self.assertEqual(i1['val'], 5)
		self.assertEqual(i1['con'], 'a > 1')

	def test2(self):
		data = load('Day8Test1.txt')
		i2 = parseLine(data[0])
		i2 = parseCondition(i2['con'])
		self.assertEqual(i2['reg'], 'a')
		self.assertEqual(i2['con'], '>')
		self.assertEqual(i2['val'], 1)

	def test3(self):
		data = load('Day8Test1.txt')
		i1 = parseLine(data[0])
		i2 = parseLine(data[1])
		i3 = parseLine(data[2])
		i4 = parseLine(data[3])
		i1 = parseCondition(i1['con'])
		i2 = parseCondition(i2['con'])
		i3 = parseCondition(i3['con'])
		i4 = parseCondition(i4['con'])
		self.assertFalse(evalCondition(i1, {'a': 0}))
		self.assertTrue(evalCondition(i2, {'b': 0}))
		self.assertFalse(evalCondition(i3, {'a': 0}))
		self.assertFalse(evalCondition(i4, {'c': 0}))

if __name__ == '__main__':
	unittest.main()
	# Part 1:

	# Part 2:
