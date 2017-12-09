import unittest

def calcScore(line):
	stack = []
	score = 0
	garbage = False
	skip = False
	for i in range(len(line)):
		if skip:
			skip = False
			continue
		if not garbage:
			if line[i] == '{':
				stack.append('{')
			elif line[i] == '}':
				score += len(stack)
				stack.pop()
			elif line[i] == '<':
				garbage = True
		else:
			if line[i] == '>':
				garbage = False
			elif line[i] == '!':
				skip = True
	return score

def calcGarbage(line):
	stack = []
	score = 0
	garbage = False
	skip = False
	for i in range(len(line)):
		if skip:
			skip = False
			continue
		if not garbage:
			if line[i] == '{':
				stack.append('{')
			elif line[i] == '}':
				stack.pop()
			elif line[i] == '<':
				garbage = True
		else:
			if line[i] == '>':
				garbage = False
			elif line[i] == '!':
				skip = True
			else:
				score += 1
	return score

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data.replace('\n', '')

class TestDay9(unittest.TestCase):

	def test1(self):
		t = '{}'
		self.assertEqual(calcScore(t), 1)

	def test2(self):
		t = '{{{}}}'
		self.assertEqual(calcScore(t), 6)
		t = '{{},{}}'
		self.assertEqual(calcScore(t), 5)
		t = '{{{},{},{{}}}}'
		self.assertEqual(calcScore(t), 16)

	def test3(self):
		t = '{<a>,<a>,<a>,<a>}'
		self.assertEqual(calcScore(t), 1)
		t = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
		self.assertEqual(calcScore(t), 9)

	def test4(self):
		t = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
		self.assertEqual(calcScore(t), 9)
		t = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
		self.assertEqual(calcScore(t), 3)

	def test5(self):
		t = '<>'
		self.assertEqual(calcGarbage(t), 0)

	def test6(self):
		t = '<random characters>'
		self.assertEqual(calcGarbage(t), 17)
		t = '<<<<>'
		self.assertEqual(calcGarbage(t), 3)

	def test7(self):
		t = '<{!>}>'
		self.assertEqual(calcGarbage(t), 2)
		t = '<!!>'
		self.assertEqual(calcGarbage(t), 0)
		t = '<!!!>>'
		self.assertEqual(calcGarbage(t), 0)

	def test8(self):
		t = '<{o"i!a,<{i<a>'
		self.assertEqual(calcGarbage(t), 10)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 10050
	print(calcScore(load('Day9.txt')))
	# Part2: 4482
	print(calcGarbage(load('Day9.txt')))
