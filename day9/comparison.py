com1 = open('compare1.txt').read().split('\n')
com2 = open('compare2.txt').read().split('\n')

for i in com2:
	found = False
	for j in com1:
		if i == j:
			found = True
			# print(f'{i} : {j}')
	if found == False:
		print(i)

# for i in com2:
# 	cnt = 0
# 	for j in com2:
# 		if i == j:
# 			cnt += 1
# 	if cnt >= 2:
# 		print(i)