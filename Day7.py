import unittest

def calc(data):
	for i in data:
		print(i)
	return

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data



class TestDay7(unittest.TestCase):

	def test1(self):
		t = load('Day7Test1.txt')
		self.assertEqual(calc(t), 'tknk')

if __name__ == '__main__':
	unittest.main()
	# Part 1:
	print(calc(load('Day7.txt')))
	#Part 2:
	print(calc(load('Day7.txt')))
