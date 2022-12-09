import sys

def moveT(prevH, posH, posT):
	if posH[0] - posT[0] > 1 or posH[0] - posT[0] < -1 or posH[1] - posT[1] > 1 or posH[1] - posT[1] < -1:
		posT = prevH
		return posT
	else:
		return posT


def moveH(direction, posH, code):
	
	posH[0] += code[direction][0]
	posH[1] += code[direction][1]

	return posH

def moveLine(line, posH, posT, code):
	direction = line[0]
	prevH = []
	value = int(line[2::])
	cnt = 0

	for i in range(value):
		prevH = list(posH)
		posH = moveH(direction, posH, code)
		posT = moveT(prevH, posH, posT)
		pos_set.add(str(posT[1]) + ',' + str(posT[0]))
		cnt += 1
	return (posH, posT)

def solution_1(lines, pos_set):
	posH = [0, 0]
	posT = [0, 0]

	code = {
		'R': [1, 0],
		'L': [-1, 0],
		'U': [0, -1],
		'D': [0, 1]
	}

	for line in lines:
		change = moveLine(line, posH, posT, code)
		posH = change[0]
		posT = change[1]

	print(len(pos_set))

def solution_2(lines, pos_set):
	posH = [0, 0]
	posT = [0, 0]

	code = {
		'R': [1, 0],
		'L': [-1, 0],
		'U': [0, -1],
		'D': [0, 1]
	}

	for line in lines:
		change = moveLine(line, posH, posT, code)
		posH = change[0]
		posT = change[1]

	print(len(pos_set))

if __name__ == '__main__':
	infile = sys.argv[1] if len(sys.argv)>1 else 'input.in'
	data = open(infile).read().strip()
	lines = [x for x in data.split('\n')]
	pos_set = set()
	solution_1(lines, pos_set)


