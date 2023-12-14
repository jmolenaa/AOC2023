from array import array

def roll_rock(column, i, space):
	# if i == 0 and column[i] == 'O':
	# 	return 1
	if space == "O":
		column[i] = '.'
		# print(i, column)
		i -= 1
		while i >= 0:
			if column[i] == "O" or column[i] == "#":
				break
			i -= 1
		column[i + 1] = "O"
		# print(column)

		return(i + 2)
	# print(column)
	return 0

def make_columns(lines):
	columns = list()
	for i in range(len(lines[0])):
		columns.append(''.join([x[i] for x in lines]))
	return columns

def main():
	with open("input") as file:
		lines = file.read().split("\n")
	# print(lines)
	result = 0
	columns = make_columns(lines)
	for column in columns:
		column_array = list([*column])
		for i, space in enumerate(column):
			# print(column_array)
			index = roll_rock(column_array, i, space)
			if index != 0:
				# print(len(column) - index + 1)
				result += len(column) - index + 1
			# print(column_array)
		# print(column_array)
		print(result)
		# break
	# print(columns)



if __name__ == "__main__":
	main()