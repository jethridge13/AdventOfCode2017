import unittest

def calc(data):
	d = treeify(data)
	n = d.itervalues().next()
	while n.parent != None:
		n = n.parent
	return n.name

def calc2(data):
	tree = treeify(data)
	rootName = calc(data)
	root = tree.get(rootName)
	index = compWeight(root)
	return -1

def compWeight(root):
	weights = []
	for i in root.children:
		weights.append(calcWeight(i))
	index = -1
	value = -1
	for i in range(len(weights)):
		n = weights[i]
		if weights.count(n) == 1:
			index = i
			value = n
			break
	if index + 1 >= len(weights):
		dif = weights[index - 1] - value
	else:
		dif = weights[index + 1] - value
	print(root.children[i].name, weights, i)
	return i

def treeify(data):
	d = {}
	for i in data:
		i = i.replace('\n', '')
		i = i.split(' -> ')
		i[0] = i[0].split(' ')
		i[0][1] = int(i[0][1].replace('(', '').replace(')', ''))
		if len(i) > 1:
			i[1] = i[1].split(', ')
		if d.get(i[0][0]) == None:
			n = Node(i[0][0], i[0][1])
			n.weight = i[0][1]
			d[i[0][0]] = n
		else:
			d.get(i[0][0]).weight = i[0][1]
		if len(i) <= 1:
			continue
		for j in i[1]:
			if d.get(j) == None:
				n = Node(j)
				d[j] = n
			d.get(j).parent = d.get(i[0][0])
			d.get(i[0][0]).children.append(d.get(j))
	return d

def calcWeight(tree):
	sum = 0
	if len(tree.children):
		for i in tree.children:
			sum += calcWeight(i)
	return sum + tree.weight


def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

class Node(object):

	def __init__(self, name, weight=-1):
		self.name = name
		self.weight = weight
		self.parent = None
		self.children = []

class TestDay7(unittest.TestCase):

	def test1(self):
		t = load('Day7Test1.txt')
		self.assertEqual(calc(t), 'tknk')

	def test2(self):
		path = load('Day7Test1.txt')
		tree = treeify(path)
		rootName = calc(path)
		root = tree.get(rootName)
		self.assertEqual(calcWeight(root.children[0]), 251)

	def test3(self):
		path = load('Day7Test1.txt')
		tree = treeify(path)
		rootName = calc(path)
		root = tree.get(rootName)
		self.assertEqual(calcWeight(root.children[1]), 243)

	def test4(self):
		path = load('Day7Test1.txt')
		tree = treeify(path)
		rootName = calc(path)
		root = tree.get(rootName)
		self.assertEqual(calcWeight(root.children[2]), 243)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: ykpsek
	print(calc(load('Day7.txt')))
	#Part 2:
	print(calc2(load('Day7.txt')))
