import unittest

def calc(array):
	sum = 0
	for i in array:
		mini = int(min(i))
		maxi = int(max(i))
		sum += maxi - mini
	return sum

def calc2(array):
	sum = 0
	for i in array:
		for j in range(len(i)):
			sumAdded = False
			for k in range(len(i)):
				if j == k:
					continue
				a = max(i[j], i[k])
				b = min(i[j], i[k])
				if a % b == 0:
					sum += a / b
					sumAdded = True
					break
			if sumAdded:
				break
	return int(sum)

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			l = line.split()
			l = list(map(int, l))
			data.append(l)
	return data

class TestDay2(unittest.TestCase):

	def test1(self):
		t = [
		[5,1,9,5],
		[7,5,3],
		[2,4,6,8]
		]
		self.assertEqual(calc(t), 18)

	def test2(self):
		t = [
		[5,9,2,8],
		[9,4,7,3],
		[3,8,6,5]
		]
		self.assertEqual(calc2(t), 9)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 34925
	print(calc(load('Day2.txt')))
	# Part 2: 221
	print(calc2(load('Day2.txt')))