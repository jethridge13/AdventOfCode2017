import unittest

def calc(seq):
	sum = 0
	for i in range(0, len(seq)):
		a = int(seq[i])
		if i + 1 > len(seq) - 1:
			b = int(seq[0])
		else:
			b = int(seq[i + 1])
		if a == b:
			sum += a
	return sum

def calc2(seq):
	sum = 0
	half = len(seq)/2
	for i in range(0, len(seq)):
		a = int(seq[i])
		if i + half > len(seq) - 1:
			b = int(seq[i + half - len(seq)])
		else:
			b = int(seq[i+half])
		if a == b:
			sum += a
	return sum

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

class TestDay1(unittest.TestCase):

	def test1(self):
		t = [1,1,2,2]
		self.assertEqual(calc(t), 3)

	def test2(self):
		t = [1,1,1,1]
		self.assertEqual(calc(t), 4)

	def test3(self):
		t = [1,2,3,4]
		self.assertEqual(calc(t), 0)

	def test4(self):
		t = [9,1,2,1,2,1,2,9]
		self.assertEqual(calc(t), 9)

	def test5(self):
		t = [1,2,1,2]
		self.assertEqual(calc2(t), 6)

	def test6(self):
		t = [1,2,2,1]
		self.assertEqual(calc2(t), 0)

	def test7(self):
		t = [1,2,3,4,2,5]
		self.assertEqual(calc2(t), 4)

	def test8(self):
		t = [1,2,3,1,2,3]
		self.assertEqual(calc2(t), 12)

	def test9(self):
		t = [1,2,1,3,1,4,1,5]
		self.assertEqual(calc2(t), 4)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 1171
	print(calc(load('Day1.txt')))
	# Part 2: 1024
	print(calc2(load('Day1.txt')))