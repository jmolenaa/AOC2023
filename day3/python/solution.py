class numb:
	def __init__(self, x, y, num):
		self.x = x
		self.y = y
		self.num = num

def atoi(x, y):
	number = 0
	while lines[x][y].isdigit():
		number = number * 10 + ord(lines[x][y]) - 48
		y += 1
	return number 


def check_if_already_in(new_number, temp_numbers):
	for number in numbers:
		if number.x == new_number.x and number.y == new_number.y:
			return
	numbers.append(new_number)
	temp_numbers.append(new_number)


# checks if current position is a digit, if so atoi on it 
# and checks if we already have the number in the list
# if not we append it to the list of current symbol number and all numbers
def find_number(x, y, temp_numbers):
	if lines[x][y].isdigit():
		while y >= 0 and lines[x][y].isdigit():
			y -= 1
		y += 1
		new_number = numb(x, y, atoi(x, y))
		check_if_already_in(new_number, temp_numbers)


def check_adjacent():

	# list to store all the numbers next to current symbol
	temp_numbers = list()

	# loops through adjacent chars checkign for out of bounds
	for x in range(i - 1, i + 2):
		if x < 0 or x >= len(lines):
			continue
		for y in range(j - 1, j + 2):
			if y < 0 or y >= len(line):
				continue
			find_number(x, y, temp_numbers)

	# checks if we have a gear
	if len(temp_numbers) == 2 and lines[i][j] == "*":
		numbers_gear.append(temp_numbers[0].num * temp_numbers[1].num)



lines = open("input").readlines()

# two lists where I store the numbers for later
numbers = list()
numbers_gear = list()


# loops over all characters finding the symbols in the input and then checking for adjacent numbers
for i, line in enumerate(lines):
	for j, c in enumerate(line):
		if not c.isdigit() and c != "." and c !="\n":
			check_adjacent()


result_part1 = 0
result_part2 = 0

for number in numbers:
	result_part1 += number.num
print("result of part1: ", result_part1)

for number in numbers_gear:
	result_part2 += number
print("result of part2: ", result_part2)

