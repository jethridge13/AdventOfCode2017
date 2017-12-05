import unittest

def calc(array):
	i = 0
	steps = 0
	while i >= 0 and i < len(array):
		steps += 1
		array[i] += 1
		i = i + array[i] - 1
	return steps

def calc2(array):
	i = 0
	steps = 0
	while i >= 0 and i < len(array):
		steps += 1
		dif = 1
		if array[i] >= 3:
			dif = -1
		array[i] += dif
		i = i + array[i] - dif
	return steps

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			l = int(line)
			data.append(l)
	return data

class TestDay5(unittest.TestCase):

	def test1(self):
		t = [0, 3, 0, 1, -3]
		self.assertEqual(calc(t), 5)

	def test2(self):
		t = [0, 3, 0, 1, -3]
		self.assertEqual(calc2(t), 10)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 364539
	print(calc(load('Day5.txt')))
	# Part 2: 27477714
	print(calc2(load('Day5.txt')))

