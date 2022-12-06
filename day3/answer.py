MAX_CHAR = 53


def common(str1, str2):
	str1 = str1.strip()
	str2 = str2.strip()
	a1 = [0 for i in range(MAX_CHAR)]
	a2 = [0 for i in range(MAX_CHAR)]

	for i in range(0, len(str1)):
		if (str1[i].isupper()):
			a1[ord(str1[i]) - 38] += 1
		else:
			a1[ord(str1[i]) - ord('a')] += 1

	for i in range(0, len(str2)):
		if (str2[i].isupper()):
			a2[ord(str2[i]) - 38] += 1
		else:
			a2[ord(str2[i]) - ord('a')] += 1

	for i in range(0, 26):
		if (a1[i] > 0 and a2[i] > 0):
			return chr(i + ord('a'))
	for i in range(27, 53):
		if (a1[i] > 0 and a2[i] > 0):
			return chr(i + 38)

	return '!'

file = open('input.in', 'r')
lines = file.readlines()

cnt = 0;

for line in lines:
	str1 = line[slice(0, len(line)//2)]
	str2 = line[slice(len(line)//2, len(line))]

	print(common(str(str1), str(str2)))
	answer = ord(common(str(str1), str(str2)))

	if (answer > 90):
		cnt += ord(common(str(str1), str(str2))) - ord('a') + 1
	else:
		cnt += ord(common(str(str1), str(str2))) - ord('A') + 27
	

print(cnt)
	