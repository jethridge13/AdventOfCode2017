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

def calc2Main(l, lengths):
	index = 0
	skipSize = 0
	lengths = appendSequence(lengths)
	for i in range(64):
		check, index, skipSize = calc2(l, lengths, skipSize, index)
	hsh = sparseToDense(l)
	return hsh


def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return list(map(int, data.split(',')))

def loadString(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	data = data.replace('\n', '')
	return data

def transformIntoASCII(s):
	data = []
	for i in s:
		data.append(ord(i))
	return data

def appendSequence(s):
	return transformIntoASCII(s) + [17, 31, 73, 47, 23]

def sparseToDense(l):
	# Given the 256 numbers, break into 16 blocks
	data = []
	for i in range(16):
		n = i * 16
		x = xorBlock(l[n:n+16])
		data.append(x)
	return toHex(data)

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

	def test8(self):
		t = ''
		self.assertEqual(calc2Main(list(range(0, 256)), t), 'a2582a3a0e66e6e86e3812dcb672a272')

	def test9(self):
		t = 'AoC 2017'
		self.assertEqual(calc2Main(list(range(0, 256)), t), '33efeb34ea91902bb2f59c9920caa6cd')

	def test10(self):
		t = '1,2,3'
		self.assertEqual(calc2Main(list(range(0, 256)), t), '3efbe78a8d82f29979031a4aa0b16a9d')
		t = '1,2,4'
		self.assertEqual(calc2Main(list(range(0, 256)), t), '63960835bcdc130f0b66d7ff4f6a5a8e')
	
	def test11(self):
		t = loadString('Day10.txt')
		self.assertEqual(t, '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36')

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 11413
	print(calc(list(range(0, 256)), load('Day10.txt')))
	# Part 2: 7adfd64c2a03a4968cf708d1b7fd418d
	print(calc2Main(list(range(0, 256)), loadString('Day10.txt')))