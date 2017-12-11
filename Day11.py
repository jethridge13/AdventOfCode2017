import unittest
from collections import Counter
import copy

def calc(path):
	cnt = Counter(path)
	cancel(cnt, 'n', 's')
	cancel(cnt, 'ne', 'sw')
	cancel(cnt, 'nw', 'se')
	while (combine(cnt, 'ne', 'nw', 'n')
		or combine(cnt, 'ne', 's', 'se')
		or combine(cnt, 'nw', 's', 'sw')
		or combine(cnt, 'se', 'n', 'ne')
		or combine(cnt, 'sw', 'n', 'nw')
		or combine(cnt, 'sw', 'se', 's')):
		cancel(cnt, 'n', 's')
		cancel(cnt, 'ne', 'sw')
		cancel(cnt, 'nw', 'se')

	return cnt['n'] + cnt['ne'] + cnt['se'] + cnt['s'] + cnt['sw'] + cnt['nw']

def calc2(path):
	m = 0
	for i in range(len(path)):
		l = path[:i+1]
		m = max(m, calc(l))
	return m

def cancel(cnt, dir1, dir2):
	# Returns True if list was modified
	# Otherwise returns False
	c = copy.copy(cnt)
	if cnt[dir1] >= cnt[dir2]:
		cnt[dir1] = cnt[dir1] - cnt[dir2]
		cnt[dir2] = 0
	else:
		cnt[dir2] = cnt[dir2] - cnt[dir1]
		cnt[dir1] = 0
	return not c == cnt

def combine(cnt, dir1, dir2, result):
	c = copy.copy(cnt)
	while cnt[dir1] > 0 and cnt[dir2] > 0:
		cnt[dir1] -= 1
		cnt[dir2] -= 1
		cnt[result] += 1
	return not c == cnt

def load(path):
	with open(path, 'r') as f:
		data = f.read()
	return data.split(',')

class TestDay11(unittest.TestCase):

	def test1(self):
		t = ['ne', 'ne', 'ne']
		self.assertEqual(calc(t), 3)

	def test2(self):
		t = ['ne', 'ne', 'sw', 'sw']
		self.assertEqual(calc(t), 0)

	def test3(self):
		t = ['ne', 'ne', 's', 's']
		self.assertEqual(calc(t), 2)

	def test4(self):
		t = ['se', 'sw', 'se', 'sw', 'sw']
		self.assertEqual(calc(t), 3)

	def test5(self):
		# Self defined tests
		t = ['n', 'se']
		self.assertEqual(calc(t), 1)
		t = ['ne', 'nw']
		self.assertEqual(calc(t), 1)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 707
	print(calc(load('Day11.txt')))
	# Part 2: 1490
	print(calc2(load('Day11.txt')))
