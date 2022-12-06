
file = open('input1.txt', 'r')
Lines = file.readlines()
stack = []

cnt = 0;

for line in Lines:
	if (line == '\n'):

		if (len(stack) >= 3):
			if (cnt > stack[-1]):
				stack.pop()
				stack.append(cnt)
				stack.sort(reverse=True)
		else:
			stack.append(cnt)
			stack.sort(reverse=True)

		cnt = 0;
	else:
		cnt += int(line.strip())

print(stack)

cnt = 0;

for i in stack:
	cnt += i

print(cnt)