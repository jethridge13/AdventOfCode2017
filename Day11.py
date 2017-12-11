import unittest
import math

def calc(path):
	# TODO Use 3 axes instead of 2
	startX, startY, startZ = 0, 0, 0
	x, y, z = startX, startY, startZ
	for i in path:
		if i == 'n':
			x += 1
		elif i == 'ne':
			x += 0.5
			y += 1
		elif i == 'se':
			x -= 0.5
			y += 1
		elif i == 's':
			x -= 1
		elif i == 'sw':
			x -= 0.5
			y -= 1
		elif i == 'nw':
			x += 0.5
			y += 1
	return int(math.floor((abs(x + y))))

def load(path):
	with open(path, 'r') as f:
		data = f.read()
	return f.split(',')

class TestDay11(unittest.TestCase):

	def test1(self):
		t = ['ne', 'ne', 'ne']
		self.assertEqual(calc(t), 3)

	def test2(self):
		t = ['ne', 'ne', 'sw', 'sw']
		self.assertEqual(calc(t), 0)

	def test3(self):
		t = ['ne', 'ne', 's', 's']
		self.assertEqual(calc(t), 2)

	def test4(self):
		t = ['se', 'sw', 'se', 'sw', 'sw']
		self.assertEqual(calc(t), 3)

if __name__ == '__main__':
	unittest.main()
	# Part 1:

	# Part 2:

