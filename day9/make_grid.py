data1 = open('compare1.txt', 'r').read().split('\n')
data2 = open('compare2.txt', 'r').read().split('\n')

grid1 = [[0 for i in range(26)] for j in range(21)]
grid2 = [[0 for i in range(26)] for j in range(21)]

# for i in grid1:
# 	print(i)

# print('-----------------------------GRID--------------------------------')

# for i in grid2:
# 	print(i)

print(data1)
print(data2)

for i in data1:
	i = i.split(',')
	i[0].replace('-', '')
	i[1].replace('-', '')
	print(i[0])
	grid1[int(i[0]) + 11][int(i[1]) + 11] = 1

for i in data2:
	i = i.split(',')
	i[0].replace('-', '')
	i[1].replace('-', '')
	grid2[int(i[0]) + 11][int(i[1]) + 11] = 1

for i in grid1:
	print(i)

print('-----------------------------GRID--------------------------------')

for i in grid2:
	print(i)