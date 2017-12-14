import unittest
import Day10

def calc():
	return -1

def hexToBin(hx):
	return bin(int(hx, 16))[2:]

class TestDay14(unittest.TestCase):

	def test1(self):
		t = Day10.calc2Main(list(range(0, 256)), Day10.loadString('Day10.txt'))
		self.assertEqual(t, '7adfd64c2a03a4968cf708d1b7fd418d')

	def test2(self):
		a = '1010000011000010000000010111'
		self.assertEqual(hexToBin('a0c2017'), a)

	def test3(self):
		t = 'flqrgnkx-0'
		t = Day10.calc2Main(list(range(0, 256)), t)
		print(t)
		t = hexToBin(t)
		print(t[2:10])
		self.assertEqual(t[2:10], '11010100')
		t = 'flqrgnkx-1'
		t = Day10.calc2Main(list(range(0, 256)), t)
		print(t)
		t = hexToBin(t)
		print(t[2:10])
		self.assertEqual(t[2:10], '01010101')
		t = 'flqrgnkx-2'
		t = Day10.calc2Main(list(range(0, 256)), t)
		t = hexToBin(t)
		print(t[2:10])
		self.assertEqual(t[2:10], '00001010')

if __name__ == '__main__':
	unittest.main()
	# Part 1:

	# Part 2:

