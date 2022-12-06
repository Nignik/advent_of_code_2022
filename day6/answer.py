data = open('input.in').read()

occurences = [0] * 26

different, cnt = 0, 0
last = []

for i in data:

    val = ord(i) - ord('a')

    if occurences[val] == 0:
        different += 1

    occurences[val] += 1


    if cnt >= 14:
        if occurences[last[0]] == 1:
            different -= 1
        occurences[last[0]] -= 1
        last.remove(last[0])
        last.append(val)
    else:
        last.append(val)

    if different == 14:
        break

    print(last)
    
    cnt += 1
    
    
print(cnt + 1)

