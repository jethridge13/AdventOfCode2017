import unittest

def calc(data):
	severity = 0
	for i in data.keys():
		if isZero(i, data[i]):
			severity += i * data[i]
	return severity

def calc2(data):
	step = -1
	found = False
	while True:
		step += 1
		found = False
		for i in data.keys():
			if isZero(i + step, data[i]):
				found = True
				break
		if not found:
			return step


def isZero(step, arrayLen):
	return step % (2 * arrayLen - 2) == 0

def getPos(step, arrayLen):
	pos = step % (2 * arrayLen - 2)
	if pos >= arrayLen:
		return pos - 2
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
		t = load('Day13Test1.txt')
		self.assertEqual(calc(t), 24)

	def test3(self):
		t = load('Day13Test1.txt')
		self.assertEqual(calc2(t), 10)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 1588
	print(calc(load('Day13.txt')))
	# Part 2: 3865118
	print(calc2(load('Day13.txt')))
