import unittest
from threading import Thread
import threading

def calc(ins):
	reg = {}
	i = 0
	lastPlayedSound = 0
	while True:
		data = parseIns(ins[i])
		if reg.get(data['reg']) == None:
			reg[data['reg']] = 0
		if data.get('val') is not None and \
		not isinstance(data['val'], int) and \
		reg.get(data['val']) == None:
			reg[data['val']] = 0
		# Parse instructions
		if data['ins'] == 'snd':
			if checkInt(data['reg']):
				lastPlayedSound = data['reg']
			else:
				lastPlayedSound = reg[data['reg']]
		elif data['ins'] == 'set':
			if isinstance(data['val'], int):
				reg[data['reg']] = data['val']
			else:
				reg[data['reg']] = reg[data['val']]
		elif data['ins'] == 'add':
			if isinstance(data['val'], int):
				reg[data['reg']] += data['val']
			else:
				reg[data['reg']] += reg[data['val']]
		elif data['ins'] == 'mul':
			if isinstance(data['val'], int):
				reg[data['reg']] *= data['val']
			else:
				reg[data['reg']] *= reg[data['val']]
		elif data['ins'] == 'mod':
			if isinstance(data['val'], int):
				reg[data['reg']] %= data['val']
			else:
				reg[data['reg']] %= reg[data['val']]
		elif data['ins'] == 'rcv':
			if reg[data['reg']] != 0:
				return lastPlayedSound
		elif data['ins'] == 'jgz':
			if reg[data['reg']] > 0:
				if isinstance(data['val'], int):
					i += data['val'] - 1
				else:
					i += reg[data['val']] - 1

		i += 1
	return lastPlayedSound

def calc2Single(ins):
	rcv0Q = []
	rcv1Q = []
	waiting0 = False
	waiting1 = False
	reg0 = {'p': 0}
	reg1 = {'p': 1}
	sent = 0
	i0 = 0
	i1 = 1
	while True:
		while not waiting0:
			data = parseIns(ins[i0])
			#print(data)
			if reg0.get(data['reg']) == None:
				reg0[data['reg']] = 0
			if data.get('val') is not None and \
			not isinstance(data['val'], int) and \
			reg0.get(data['val']) == None:
				reg0[data['val']] = 0
			# Parse instructions
			if data['ins'] == 'snd':
				if checkInt(data['reg']):
					rcv1Q.append(int(data['reg']))
				else:
					rcv1Q.append(reg0[data['reg']])
			elif data['ins'] == 'set':
				if isinstance(data['val'], int):
					reg0[data['reg']] = data['val']
				else:
					reg0[data['reg']] = reg0[data['val']]
			elif data['ins'] == 'add':
				if isinstance(data['val'], int):
					reg0[data['reg']] += data['val']
				else:
					reg0[data['reg']] += reg0[data['val']]
			elif data['ins'] == 'mul':
				if isinstance(data['val'], int):
					reg0[data['reg']] *= data['val']
				else:
					reg0[data['reg']] *= reg0[data['val']]
			elif data['ins'] == 'mod':
				if isinstance(data['val'], int):
					reg0[data['reg']] %= data['val']
				else:
					reg0[data['reg']] %= reg0[data['val']]
			elif data['ins'] == 'rcv':
				if len(rcv0Q) > 0:
					reg0[data['reg']] = rcv0Q.pop(0)
				else:
					waiting0 = True
					i0 -= 1
			elif data['ins'] == 'jgz':
				if checkInt(data['reg']) and int(data['reg']) > 0:
					if isinstance(data['val'], int):
						i0 += data['val'] - 1
					else:
						i0 += reg0[data['val']] - 1
				elif reg0[data['reg']] > 0:
					if isinstance(data['val'], int):
						i0 += data['val'] - 1
					else:
						i0 += reg0[data['val']] - 1
			i0 += 1

		while not waiting1:
			data = parseIns(ins[i1])
			#print(data)
			if reg1.get(data['reg']) == None:
				reg1[data['reg']] = 0
			if data.get('val') is not None and \
			not isinstance(data['val'], int) and \
			reg1.get(data['val']) == None:
				reg1[data['val']] = 0
			# Parse instructions
			if data['ins'] == 'snd':
				sent += 1
				if checkInt(data['reg']):
					rcv0Q.append(int(data['reg']))
				else:
					rcv0Q.append(reg1[data['reg']])
			elif data['ins'] == 'set':
				if isinstance(data['val'], int):
					reg1[data['reg']] = data['val']
				else:
					reg1[data['reg']] = reg1[data['val']]
			elif data['ins'] == 'add':
				if isinstance(data['val'], int):
					reg1[data['reg']] += data['val']
				else:
					reg1[data['reg']] += reg1[data['val']]
			elif data['ins'] == 'mul':
				if isinstance(data['val'], int):
					reg1[data['reg']] *= data['val']
				else:
					reg1[data['reg']] *= reg1[data['val']]
			elif data['ins'] == 'mod':
				if isinstance(data['val'], int):
					reg1[data['reg']] %= data['val']
				else:
					reg1[data['reg']] %= reg1[data['val']]
			elif data['ins'] == 'rcv':
				if len(rcv1Q) > 0:
					reg1[data['reg']] = rcv1Q.pop(0)
				else:
					waiting1 = True
					i1 -= 1
			elif data['ins'] == 'jgz':
				if checkInt(data['reg']) and int(data['reg']) > 0:
					if isinstance(data['val'], int):
						i1 += data['val'] - 1
					else:
						i1 += reg1[data['val']] - 1
				elif reg1[data['reg']] > 0:
					if isinstance(data['val'], int):
						i1 += data['val'] - 1
					else:
						i1 += reg1[data['val']] - 1
			i1 += 1
		if (waiting0 and waiting1) and not len(rcv0Q) and not len(rcv1Q):
			return sent
		waiting0 = False
		waiting1 = False
	return sent

def checkInt(s):
	if s[0] in ('-', '+'):
		return s[1:].isdigit()
	return s.isdigit()

def parseIns(line):
	line = line.replace('\n', '')
	stuff = line.split(' ')
	data = {}
	data['ins'] = stuff[0]
	data['reg'] = stuff[1]
	if len(stuff) > 2:
		if checkInt(stuff[2]):
			data['val'] = int(stuff[2])
		else:
			data['val'] = stuff[2]
	return data

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data

class TestDay18(unittest.TestCase):

	def test1(self):
		t = parseIns('snd X')
		self.assertEqual(t['ins'], 'snd')
		self.assertEqual(t['reg'], 'X')
		t = parseIns('set X Y')
		self.assertEqual(t['ins'], 'set')
		self.assertEqual(t['reg'], 'X')
		self.assertEqual(t['val'], 'Y')

	def test2(self):
		t = load('Day18Test1.txt')
		self.assertEqual(calc(t), 4)

	def test3(self):
		t = load('Day18Test2.txt')
		self.assertEqual(calc2Single(t), 3)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 8600
	print(calc(load('Day18.txt')))
	# Part 2: 7239
	print(calc2Single(load('Day18.txt')))
