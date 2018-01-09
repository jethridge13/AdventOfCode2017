import unittest
import math

def calc(clues, rounds):
	# Note: Could make more efficient by
	# Just calling transformParts several times instead
	# of reforming and breaking down
	image = [['.', '#', '.'],
			 ['.', '.', '#'],
			 ['#', '#', '#']]
	for i in range(rounds):
		print(i)
		parts = breakIntoParts(image)
		image = transformParts(parts, clues)
		printImage(image)
	return score(image)

def lineify(array):
	s = ''
	for i in array:
		s += '/'
		for j in i:
			s += j
	return s[1:]

def arrayify(line):
	s = []
	l = []
	for i in line:
		if i == '/':
			s.append(l)
			l = []
		else:
			l.append(i)
	s.append(l)
	return s

def score(array):
	s = 0
	for i in array:
		for j in i:
			if j == '#':
				s += 1
	return s

def getNextPiece(clue, m):
	r = clue
	for i in range(4):
		l = lineify(r)
		if m.get(l):
			return m[l]
		l = lineify(r[::-1])
		if m.get(l):
			return m[l]
		r = list(zip(*r[::-1]))
	print('Error with following clue: ', clue)
	print(lineify(clue))
	return '-1'

def breakIntoParts(array):
	parts = []
	if len(array) % 3 == 0:
		for i in range(0, len(array), 3):
			for j in range(0, len(array), 3):
				l1 = [array[i][j], array[i][j+1], array[i][j+2]]
				l2 = [array[i+1][j], array[i+1][j+1], array[i+1][j+2]]
				l3 = [array[i+2][j], array[i+2][j+1], array[i+2][j+2]]
				l = [l1, l2, l3]
				parts.append(l)
	else:
		for i in range(0, len(array), 2):
			for j in range(0, len(array[i]), 2):
				l1 = [array[i][j], array[i][j+1]]
				l2 = [array[i+1][j], array[i+1][j+1]]
				l = [l1, l2]
				parts.append(l)
	print(parts)
	return parts

def transformParts(parts, clues):
	newParts = []
	for i in parts:
		newParts.append(arrayify(getNextPiece(i, clues)))
	if len(newParts) == 1:
		return newParts[0]
	r = []
	items = 0
	for i in newParts:
		items += len(i)
	w = int(math.sqrt(items))
	print('items', items, 'w', w)
	# print(newParts)
	index = 0
	while(newParts):
		r.append([])
		for i in range(w - 1):
			try:
				r[-1] += newParts[index].pop(0)
				if len(newParts[index]) <= 0:
					newParts.pop(index)
					index -= 1
			except Exception as e:
				print(i, index)
				printImage(newParts)
				printImage(r)
				raise e
			index += 1
		index = 0
	return r

def load(path):
	data = {}
	with open(path, 'r') as f:
		for line in f:
			l = line.replace('\n', '').split(' => ')
			data[l[0]] = l[1]
	return data

def printImage(array):
	for i in array:
		for j in i:
			print(j, end='')
		print()

class TestDay14(unittest.TestCase):

	def test1(self):
		t = [['.', '.'],
			['.', '#']]
		self.assertEqual(lineify(t), '../.#')
		t = [['.', '#', '.'],
			 ['.', '.', '#'],
			 ['#', '#', '#']]
		self.assertEqual(lineify(t), '.#./..#/###')

	def test2(self):
		t = load('Day21Test1.txt')
		self.assertEqual(t.get('../.#'), '##./#../...')

	def test3(self):
		t = [['#', '#', '.', '#', '#', '.'],
			['#', '.', '.', '#', '.', '.'],
			['.', '.', '.', '.', '.', '.'],
			['#', '#', '.', '#', '#', '.'],
			['#', '.', '.', '#', '.', '.'],
			['.', '.', '.', '.', '.', '.']]
		self.assertEqual(score(t), 12)

	def test4(self):
		m = load('Day21Test1.txt')
		t1 = [['.', '.'],
			  ['.', '#']]
		t2 = [['#', '.'],
			  ['.', '.']]
		s = '##./#../...'
		self.assertEqual(getNextPiece(t1, m), s)
		self.assertEqual(getNextPiece(t2, m), s)

	def test5(self):
		t = [['.', '#', '.'],
			 ['.', '.', '#'],
			 ['#', '#', '#']]
		s = lineify(t)
		self.assertEqual(arrayify(s), t)

	def test6(self):
		t = [['#', '#', '.', '#', '#', '.'],
			['#', '.', '.', '#', '.', '.'],
			['.', '.', '.', '.', '.', '.'],
			['#', '#', '.', '#', '#', '.'],
			['#', '.', '.', '#', '.', '.'],
			['.', '.', '.', '.', '.', '.']]
		t = breakIntoParts(t)
		s = [['#', '#', '.'],
			['#', '.', '.'],
			['.', '.', '.']]
		self.assertEqual(len(t), 4)
		self.assertEqual(t[0], s)
		self.assertEqual(t[1], s)
		self.assertEqual(t[2], s)
		self.assertEqual(t[3], s)
		t = [['#', '.', '.', '#'],
			 ['.', '.', '.', '.'],
			 ['.', '.', '.', '.'],
			 ['#', '.', '.', '#']]
		t = breakIntoParts(t)
		s1 = [['#', '.'],
			  ['.', '.']]
		s2 = [['.', '#'],
			  ['.', '.']]
		s3 = [['.', '.'],
			  ['#', '.']]
		s4 = [['.', '.'],
			  ['.', '#']]
		self.assertEqual(len(t), 4)
		self.assertEqual(t[0], s1)
		self.assertEqual(t[1], s2)
		self.assertEqual(t[2], s3)
		self.assertEqual(t[3], s4)

	def test7(self):
		t = [['.', '#', '.'],
			 ['.', '.', '#'],
			 ['#', '#', '#']]
		t = breakIntoParts(t)
		s = [['#', '.', '.', '#'],
			 ['.', '.', '.', '.'],
			 ['.', '.', '.', '.'],
			 ['#', '.', '.', '#']]
		l = load('Day21Test1.txt')
		self.assertEqual(transformParts(t, l), s)
		t = [['#', '.', '.', '#'],
			 ['.', '.', '.', '.'],
			 ['.', '.', '.', '.'],
			 ['#', '.', '.', '#']]
		t = breakIntoParts(t)
		s = [['#', '#', '.', '#', '#', '.'],
			['#', '.', '.', '#', '.', '.'],
			['.', '.', '.', '.', '.', '.'],
			['#', '#', '.', '#', '#', '.'],
			['#', '.', '.', '#', '.', '.'],
			['.', '.', '.', '.', '.', '.']]
		self.assertEqual(transformParts(t, l), s)

	def test8(self):
		t = load('Day21Test1.txt')
		self.assertEqual(calc(t, 2), 12)

if __name__ == '__main__':
	#unittest.main()
	# Part 1:
	calc(load('Day21.txt'), 5)
	# Part 2:

