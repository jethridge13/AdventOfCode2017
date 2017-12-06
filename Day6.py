import unittest
import copy

def calc(array):
	l = [copy.deepcopy(array)]
	n = 0
	while True:
		array = redis(array)
		if array in l:
			return n + 1
		l.append(copy.deepcopy(array))
		n += 1
	return -1

def calc2(array):
	l = {tuple((array)): 0}
	n = 0
	while True:
		array = redis(array)
		if l.get(tuple(array)) != None:
			return n - l.get(tuple(array)) + 1
		n += 1
		l[tuple((array))] = n
	return -1

def redis(array):
	# maxTup[0] = index
	# maxTup[1] = value
	maxTup = (-1, -1)
	for i in range(len(array)):
		if array[i] > maxTup[1]:
			maxTup = (i, array[i])
	n = array[maxTup[0]]
	array[maxTup[0]] = 0
	i = maxTup[0] + 1
	while n > 0:
		if i >= len(array):
			i = 0
		array[i] += 1
		n -= 1
		i += 1
	return array

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			l = line.split()
			l = list(map(int, l))
			data = l
	return data

class TestDay6(unittest.TestCase):

	def test1(self):
		t = [0, 2, 7, 0]
		self.assertEqual(redis(t), [2, 4, 1, 2])

	def test2(self):
		t = [2, 4, 1, 2]
		self.assertEqual(redis(t), [3, 1, 2, 3])

	def test3(self):
		t = [3, 1, 2, 3]
		self.assertEqual(redis(t), [0, 2, 3, 4])

	def test4(self):
		t = [0, 2, 3, 4]
		self.assertEqual(redis(t), [1, 3, 4, 1])

	def test5(self):
		t = [1, 3, 4, 1]
		self.assertEqual(redis(t), [2, 4, 1, 2])

	def test6(self):
		t = [0, 2, 7, 0]
		self.assertEqual(calc(t), 5)

	def test7(self):
		t = [0, 2, 7, 0]
		self.assertEqual(calc2(t), 4)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 3156
	print(calc(load('Day6.txt')))
	# Part 2: 1610
	print(calc2(load('Day6.txt')))
