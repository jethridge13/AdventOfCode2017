import unittest

def calc(l):
	# TODO Recursively go through all bridges
	# Then compare strengths
	r = buildRecursively(0, l)
	finalScore = 0
	l = []
	for i in r:
		s = score(i)
		if s > finalScore:
			finalScore = s
			l = i
	return finalScore

def buildRecursively(n, l, r=[], bridges=[]): 
	c = findAllCandidates(n, l)
	if len(l) == 0 or len(c) == 0:
		return bridges + [r]
	for i in c:
		newList = l[:]
		newList.remove(i)
		if i[0] == n:
			bridges = buildRecursively(i[1], newList, r + [i], bridges)
		else:
			bridges = buildRecursively(i[0], newList, r + [i], bridges)
	return bridges

def findAllCandidates(n, l):
	candidates = []
	for i in l:
		if i[0] == n or i[1] == n:
			candidates.append(i)
	return candidates

def score(l):
	score = 0
	for i in l:
		score += i[0] + i[1]
	return score

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			s = line.split('/')
			data.append((int(s[0]), int(s[1])))
	return data

class TestDay14(unittest.TestCase):

	def test1(self):
		t = 'Day24Test1.txt'
		data = load(t)
		self.assertEqual(data[0], (0, 2))
		self.assertEqual(data[1], (2, 2))
		self.assertEqual(data[-1], (9, 10))

	def test2(self):
		data = load('Day24Test1.txt')
		t = findAllCandidates(0, data)
		self.assertEqual(len(t), 2)
		self.assertEqual(t[0], (0, 2))
		self.assertEqual(t[1], (0, 1))

	def test3(self):
		t = [(0, 1), (10, 1), (9, 10)]
		self.assertEqual(score(t), 31)

	def test4(self):
		t = load('Day24Test1.txt')
		self.assertEqual(calc(t), 31)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 1656
	print(calc(load('Day24.txt')))
	# Part 2:

