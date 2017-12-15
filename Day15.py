import unittest
from threading import Thread

def calc(aStart, aFactor, bStart, bFactor, rounds):
	count = 0
	a = aStart
	b = bStart
	for i in range(rounds):
		a = generateNumber(a, aFactor)
		b = generateNumber(b, bFactor)
		if compareLow16(a, b):
			count += 1
	return count

def calc2(aStart, aFactor, bStart, bFactor, rounds):
	threads = []
	aRes = []
	bRes = []
	threads.append(Thread(target=genArray, args=(aStart, aFactor, rounds, 4, aRes)))
	threads.append(Thread(target=genArray, args=(bStart, bFactor, rounds, 8, bRes)))
	for i in threads:
		i.start()

	results = [aRes, bRes]
	count = 0
	for i in threads:
		i.join()
	for i in range(len(results[0])):
		if compareLow16(results[0][i], results[1][i]):
			count += 1
	return count

def generateNumber(n, factor):
	return (n * factor) % 2147483647

def generateNumber2(n, factor, divisor):
	while True:
		candidate = (n * factor) % 2147483647
		if candidate % divisor == 0:
			return candidate
		n = candidate

def genArray(start, factor, rounds, divisor, res=[]):
	n = start
	data = []
	for i in range(rounds):
		r = generateNumber2(n, factor, divisor)
		data.append(r)
		res.append(r)
		n = r
	return data

def compareLow16(a, b):
	aBin = '{0:#b}'.format(a)
	bBin = '{0:#b}'.format(b)
	return aBin[-16:] == bBin[-16:]

def load(path):
	with open(path, 'r') as f:
		return f
	return -1

class TestDay14(unittest.TestCase):

	def test1(self):
		self.assertEqual(generateNumber(65, 16807), 1092455)
		self.assertEqual(generateNumber(8921, 48271), 430625591)

	def test2(self):
		self.assertTrue(compareLow16(245556042, 1431495498))
	
	def test3(self):
		self.assertEqual(calc(65, 16807, 8921, 48271, 40000000), 588)

	def test4(self):
		self.assertEqual(generateNumber2(65, 16807, 4), 1352636452)
		self.assertEqual(generateNumber2(8921, 48271, 8), 1233683848)

	def test5(self):
		self.assertEqual(calc2(65, 16807, 8921, 48271, 5000000), 309)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 638
	print(calc(289, 16807, 629, 48271, 40000000))
	# Part 2: 343
	print(calc2(289, 16807, 629, 48271, 5000000))
