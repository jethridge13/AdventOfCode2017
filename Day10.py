import unittest

def calc(l, lengths):
	skipSize = 0
	index = 0
	endIndex = -1
	for i in lengths:
		if i == 0:
			index += skipSize
			skipSize += 1
			continue
		endIndex = index + i
		l2 = []
		for j in range(index, endIndex):
			l2.append(l[j % len(l)])
		l2 = l2[::-1]
		for i in l2:
			l[index] = i
			index += 1
			index = index % len(l)
		index += skipSize
		index = index % len(l)
		skipSize += 1
	return l[0] * l[1]

def calc2(l, lengths, skipSize=0, index=0):
	# TODO
	endIndex = -1
	for i in lengths:
		if i == 0:
			index += skipSize
			skipSize += 1
			continue
		endIndex = index + i
		l2 = []
		for j in range(index, endIndex):
			l2.append(l[j % len(l)])
		l2 = l2[::-1]
		for i in l2:
			l[index] = i
			index += 1
			index = index % len(l)
		index += skipSize
		index = index % len(l)
		skipSize += 1
	return l[0] * l[1], index, skipSize

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return list(map(int, data.split(',')))

def loadString(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def transformIntoASCII(s):
	data = []
	for i in s:
		data.append(ord(i))
	return data

def appendSequence(s):
	return transformIntoASCII(s) + [17, 31, 73, 47, 23]

def sparseToDense(l):
	# TODO
	return

def xorBlock(l):
	x = l[0]
	for i in range(1, len(l)):
		x = x ^ l[i]
	return x

def toHex(l):
	s = ''
	for i in l:
		s += '{:02x}'.format(i)
	return s

class TestDay10(unittest.TestCase):

	def test1(self):
		t1 = [0, 1, 2, 3, 4]
		t2 = [3, 4, 1, 5]
		self.assertEqual(calc(t1, t2), 12)

	def test2(self):
		t1 = 'Day10.txt'
		self.assertEqual(load(t1), 
			[106, 16, 254, 226, 55, 2, 1, 166, 177, 247, 93, 0, 255, 228, 60, 36])

	def test3(self):
		t = 'Day10.txt'
		self.assertEqual(loadString(t).replace('\n', ''), '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36')

	def test4(self):
		t = '1,2,3'
		self.assertEqual(transformIntoASCII(t), [49, 44, 50, 44, 51])

	def test5(self):
		t = '1,2,3'
		self.assertEqual(appendSequence(t), [49, 44, 50, 44, 51, 17, 31, 73, 47, 23])

	def test6(self):
		t = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
		self.assertEqual(xorBlock(t), 64)

	def test7(self):
		t = [64, 7, 255]
		self.assertEqual(toHex(t), '4007ff')
	
if __name__ == '__main__':
	unittest.main()
	# Part 1: 11413
	print(calc(list(range(0, 256)), load('Day10.txt')))
	# Part 2:
