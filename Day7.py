import unittest

def calc(data):
	d = treeify(data)
	n = d.itervalues().next()
	while n.parent != None:
		n = n.parent
	return n.name

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
	return d

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

class TestDay7(unittest.TestCase):

	def test1(self):
		t = load('Day7Test1.txt')
		self.assertEqual(calc(t), 'tknk')

if __name__ == '__main__':
	unittest.main()
	# Part 1: ykpsek
	print(calc(load('Day7.txt')))
	#Part 2:
	print(calc(load('Day7.txt')))
