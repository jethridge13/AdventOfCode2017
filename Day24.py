import unittest

def calc():
	# TODO Recursively go through all bridges
	# Then compare strengths
	return -1

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

if __name__ == '__main__':
	unittest.main()
	# Part 1:

	# Part 2:

