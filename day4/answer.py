file = open('input.in', 'r')
lines = file.readlines()

cnt = 0

for line in lines:
	line = line.strip()
	line = line.split(',')
	assignment = [line[0].split('-'), line[1].split('-')]

	if (((int(assignment[0][0]) >= int(assignment[1][0])) and (int(assignment[0][1]) <= int(assignment[1][1]))) or 
			((int(assignment[0][0]) <= int(assignment[1][0])) and (int(assignment[0][1]) >= int(assignment[1][1])))):
		cnt += 1

print(cnt)