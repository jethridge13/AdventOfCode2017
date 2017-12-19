import unittest
import re

def calc(array):
	start = [0, findStart(array)]
	index = start
	path = []
	direction = 'S'
	lastDirection = 'N'
	while True:
		if direction == 'N':
			if canContinue(array, index[0], index[1]):
				return -1
		elif direction == 'S':
			return -1
		elif direction == 'E':
			return -1
		elif direction == 'W':
			return -1
	return -1

def checkIndex(array, x, y):
	return array[y][x]

def canContinue(array, x, y, dire):
	if dire == 'N':
		if y - 1 > 0:
			s = checkIndex(array, x, y -1)
		else:
			return False
	elif dire == 'S':
		if y + 1 < len(array):
			s = checkIndex(array, x, y + 1)
		else:
			return False
	elif dire == 'E':
		if x + 1 < len(array[y]):
			s = checkIndex(array, x + 1, y)
	elif dire == 'W':
		if x - 1 > 0:
			s = checkIndex(array, x - 1, y)
		else:
			return False
	if re.match('A-Z+'):
		return True
	return -1

def findStart(data):
	for i in range(len(data[0])):
		if data[0][i] == '|':
			return i
	return -1

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

class TestDay14(unittest.TestCase):

	def test1(self):
		t = load('Day19Test1.txt')
		self.assertEqual(findStart(t), 5)

	def test2(self):
		t = load('Day19Test1.txt')
		self.assertEqual(checkIndex(t, 5, 2), 'A')

	def test3(self):
		t = load('Day19Test1.txt')
		self.assertTrue(canContinue(t, 0, 5, 'S'))

	def test4(self):
		t = load('Day19Test1.txt')
		self.assertEqual(calc(t), ['A', 'B', 'C', 'D', 'E'])

if __name__ == '__main__':
	unittest.main()
	# Part 1:

	# Part 2:

