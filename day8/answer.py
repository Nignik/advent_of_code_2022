def string_reverse(s):
	return s[::-1]
data = open('input.in', 'r').readlines()

row = 0
col = 0

positions = {}
rows = [[] for _ in range(len(data[0]))] 
x = -1
y = -1

matrix = [[0 for _ in range(len(data[0]) - 1)] for j in range(len(data))]
#print(matrix)



for line in data:
	line = line.strip()
	row += 1
	y = -1
	col = 0
	for num in line:
		col += 1
		if int(num) > y:
			positions[(col, row)] = True
			
			#print(f'col: {col}\nrow: {row}')
			#print()
			y = int(num)
		matrix[col-1][row-1] = int(num)
		rows[col].append(int(num))
		
	y = -1
	col = len(line) + 1
	for num in string_reverse(line):
		col -= 1
		if int(num) > y:
			
			positions[(col, row)] = True
			#print(f'col: {col}\nrow: {row}')
			#print()
			y = int(num)
		matrix[col-1][row-1] = int(num)

#print(rows)
col = 0
row = 0

for i in rows:
	x = -1
	row = 0
	#print(i)
	if len(i) > 0:
		col += 1
		for num in i:
			row += 1
			if int(num) > x:
				positions[(col, row)] = True
				#print(f'col: {col}\nrow: {row}')
				#print()
				x = int(num)
			matrix[col-1][row-1] = int(num)
		x = -1
		row = len(i) + 1
		i.reverse()
		for num in i:
			row -= 1
			if int(num) > x:
				positions[(col, row)] = True
				#print(f'col: {col}\nrow: {row}')
				#print()
				x = int(num)
			matrix[col-1][row-1] = int(num)

cnt = 0
#print(matrix)

for i in positions.values():
	if i:
		cnt += 1

#print(cnt)


#answer 2 ---------------------------------------------------------------------------

print(matrix)

view = 1
max_view = 0

length = len(matrix)
width = len(matrix[0])

for row in range(length - 1):
	for col in range(width - 1):
		tree = matrix[col][row]
		view = 1
		i = 1
		if (col != 0) and (row != 0) and (col != width - 1) and (row != length - 1):
			print(tree)
			print(f'column: {col}')
			mareker = False
			while tree > matrix[col + i][row]:
				i += 1			
				if col + i == width:
					mareker = True
					break
			if mareker:
				view *= i - 1
			else:
				view *= i
			print(f'view: {view}\ni: {i}')
			mareker = False
			i = 1
			while tree > matrix[col - i][row]:
				i += 1
				if col - i < 0:		
					mareker = True
					break
			if mareker:
				view *= i - 1
			else:
				view *= i
			print(f'view: {view}\ni: {i}')
			mareker = False
			i = 1
			while tree > matrix[col][row + i]:
				i += 1
				if row + i == length:
					mareker = True
					break
			if mareker:
				view *= i - 1
			else:
				view *= i
			print(f'view: {view}\ni: {i}')
			mareker = False
			i = 1
			while tree > matrix[col][row - i]:
				i += 1
				if row - i < 0:
					mareker = True
					break
			if mareker:
				view *= i - 1
			else:
				view *= i
			print(f'view: {view}\ni: {i}')
			print('-----------------------------------------------------')
			i = 1
		
		max_view = max(max_view, view)

print(max_view)
