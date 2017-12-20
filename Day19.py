import unittest
import re

def calc(array):
	start = [findStart(array), 0]
	index = start
	path = []
	direction = 'S'
	lastDirection = 'N'
	moved = False
	while True:
		# print(index, direction, lastDirection)
		# Continue heading in the current direction
		if direction == 'N':
			if canContinue(array, index[0], index[1], 'N'):
				index[1] -= 1
				moved = True
		elif direction == 'S':
			if canContinue(array, index[0], index[1], 'S'):
				index[1] += 1
				moved = True
		elif direction == 'E':
			if canContinue(array, index[0], index[1], 'E'):
				index[0] += 1
				moved = True
		elif direction == 'W':
			if canContinue(array, index[0], index[1], 'W'):
				index[0] -= 1
				moved = True
		if moved:
			moved = False
			if re.match(r'[A-Z]', array[index[1]][index[0]]):
				path.append(array[index[1]][index[0]])
		else:
			# Can't continue forward, try changing directions
			if lastDirection != 'N' and canContinue(array, index[0], index[1], 'N'):
				lastDirection = 'S'
				direction = 'N'
				index[1] -= 1
				if re.match(r'[A-Z]', array[index[1]][index[0]]):
					path.append(array[index[1]][index[0]])
			elif lastDirection != 'S' and canContinue(array, index[0], index[1], 'S'):
				lastDirection = 'N'
				direction = 'S'
				index[1] += 1
				if re.match(r'[A-Z]', array[index[1]][index[0]]):
					path.append(array[index[1]][index[0]])
			elif lastDirection != 'E' and canContinue(array, index[0], index[1], 'E'):
				lastDirection = 'W'
				direction = 'E'
				index[0] += 1
				if re.match(r'[A-Z]', array[index[1]][index[0]]):
					path.append(array[index[1]][index[0]])
			elif lastDirection != 'W' and canContinue(array, index[0], index[1], 'W'):
				lastDirection = 'E'
				direction = 'W'
				index[0] -= 1
				if re.match(r'[A-Z]', array[index[1]][index[0]]):
					path.append(array[index[1]][index[0]])
			else:
				return path
	return path

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
	if s == ' ':
		return False
	if re.match(r'[A-Z\+]', s):
		return True
	if (dire == 'N' or dire == 'S'):
		if s == '|':
			return True	
		if s == '-':
			if dire == 'N':
				return canContinue(array, x, y - 1, dire)
			else:
				return canContinue(array, x, y + 1, dire)
	elif (dire == 'E' or dire == 'W'):
		if s == '-':
			return True
		if s == '|':
			if dire == 'E':
				return canContinue(array, x + 1, y, dire)
			else:
				return canContinue(array, x - 1, y, dire)
	return False

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
		self.assertTrue(canContinue(t, 5, 0, 'S'))
		self.assertTrue(canContinue(t, 5, 1, 'S'))
		self.assertTrue(canContinue(t, 5, 2, 'S'))
		self.assertTrue(canContinue(t, 5, 4, 'S'))
		self.assertFalse(canContinue(t, 5, 5, 'S'))

	def test4(self):
		t = load('Day19Test1.txt')
		self.assertEqual(calc(t), ['A', 'B', 'C', 'D', 'E', 'F'])

if __name__ == '__main__':
	#unittest.main()
	# Part 1: LXWCKGRAOY
	print(calc(load('Day19.txt')))
	# Part 2:

