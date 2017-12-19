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
	sent = 0
	threads.append(Thread(target=threadCalc, args=(ins, 0, sent)))
	threads.append(Thread(target=threadCalc, args=(ins, 1, sent)))
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	return sent

rcv0 = False
rcv1 = False

rcv0Queue = []
rcv1Queue = []

rcv0Lock = threading.Lock()
rcv1Lock = threading.Lock()
rcv0QLock = threading.Lock()
rcv1QLock = threading.Lock()

def threadCalc(ins, tid, sent):
	global rcv0
	global rcv1
	global rcv0Queue
	global rcv1Queue
	global rcv0Lock
	global rcv1Lock
	reg = {}
	reg['p'] = tid
	i = 0
	insSent = 0
	while True:
		data = parseIns(ins[i])
		print(tid, data)
		if reg.get(data['reg']) == None:
			reg[data['reg']] = 0
		if data.get('val') is not None and \
		not isinstance(data['val'], int) and \
		reg.get(data['val']) == None:
			reg[data['val']] = 0
		# Parse instructions
		if data['ins'] == 'snd':
			if tid == 0:
				rcv1QLock.acquire()
				print(tid, 'rcv1QLock Acquired')
				rcv1Queue.append(data['reg'])
				rcv1QLock.release()
				print(tid, 'rcv1QLock Released')
			else:
				insSent += 1
				rcv0QLock.acquire()
				print(tid, 'rcv0QLock Acquired')
				rcv0Queue.append(data['reg'])
				rcv0QLock.release()
				print(tid, 'rcv0QLock Released')
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
			if i == 0:
				while True:
					rcv0Lock.acquire()
					#print(tid, 'rcv0Lock Acquired')
					rcv0 = True
					print(tid, rcv1)
					if len(rcv0Queue) > 0:
						reg[data['reg']] = rcv0Queue.pop()
						#rcv0 = False
						rcv0Lock.release()
						#print(tid, 'rcv0Lock Released')
						break;
					rcv0Lock.release()
					#print(tid, 'rcv0Lock Released')
					#rcv1Lock.acquire()
					#print(tid, 'rcv1Lock Acquired')
					print(tid, 'check', rcv1)
					if rcv1:
						#rcv1Lock.release()
						#print(tid, 'rcv1Lock Released')
						#print(tid, 'Returning')
						return
					#rcv1Lock.release()
			else:
				while True:
					rcv1Lock.acquire()
					#print(tid, 'rcv1Lock Acquired')
					rcv1 = True
					print(tid, rcv0)
					if len(rcv1Queue) > 0:
						reg[data['reg']] = rcv1Queue.pop()
						#rcv1 = False
						rcv1Lock.release()
						#print(tid, 'rcv1Lock Released')
						break;
					rcv1Lock.release()
					#print(tid, 'rcv1QLock Released')
					#rcv0Lock.acquire()
					#print(tid, 'rcv0Lock Acquired')
					print(tid, 'check', rcv0)
					if rcv0:
						#rcv0Lock.release()
						#print(tid, 'rcv0Lock Released')
						print(tid, 'Returning')
						return
					#rcv0Lock.release()

		elif data['ins'] == 'jgz':
			if reg[data['reg']] > 0:
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
	#print(stuff)
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
	# Part 2:

