import sys

def touching(H, T):
	return abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1

def moveT(posH, posT):
	dc = abs(posH[0] - posT[0])
	dr = abs(posH[1] - posT[1])
	
	

	return posT


def moveH(direction, posH, code):
	
	posH[0] += code[direction][0]
	posH[1] += code[direction][1]

	return posH

def moveLine(line, posT, code):
	direction = line[0]
	value = int(line[2::])

	for i in range(value):
		posT[0] = list(moveH(direction, posT[0], code))
		
		for i in range(1, 10):
			posH = list(posT[i - 1])
			T = list(posT[i])
			if not touching(posH, T):
				sign_x = 0 if posH[0] == T[0] else (posH[0] - T[0]) / abs(posH[0] - T[0])
				sign_y = 0 if posH[1] == T[1] else (posH[1] - T[1]) / abs(posH[1] - T[1])

				T[0] += sign_x
				T[1] += sign_y
			posT[i] = list(T)

		pos_set.add(str(posT[-1][0]) + ',' + str(posT[-1][1]))

	print(f'head: {posT[0]}')
	print(f'tail: {posT[1]}')
	print()
	return posT

def solution_1(lines, pos_set):
	posT = [[12, 15] for i in range(10)]

	code = {
		'R': [1, 0],
		'L': [-1, 0],
		'U': [0, -1],
		'D': [0, 1]
	}

	for line in lines:
		change = moveLine(line, posT, code)
		for j in range(10):
			posT[j] = list(change[j])
		print(posT)
		pos_set.add(str(posT[-1][0]) + ',' + str(posT[-1][1]))

	print(len(pos_set))


if __name__ == '__main__':
	infile = sys.argv[1] if len(sys.argv)>1 else 'input.in'
	data = open(infile).read().strip()
	lines = [x for x in data.split('\n')]
	pos_set = set()
	solution_1(lines, pos_set)