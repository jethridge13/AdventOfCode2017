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

def calc2(ins):
	threads = []
	sent = [0]
	threads.append(Thread(target=threadCalc, args=(ins, 0, sent)))
	threads.append(Thread(target=threadCalc, args=(ins, 1, sent)))
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	return sent[0]

rcv = [False, False]
rcvSent = [0, 0]

rcv0Queue = []
rcv1Queue = []

rcvLock = threading.Lock()
rcv0QLock = threading.Lock()
rcv1QLock = threading.Lock()

def threadCalc(ins, tid, sent):
	global rcv0
	global rcv1
	global rcv0Queue
	global rcv1Queue
	global rcvLock
	global rcvSent
	reg = {}
	reg['p'] = tid
	i = 0
	insSent = 0
	while True:
		data = parseIns(ins[i])
		print(tid, data, reg, i)
		# Create register if necessary
		if reg.get(data['reg']) == None and \
		not checkInt(data['reg']):
			reg[data['reg']] = 0
		if data.get('val') is not None and \
		not isinstance(data['val'], int) and \
		reg.get(data['val']) == None:
			reg[data['val']] = 0
		# Parse instructions
		if data['ins'] == 'snd':
			if tid == 0:
				rcv1QLock.acquire()
				if checkInt(data['reg']):
					rcv1Queue.append(int(data['reg']))
				else:
					rcv1Queue.append(reg[data['reg']])
				rcvSent[0] += 1
				rcv1QLock.release()
			else:
				insSent += 1
				rcv0QLock.acquire()
				if checkInt(data['reg']):
					rcv0Queue.append(int(data['reg']))
				else:
					rcv0Queue.append(reg[data['reg']])
				rcvSent[1] += 1
				rcv0QLock.release()
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
			if tid == 0:
				while True:
					rcvLock.acquire()
					if len(rcv0Queue) > 0:
						reg[data['reg']] = rcv0Queue.pop()
						rcvSent[1] -= 1
						popped = True
						rcv[0] = False
						rcvLock.release()
						break;
					rcv[0] = True
					rcvLock.release()
					rcvLock.acquire()
					if rcv[1]:
						rcv1QLock.acquire()
						if not popped and not rcvSent[0] and not rcvSent[1]:
							rcv1QLock.release()
							rcvLock.release()
							print(tid, 'Returning')
							return
						rcv1QLock.release()
					popped = False
					rcvLock.release()
			else:
				while True:
					rcvLock.acquire()
					if len(rcv1Queue) > 0:
						reg[data['reg']] = rcv1Queue.pop()
						rcvSent[0] -= 1
						popped = True
						rcv[1] = False
						rcvLock.release()
						break;
					rcv[1] = True
					rcvLock.release()
					rcvLock.acquire()
					if rcv[0]:
						rcv0QLock.acquire()
						if not popped and not rcvSent[0] and not rcvSent[1]:
							rcvLock.release()
							rcv0QLock.release()
							sent[0] = insSent
							print(tid, 'Returning')
							print(insSent)
							return
						rcv0QLock.release()
					popped = False
					rcvLock.release()
		elif data['ins'] == 'jgz':
			if checkInt(data['reg']) and int(data['reg']) > 0:
				if isinstance(data['val'], int):
					i += data['val'] - 1
				else:
					i += reg[data['val']] - 1
			elif reg[data['reg']] > 0:
				if isinstance(data['val'], int):
					i += data['val'] - 1
				else:
					i += reg[data['val']] - 1
		i += 1
	return insSent


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

class TestDay14(unittest.TestCase):

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
		self.assertEqual(calc2(t), 3)

if __name__ == '__main__':
	unittest.main()
	# Part 1: 8600
	print(calc(load('Day18.txt')))
	# Part 2: >6589 <7690 NOT 7201 NOT 131
	print(calc2(load('Day18.txt')))
