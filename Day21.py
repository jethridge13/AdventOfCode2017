import unittest

def calc():
	return -1

def lineify(array):
	s = ''
	for i in array:
		s += '/'
		for j in i:
			s += j
	return s[1:]

def score(array):
	s = 0
	for i in array:
		for j in i:
			if j == '#':
				s += 1
	return s

def getNextPiece(clue, m):
	# TODO Go through all possible rotations and flips
	return -1

def load(path):
	data = {}
	with open(path, 'r') as f:
		for line in f:
			l = line.replace('\n', '').split(' => ')
			data[l[0]] = l[1]
	return data

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

if __name__ == '__main__':
	unittest.main()
	# Part 1:

	# Part 2:

