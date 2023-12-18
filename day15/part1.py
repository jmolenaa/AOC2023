# with open("test_case") as file:
# 	lines = file.read().split(",")


lines = [line.strip() for line in open("input").readlines()]
print(lines)
result = 0
for line in lines:
	line = line.split(",")
	for input in line:
		print(input)
		value = 0
		for char in input:
			value = value + ord(char)
			value = value *17
			value = value % 256
		print(value)
		result += value
		# print(result)
print(result)