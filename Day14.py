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

def calc2(word):
	array = arrayify(word)
	hashes = []
	for i in array:
		hashes.append(hexToBin(Day10.calc2Main(list(range(0, 256)), i)))
	count = 0
	sets = []
	for i in range(len(hashes)):
		for j in range(len(hashes[i])):
			setOfGroup = group(j, i, hashes, set())
			if setOfGroup:
				count += 1
				sets.append(setOfGroup)
				hashes = purgeGroup(setOfGroup, hashes)
	return count


def group(x, y, hashes, inGroup):
	if hashes[y][x] == '1' and (x, y) not in inGroup:
		inGroup.add((x, y))
		group(x, y, hashes, inGroup)
	if x - 1 >= 0 and hashes[y][x-1] == '1' and (x - 1, y) not in inGroup:
		inGroup.add((x, y))
		group(x - 1, y, hashes, inGroup)
	if x + 1 < len(hashes[y]) and hashes[y][x+1] == '1' and (x + 1, y) not in inGroup:
		inGroup.add((x, y))
		group(x + 1, y, hashes, inGroup)
	if y - 1 >= 0 and hashes[y-1][x] == '1' and (x, y - 1) not in inGroup:
		inGroup.add((x, y))
		group(x, y - 1, hashes, inGroup)
	if y + 1 < len(hashes) and hashes[y+1][x] == '1' and (x, y + 1) not in inGroup:
		inGroup.add((x, y))
		group(x, y + 1, hashes, inGroup)
	return inGroup

def purgeGroup(group, hashes):
	for i in group:
		word = hashes[i[1]]
		index = i[0]
		s = word[:index] + '0' + word[index + 1:]
		hashes[i[1]] = s
	return hashes

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

	def test6(self):
		t = ['110',
			 '100',
			 ',010']
		self.assertEqual(group(0, 0, t, set()), {(0,0), (0, 1), (1, 0)})

	def test7(self):
		t = ['110',
			 '100',
			 '010']
		a = ['000',
			 '000',
			 '010']
		g = group(0, 0, t, set())
		self.assertEqual(purgeGroup(g, t), a)
	
	def test8(self):
		t = ['110',
			 '100',
			 '010']
		a = ['000',
			 '000',
			 '000']
		count = 0
		sets = []
		for i in range(len(t)):
			for j in range(len(t[i])):
				setOfGroup = group(j, i, t, set())
				if setOfGroup:
					count += 1
					sets.append(setOfGroup)
					t = purgeGroup(setOfGroup, t)
		self.assertEqual(t, a)
		self.assertEqual(count, 2)
	
	def test9(self):
		t = 'flqrgnkx'
		self.assertEqual(calc2(t), 1242)


if __name__ == '__main__':
	#unittest.main()
	# Part 1: 8292
	print(calc('ugkiagan'))
	# Part 2: 1069, but off by 1?
	# TODO: I got close to the right answer and was able to guess
	# but I should update this to work every time
	print(calc2('ugkiagan'))
