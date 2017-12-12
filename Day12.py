import unittest

def calc(data):
	d = {}
	for i in data:
		base, nodes = i.split(' <-> ')
		base = int(base)
		l = list(map(int, nodes.split(',')))
		d[base] = l
	conn = {}
	conn[0] = d[0]
	newList = d[0]
	while True:
		newList = add(conn, newList, d)
		if not newList:
			break
		l = []
		for i in newList:
			l += conn[i]
		newList = l
	return len(conn.keys())

def calc2(data):
	d = {}
	for i in data:
		base, nodes = i.split(' <-> ')
		base = int(base)
		l = list(map(int, nodes.split(',')))
		d[base] = l
	groups = 0
	while len(d.keys()) > 0:
		conn = {}
		conn[list(d.keys())[0]] = d[list(d.keys())[0]]
		newList = d[list(d.keys())[0]]
		while True:
			newList = add(conn, newList, d)
			if not newList:
				break
			l = []
			for i in newList:
				l += conn[i]
			newList = l
		for i in conn.keys():
			del d[i]
		groups += 1
	return groups

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

def add(d, l, conns):
	newList = []
	for i in l:
		if d.get(i) == None:
			d[i] = conns.get(i)
			newList.append(i)
	return newList

class TestDay12(unittest.TestCase):

	def test1(self):
		t = load('Day12Test1.txt')
		self.assertEqual(calc(t), 6)

	def test2(self):
		t = load('Day12Test1.txt')
		self.assertEqual(calc2(t), 2)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 380
	print(calc(load('Day12.txt')))
	# Part 2: 181
	print(calc2(load('Day12.txt')))
