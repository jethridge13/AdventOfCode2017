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

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return list(map(int, data.split(',')))
		

class TestDay10(unittest.TestCase):

	def test1(self):
		t1 = [0, 1, 2, 3, 4]
		t2 = [3, 4, 1, 5]
		self.assertEqual(calc(t1, t2), 12)

	def test2(self):
		t1 = 'Day10.txt'
		self.assertEqual(load(t1), 
			[106, 16, 254, 226, 55, 2, 1, 166, 177, 247, 93, 0, 255, 228, 60, 36])
	
if __name__ == '__main__':
	#unittest.main()
	# Part 1: 11413
	print(calc(list(range(0, 256)), load('Day10.txt')))
	# Part 2:
