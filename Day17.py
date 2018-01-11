import unittest

def calc(steps, end):
	array, pos = genArray(steps, end)
	return array[pos + 1]

def calc2(steps, end):
	length = 1
	pos = 0
	e = -1
	for i in range(1, end):
		pos = (pos + steps) % length
		length += 1
		if pos == 0:
			e = i
		pos += 1
	return e
	
def genArray(steps, end):
	pos = 0
	array = [0]
	for i in range(end):
		array, pos = spinList(array, i + 1, pos, steps)
	return array, pos

def spinList(array, value, pos, steps):
	pos = (pos + steps) % len(array)
	return array[:pos + 1] + [value] + array[pos + 1:], pos + 1

class TestDay17(unittest.TestCase):

	def test1(self):
		self.assertEqual(spinList([0], 1, 0, 3), ([0, 1], 1))
		self.assertEqual(spinList([0, 1], 2, 1, 3), ([0, 2, 1], 1))
		self.assertEqual(spinList([0, 2, 1], 3, 1, 3), ([0, 2, 3, 1], 2))

	def test2(self):
		t, p = genArray(3, 9)
		self.assertEqual(t, [0, 9, 5, 7, 2, 4, 3, 8, 6, 1])
		self.assertEqual(p, 1)

	def test3(self):
		t = calc(3, 2017)
		self.assertEqual(t, 638)

	def test4(self):
		t = calc2(3, 10)
		self.assertEqual(t, 9)
		calc(3, 10)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 1487
	print(calc(367, 2017))
	# Part 2: 25674054
	print(calc2(367, 50000000))
