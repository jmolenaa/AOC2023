# with open("test_case") as file:
# 	lines = file.read().split(",")


def	find_index(list, label):
	for i, tuple in enumerate(list):
		if label == tuple[0]:
			return i
	return -1

lines = [line.strip() for line in open("input").readlines()]
print(lines)
result = 0
boxes = dict()
for line in lines:
	line = line.split(",")
	for input in line:
		value = 0
		if input.find("=") != -1:
			for char in input[:input.find("=")]:
				value = value + ord(char)
				value = value *17
				value = value % 256
			label = input[:input.find("=")]
			focus = input[input.find("=") + 1:]
			print(focus, label)
			if value in boxes:
				if find_index(boxes[value], label) != -1:
					index = find_index(boxes[value], label)
					del boxes[value][index]
					boxes[value].insert(index, (label, focus))
				else:
					boxes[value].append((label, focus))
			else:
				boxes[value] = [(label, focus)]
		elif input.find("-") != -1:
		
			for char in input[:input.find("-")]:
				value = value + ord(char)
				value = value *17
				value = value % 256
			label = input[:input.find("-")]
			focus = input[input.find("-") + 1:]
			if value in boxes:
				if find_index(boxes[value], label) != -1:
					index = find_index(boxes[value], label)
					del boxes[value][index]

				
result = 0
for key,value in boxes.items():
	for i, lens in enumerate(value):
		result += (key + 1) * (i + 1) * int((lens[1]))

print(result)