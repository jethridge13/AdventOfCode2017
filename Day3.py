import unittest
import math

def calc(n):
	#a = createArray(10000, 10000)
	a = createArray(math.ceil(math.sqrt(n)) + 1, math.ceil(math.sqrt(n)) + 1)
	oneX, oneY = findN(1, a)
	nX, nY = findN(n, a)
	distance = 0
	distance += max(oneX, nX) - min(oneX, nX)
	distance += max(oneY, nY) - min(oneY, nY)
	return distance

def createArray(w, h):
	N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
	direction = {N: W, E: N, S: E, W: S}
	x, y = w // 2, h // 2
	dx, dy = S
	array = [[None] * w for _ in range(h)]
	count = 0
	while True:
		count += 1
		array[y][x] = count
		newDx, newDy = direction[dx, dy]
		newX, newY = x + newDx, y + newDy
		if (0 <= newX < w and 0 <= newY < h
			and array[newY][newX] is None):
			x, y = newX, newY
			dx, dy = newDx, newDy
		else:
			x, y = x + dx, y + dy
			if not (0 <= x < w and 0 <= y < h):
				return array

def calc2(n):
	return(createArray2(math.ceil(math.sqrt(n)) + 1, math.ceil(math.sqrt(n)) + 1, True, n))


def createArray2(w, h, jumpOut=False, n=-1):
	N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
	direction = {N: W, E: N, S: E, W: S}
	x, y = w // 2, h // 2
	dx, dy = S
	array = [[None] * w for _ in range(h)]
	adjacent = {(0, 1), (1, 0), (1, 1), (-1, 0), (-1, 1), (-1, -1), (0, -1), (1, -1)}
	while True:
		sum = 0
		for i in adjacent:
			if (0 <= x + i[0] < w and 0 <= y + i[1] < h and
				array[y + i[1]][x + i[0]] != None):
				sum += array[y + i[1]][x + i[0]]
		if sum == 0:
			array[y][x] = 1
		else:
			array[y][x] = sum
			if jumpOut and sum > n:
				return sum
		newDx, newDy = direction[dx, dy]
		newX, newY = x + newDx, y + newDy
		if (0 <= newX < w and 0 <= newY < h
			and array[newY][newX] is None):
			x, y = newX, newY
			dx, dy = newDx, newDy
		else:
			x, y = x + dx, y + dy
			if not(0 <= x < w and 0 <= y < h):
				return array


def findN(n, a):
	for i in range(len(a)):
		for j in range(len(a[i])):
			if a[i][j] == n:
				return i, j

class TestDay3(unittest.TestCase):

	def test1(self):
		self.assertEqual(calc(1), 0)

	def test2(self):
		self.assertEqual(calc(12), 3)

	def test3(self):
		self.assertEqual(calc(23), 2)

	def test4(self):
		self.assertEqual(calc(1024), 31)

	def test5(self):
		a = createArray2(5, 5)
		self.assertEqual(a[2][2], 1)
		self.assertEqual(a[2][3], 1)
		self.assertEqual(a[1][3], 2)
		self.assertEqual(a[1][2], 4)
		self.assertEqual(a[1][1], 5)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 419
	print(calc(289326))
	# Part 2: 295229
	print(calc2(289326))