import unittest

def calc(s, l):
	for i in s:
		if i.startswith('s'):
			n = int(i[1:])
			l = spin(l, n)
		elif i.startswith('x'):
			args = i.split('/')
			a = int(args[0][1:])
			b = int(args[1])
			l = exchange(l, a, b)
		elif i.startswith('p'):
			args = i.split('/')
			a = args[0][1:]
			b = args[1]
			l = partner(l, a, b)
	return l

def calc2(s, l, n):
	cycle = findCycle(s, l)
	for i in range(n % cycle):
		l = calc(s, l)
	return l

def findCycle(s, l):
	lists = []
	lists.append(l)
	for i in range(100):
		l = calc(s, l)
		if l in lists:
			return len(lists)
		lists.append(l)
	return -1

def spin(l, n):
	return l[-n:] + l[:-n]

def exchange(l, n, m):
	temp = l[n]
	l = l[:n] + l[m] + l[n + 1:]
	l = l[:m] + temp + l[m + 1:]
	return l

def partner(l, a, b):
	i = l.index(a)
	j = l.index(b)
	return exchange(l, i, j)

def load(path):
	data = []
	with open(path, 'r') as f:
		data = f.read().split(',')
	return data

class TestDay14(unittest.TestCase):

	def test1(self):
		t = 'abcde'
		self.assertEqual(spin(t, 3), 'cdeab')

	def test2(self):
		t = 'eabcd'
		self.assertEqual(exchange(t, 3, 4), 'eabdc')

	def test3(self):
		t = 'eabdc'
		self.assertEqual(partner(t, 'e', 'b'), 'baedc')

	def test4(self):
		t = 'abcdefghijlmnop'
		s = ['s10']
		self.assertEqual(calc(s, t), 'fghijlmnopabcde')

	def test5(self):
		t = 'abcde'
		s = ['s1', 'x3/4', 'pe/b']
		self.assertEqual(calc(s, t), 'baedc')

	def test6(self):
		t = 'abcde'
		s = ['s1', 'x3/4', 'pe/b']
		self.assertEqual(calc2(s, t, 2), 'ceadb')

if __name__ == '__main__':
	#unittest.main()
	# Part 1: bijankplfgmeodhc
	print(calc(load('Day16.txt'), 'abcdefghijklmnop'))
	# Part 2: bpjahknliomefdgc
	print(calc2(load('Day16.txt'), 'abcdefghijklmnop', 1000000000))
