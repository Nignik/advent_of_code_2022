from collections import defaultdict

data = open('input.in', 'r').readlines()

last, depth, dir_space, result = -1, 0, 0, 0

class Node:
    
    def __init__(self, size, children, parent):
        self.size = size
        self.parent = parent
        self.children = children

    def add_child(self, child):
        self.children.append(child)

        return self.children

def find_sum(node):
    children = node.children
    size = node.size
    # print(f'size: {size}')

    for child in children:
        size += find_sum(child)
    return size

folders = defaultdict(Node)
home_dir = Node(0, [], None)
last_working_directory = Node(0, [], None)
working_dir = home_dir

status = False

for line in data:
    if line[0] == '$':
        if 'cd /' in line:
            depth = 0
            working_dir = home_dir
        elif 'cd ..' in line:
            depth -= 1
            working_dir = working_dir.parent
        elif 'cd' in line:
            depth += 1
            position = line.rfind('cd')
            current = line.split()[2]
            # if current in folders.values():
            working_dir = folders[current]
            # else:
            #     folders[current] = Node(0, [], working_dir)
            #     working_dir.add_child(folders[current])
            #     working_dir = folders[current]
    else:
        if 'dir' in line:
            splited = line.split()[1]
            temp = Node(0, [], working_dir)
            working_dir.add_child(temp)
            folders[splited] = temp
        else:
            size = int(line.split()[0])
            temp = Node(size, [], working_dir)
            working_dir.add_child(temp)

results = []


for i in folders.values():
    sum = find_sum(i)
    results.append(sum)

    if sum <= 100000:
        result += sum

for i in results:
    print(i)

print(result)



# for line in data:
#     pos = line.rfind('-')
#     if pos > last and '=' not in line:
#         temp = Node(0, [], working_dir)
#         folders.append(temp)
#         working_dir.add_child(temp)
#         working_dir = temp
#         depth += 1
#     elif pos < last:
#         depth -= 1
#         working_dir = working_dir.parent
#
#     if '=' in line:
#         # temp = Node(0, [], working_dir)
#         # folders.append(temp)
#         # working_dir.add_child(temp)
#         # working_dir = temp
#         value = int(line[line.rfind('=') + 1:line.rfind(')')])
#         current = Node(value, [], working_dir)
#         working_dir.add_child(current)
#
#     last = pos

# result = 0
# results = []
#
# for i in folders:
#     sum = find_sum(i)
#     results.append(sum)
#
#     if sum <= 100000:
#         result += sum
#
#     for z in i.children:
#         z.size
#         print(z.size)
#
#     print('--------------------------------------------------------------')
#
#
# for i in folders[0].children:
#      print(i.size)
#
# print(result)
# print(results)