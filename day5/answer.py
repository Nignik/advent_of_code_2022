

file = open('input.in', 'r')
lines = file.readlines()

# for i in range (len(lines)):
# 	tab.append([])

moving = False
mx = 0

for line in lines:
	line = ''.join(filter(str.isalpha, line))
	line = ''.join(filter(str.isupper, line))
	mx = max(mx, len(line))

input_length = mx
tab = [[] for i in range(input_length)]

for line in lines:
	if line[0] == '\n':
		moving = True
	
	if moving:
		line = ''.join(filter(str.isdigit, line))
		if len(line) != 0:
			break

	else:
		if len(line) != 0:
			j = 0
			for i in range(1, len(line), 4):
				if line[i].isalpha():
					tab[j].append(line[i])
				j += 1
moving = False



for i in range(len(tab)):
	tab[i].reverse()

for i in tab:
	print(i)


for line in lines:
	if line[0] == 'm':
		moving = True

	if moving == True:
		print(line)
		line = line.split()
		line = [token for token in line if not token.isalpha()]
		print(line)
		mv = int(line[0]) - 1
		fr = int(line[1]) - 1
		to = int(line[2]) - 1

		fragment = tab[fr][-(mv + 1)::]
		#fragment.reverse() ----> first challenge

		tab[to].extend(fragment)
		for i in range(mv + 1):
			tab[fr].pop()
		for i in tab:
			print(i)

for i in tab:
	print(i[-1], end='')

print()


		
