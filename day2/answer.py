
def check(a, b):
	if (a == 'X'):
		if (b == 'A'):
			return 'Z'
		elif (b == 'B'):
			return 'X'
		else:
			return 'Y'

	elif (a == 'Y'):
		if (b == 'A'):
			return 'X'
		elif (b == 'B'):
			return 'Y'
		else:
			return 'Z'
	else:
		if (b == 'A'):
			return 'Y'
		elif (b == 'B'):
			return 'Z'
		else:
			return 'X'

def decision(a):
	if (a == 'X'):
		return 0
	elif (a == 'Y'):
		return 3
	else:
		return 6

def which(a):
	if (a == 'X'):
		return 1
	elif (a == 'Y'):
		return 2
	else:
		return 3

file = open("input", "r")
lines = file.readlines()

score = 0

for line in lines:
	score += which(check(line[2], line[0])) + decision(line[2]) 

print(score)


