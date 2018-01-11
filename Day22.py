import unittest
import math

def calc(m, b):
	x = math.floor(len(m) / 2)
	y = math.floor(len(m[0]) / 2)
	d = 'N'
	c = 0
	for i in range(b):
		m, x, y, d, c = moveVirus(m, x, y, d, c)
	return c

def calc2(m, b):
	x = math.floor(len(m) / 2)
	y = math.floor(len(m[0]) / 2)
	d = 'N'
	c = 0
	for i in range(b):
		m, x, y, d, c = moveVirus2(m, x, y, d, c)
	return c

def moveVirus(m, x, y, d, c):
	infected = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
	clean = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
	m, x, y = addToMap(m, x, y)
	if m[y][x] == '#':
		d = infected[d]
		m[y][x] = '.'
	else:
		d = clean[d]
		m[y][x] = '#'
		c += 1
	if d == 'N':
		y -= 1
	elif d == 'E':
		x += 1
	elif d == 'S':
		y += 1
	else:
		x -= 1
	return m, x, y, d, c

def moveVirus2(m, x, y, d, c):
	infected = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
	clean = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
	flag = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
	m, x, y = addToMap(m, x, y)
	if m[y][x] == '#':
		d = infected[d]
		m[y][x] = 'F'
	elif m[y][x] == 'W':
		m[y][x] = '#'
		c += 1
	elif m[y][x] == 'F':
		d = flag[d]
		m[y][x] = '.'
	else:
		d = clean[d]
		m[y][x] = 'W'
	if d == 'N':
		y -= 1
	elif d == 'E':
		x += 1
	elif d == 'S':
		y += 1
	else:
		x -= 1
	return m, x, y, d, c

def addToMap(m, x, y):
	if y + 1 >= len(m):
		l = ['.'] * len(m[y])
		m.append(l)
	if y - 1 <= 0:
		l = ['.'] * len(m[y])
		m.insert(0, l)
		y += 1
	if x + 1 >= len(m[y]):
		for i in m:
			i.append('.')
	if x - 1 <= 0:
		for i in m:
			i.insert(0, '.')
		x += 1
	return m, x, y

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			l = line.replace('\n', '')
			data.append(list(l))
	return data

class TestDay22(unittest.TestCase):

	def test1(self):
		m = [['.', '.', '#'],
			['#', '.', '.'],
			['.', '.', '.']]
		t = calc(m, 7)
		self.assertEqual(t, 5)
	
	def test2(self):
		m = load('Day22Test1.txt')
		t = calc(m, 7)
		self.assertEqual(t, 5)
		t = calc(m, 70)
		self.assertEqual(t, 41)
		t = calc(m, 10000)
		self.assertEqual(t, 5587)

	def test3(self):
		m = load('Day22Test1.txt')
		t = calc2(m, 100)
		self.assertEqual(t, 26)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 5538
	print(calc(load('Day22.txt'), 10000))
	# Part 2: 2511090
	print(calc2(load('Day22.txt'), 10000000))
