MAX_CHAR = 53


def common(str1, str2, str3):
	str1 = str1.strip()
	str2 = str2.strip()
	str3 = str3.strip()
	a1 = [0 for i in range(MAX_CHAR)]
	a2 = [0 for i in range(MAX_CHAR)]
	a3 = [0 for i in range(MAX_CHAR)]

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

	for i in range(0, len(str3)):
		if (str3[i].isupper()):
			a3[ord(str3[i]) - 38] += 1
		else:
			a3[ord(str3[i]) - ord('a')] += 1

	for i in range(0, 26):
		if (a1[i] > 0 and a2[i] > 0 and a3[i] > 0):
			return chr(i + ord('a'))
	for i in range(27, 53):
		if (a1[i] > 0 and a2[i] > 0 and a3[i] > 0):
			return chr(i + 38)

	return '!'

file = open('input.in', 'r')
lines = file.readlines()

cnt = 0;
groups = []

i = 0
while i < len(lines):

	for tick in range(3):
		s1 = lines[i]
		s2 = lines[i+1]
		s3 = lines[i+2]

	answer = ord(common(s1, s2, s3))

	if (answer > 90):
		cnt += answer - ord('a') + 1
	else:
		cnt += answer - ord('A') + 27

	i += 3
	

print(cnt)