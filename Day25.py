import unittest

def calc(startState, steps, rules):
	tape = [0]
	index = 0
	state = startState
	for i in range(steps):
		n = tape[index]
		tape[index] = rules[state][n]['write']
		index += rules[state][n]['move']
		state = rules[state][n]['state']
		if index < 0:
			tape.insert(0, 0)
			index += 1
		elif index >= len(tape):
			tape.append(0)
	return tape.count(1)

def calcWithRules():
	startState = 'A'
	steps = 12317297
	a = {0: {'write': 1, 'move': 1, 'state': 'B'},
		1: {'write': 0, 'move': -1, 'state': 'D'}}

	b = {0: {'write': 1, 'move': 1, 'state': 'C'},
		1: {'write': 0, 'move': 1, 'state': 'F'}}

	c = {0: {'write': 1, 'move': -1, 'state': 'C'},
		1: {'write': 1, 'move': -1, 'state': 'A'}}

	d = {0: {'write': 0, 'move': -1, 'state': 'E'},
		1: {'write': 1, 'move': 1, 'state': 'A'}}

	e = {0: {'write': 1, 'move': -1, 'state': 'A'},
		1: {'write': 0, 'move': 1, 'state': 'B'}}

	f = {0: {'write': 0, 'move': 1, 'state': 'C'},
		1: {'write': 0, 'move': 1, 'state': 'E'}}

	rules = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f}
	return calc(startState, steps, rules)

class TestDay14(unittest.TestCase):

	def test1(self):
		a = {0: {'write': 1, 'move': 1, 'state': 'B'},
			1: {'write': 0, 'move': -1, 'state': 'B'}}
		b = {0: {'write': 1, 'move': -1, 'state': 'A'},
			1: {'write': 1, 'move': 1, 'state': 'A'}}
		t = {'A': a, 'B': b}
		self.assertEqual(calc('A', 6, t), 3)


if __name__ == '__main__':
	#unittest.main()
	# Part 1: 4230
	print(calcWithRules())
	# Part 2:

