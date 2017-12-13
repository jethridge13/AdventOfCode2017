import unittest

def calc(data):
	return -1

def getPos(step, arrayLen):
	if arrayLen == 2:
		return step % arrayLen
	pos = 0
	pos = step % ((arrayLen  * 2) - 1)
	if pos >= arrayLen:
		print(pos)
		pos = arrayLen - pos + 1
	return pos

def load(path):
	data = {}
	with open(path, 'r') as f:
		for line in f:
			s = line.replace('\n', '')
			k, v = s.split(': ')
			k = int(k)
			v = int(v)
			data[k] = v
	return data

class TestDay13(unittest.TestCase):

	def test1(self):
		t = load('Day13Test1.txt')
		d = {0: 3, 1: 2, 4: 4, 6: 4}
		self.assertEqual(t, d)

	def test2(self):
		arrayLen = 3
		self.assertEqual(getPos(0, arrayLen), 0)
		self.assertEqual(getPos(1, arrayLen), 1)
		self.assertEqual(getPos(2, arrayLen), 2)
		self.assertEqual(getPos(3, arrayLen), 1)
		self.assertEqual(getPos(4, arrayLen), 0)
		self.assertEqual(getPos(5, arrayLen), 1)
		self.assertEqual(getPos(6, arrayLen), 2)
		self.assertEqual(getPos(7, arrayLen), 1)
	
	def test3(self):
		arrayLen = 2
		self.assertEqual(getPos(0, arrayLen), 0)
		self.assertEqual(getPos(1, arrayLen), 1)
		self.assertEqual(getPos(2, arrayLen), 0)
		self.assertEqual(getPos(3, arrayLen), 1)

if __name__ == '__main__':
	unittest.main()
	# Part 1:

	# Part 2:

