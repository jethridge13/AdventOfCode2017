import unittest

def calc(data):
	length = range(len(data))
	closestI = -1
	closest = 1000000
	for i in length:
		c = abs(data[i]['a']['x']) + abs(data[i]['a']['y']) + abs(data[i]['a']['z'])
		if c < closest:
			closest = c
			closestI = i
	return closestI

def calc2(data):
	turnsWOCol = 0
	while turnsWOCol < 1000:
		cMap = checkForCollisions(data)
		dataBefore = data
		data = removeCollisions(data, cMap)
		if len(data) == len(dataBefore):
			turnsWOCol += 1
		else:
			turnsWOCol = 0
		data = moveParticles(data)
	return len(data)

def checkForCollisions(data):
	pMap = {}
	cMap = {}
	for i in data:
		check = tuple(data[i]['p'].values())
		if pMap.get(check):
			cMap[check] = 1
		else:
			pMap[check] = 1
	return cMap

def removeCollisions(data, cMap):
	toDel = []
	for i in data.keys():
		check = tuple(data[i]['p'].values())
		if cMap.get(check):
			toDel.append(i)
	for i in toDel:
		del data[i]
	return data

def moveParticles(data):
	for i in data:
		a = data[i]['a']
		v = data[i]['v']
		p = data[i]['p']
		data[i]['v']['x'] += a['x']
		data[i]['v']['y'] += a['y']
		data[i]['v']['z'] += a['z']
		data[i]['p']['x'] += v['x']
		data[i]['p']['y'] += v['y']
		data[i]['p']['z'] += v['z']
	return data

def load(path):
	data = {}
	i = 0
	with open(path, 'r') as f:
		for line in f:
			l = line.split(', ')
			d = {}
			d['p'] = breakIntoLetters(l[0])
			d['v'] = breakIntoLetters(l[1])
			d['a'] = breakIntoLetters(l[2])
			data[i] = d
			i += 1
	return data

def breakIntoLetters(line):
	data = {}
	line = line[line.index('<') + 1:line.index('>')]
	line = line.split(',')
	data['x'] = int(line[0])
	data['y'] = int(line[1])
	data['z'] = int(line[2])
	return data

class TestDay20(unittest.TestCase):

	def test1(self):
		t = 'p=< 3,0,0>'
		self.assertEqual(breakIntoLetters(t)['x'], 3)
		t = 'a=<-1,0,0>'
		self.assertEqual(breakIntoLetters(t)['x'], -1)

	def test2(self):
		t = load('Day20Test1.txt')
		self.assertEqual(t[0]['p']['x'], 3)
		self.assertEqual(t[0]['p']['y'], 0)
		self.assertEqual(t[1]['p']['x'], 4)

	def test3(self):
		t = load('Day20Test1.txt')
		self.assertEqual(calc(t), 0)

	def test4(self):
		t = load('Day20Test2.txt')
		self.assertEqual(calc2(t), 1)

	def test5(self):
		t = load('Day20Test3.txt')
		self.assertEqual(len(checkForCollisions(t)), 1)

	def test6(self):
		t = load('Day20Test3.txt')
		self.assertEqual(
			len(removeCollisions(t, checkForCollisions(t))),
			1)


if __name__ == '__main__':
	#unittest.main()
	# Part 1: 144
	print(calc(load('Day20.txt')))
	# Part 2: 477
	print(calc2(load('Day20.txt')))
