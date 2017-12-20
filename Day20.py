import unittest

def calc(data):
	length = range(len(data))
	closestI = -1
	closest = 1000000
	for i in length:
		c = abs(data[i]['a']['x']) + abs(data[i]['a']['y']) + abs(data[i]['a']['z'])
		if c < closest:
			closest = c
			closestI = i
	return closestI

def calc2(data):
	return -1

def load(path):
	data = {}
	i = 0
	with open(path, 'r') as f:
		for line in f:
			l = line.split(', ')
			d = {}
			d['p'] = breakIntoLetters(l[0])
			d['v'] = breakIntoLetters(l[1])
			d['a'] = breakIntoLetters(l[2])
			data[i] = d
			i += 1
	return data

def breakIntoLetters(line):
	data = {}
	line = line[line.index('<') + 1:line.index('>')]
	line = line.split(',')
	data['x'] = int(line[0])
	data['y'] = int(line[1])
	data['z'] = int(line[2])
	return data

class TestDay14(unittest.TestCase):

	def test1(self):
		t = 'p=< 3,0,0>'
		self.assertEqual(breakIntoLetters(t)['x'], 3)
		t = 'a=<-1,0,0>'
		self.assertEqual(breakIntoLetters(t)['x'], -1)

	def test2(self):
		t = load('Day20Test1.txt')
		self.assertEqual(t[0]['p']['x'], 3)
		self.assertEqual(t[0]['p']['y'], 0)
		self.assertEqual(t[1]['p']['x'], 4)

	def test3(self):
		t = load('Day20Test1.txt')
		self.assertEqual(calc(t), 0)

	def test4(self):
		t = load('Day20Test2.txt')
		self.assertEqual(calc2(t), 1)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 144
	print(calc(load('Day20.txt')))
	# Part 2:

