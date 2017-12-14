import unittest
import Day10

def calc(word):
	array = arrayify(word)
	hashes = []
	count = 0
	for i in array:
		hashes.append(hexToBin(Day10.calc2Main(list(range(0, 256)), i)))
	for i in hashes:
		count += i.count('1')
	return count

def arrayify(string, size=128):
	data = []
	for i in range(size):
		data.append(string + '-' + str(i))
	return data

def hexToBin(hx):
	return bin(int(hx, 16))[2:].zfill(128)

class TestDay14(unittest.TestCase):

	def test1(self):
		t = Day10.calc2Main(list(range(0, 256)), Day10.loadString('Day10.txt'))
		self.assertEqual(t, '7adfd64c2a03a4968cf708d1b7fd418d')

	def test2(self):
		a = '1010000011000010000000010111'
		self.assertTrue(hexToBin('a0c2017').endswith(a))

	def test3(self):
		t = 'flqrgnkx-0'
		t = Day10.calc2Main(list(range(0, 256)), t)
		self.assertTrue(t.startswith('d4f76'))
		t = hexToBin(t)
		self.assertEqual(t[:8], '11010100')
		t = 'flqrgnkx-1'
		t = Day10.calc2Main(list(range(0, 256)), t)
		self.assertTrue(t.startswith('55eab3'))
		t = hexToBin(t)
		self.assertEqual(t[:8], '01010101')
		t = 'flqrgnkx-2'
		t = Day10.calc2Main(list(range(0, 256)), t)
		t = hexToBin(t)
		self.assertEqual(t[:8], '00001010')
		t = 'flqrgnkx-127'
		t = Day10.calc2Main(list(range(0, 256)), t)
		self.assertTrue(t.startswith('3ecaf0'))
		t = hexToBin(t)
		self.assertEqual(t[:8], '00111110')

	def test4(self):
		t = 'flqrgnkx'
		self.assertEqual(arrayify(t)[0], 'flqrgnkx-0')
		self.assertEqual(arrayify(t)[-1], 'flqrgnkx-127')

	def test5(self):
		t = 'flqrgnkx'
		self.assertEqual(calc(t), 8108)


if __name__ == '__main__':
	#unittest.main()
	# Part 1: 8292
	print(calc('ugkiagan'))
	# Part 2:

