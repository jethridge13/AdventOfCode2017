import unittest

def calc(array):
	sum = 0
	for i in array:
		if lineCalc(i):
			sum += 1
	return sum

def calc2(array):
	sum = 0
	for i in array:
		if lineCalc(i) and lineCalc2(i):
			sum += 1
	return sum

def lineCalc(l):
	l = l.split()
	l.sort()
	for i in range(len(l)):
		if i + 1 < len(l):
			if l[i] == l[i + 1]:
				return False
	return True

def lineCalc2(l):
	l = l.split()
	l.sort()
	for i in range(len(l)):
		s = ''.join(sorted(l[i]))
		l[i] = s
	l = ' '.join(l)
	return lineCalc(l)

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

class TestDay4(unittest.TestCase):

	def test1(self):
		t = 'aa bb cc dd ee'
		self.assertTrue(lineCalc(t))

	def test2(self):
		t = 'aa bb cc dd aa'
		self.assertFalse(lineCalc(t))

	def test3(self):
		t = 'aa bb cc dd aaa'
		self.assertTrue(lineCalc(t))

	def test4(self):
		t = 'abcde fghij'
		self.assertTrue(lineCalc2(t))

	def test5(self):
		t = 'abcde xyz ecdab'
		self.assertFalse(lineCalc2(t))

	def test6(self):
		t = 'a ab abc abd abf abj'
		self.assertTrue(lineCalc2(t))

	def test7(self):
		t = 'iiii oiii ooii oooi oooo'
		self.assertTrue(lineCalc2(t))

	def test8(self):
		t = 'oiii ioii iioi iiio'
		self.assertFalse(lineCalc2(t))

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 451
	print(calc(load('Day4.txt')))
	#Part 2: 223
	print(calc2(load('Day4.txt')))
