def	make_columns(rows):
	columns = list()
	for i in range(len(rows[0])):
		yo = [x[i] for x in rows]
		yo = ''.join(yo)
		columns.append(yo)
	return columns

def	check_rest(lines, i):
	j = 1
	if i + j >= len(lines) or i - 1 - j < 0:
		return True
	line = lines[i + j]
	previous_line = lines[i - 1 - j]
	while line == previous_line:
		j += 1
		if i + j >= len(lines) or i - 1 - j < 0:
			return True
		line = lines[i + j]
		previous_line = lines[i - 1 - j]
	return False

def	find_reflection(lines):
	previous_line = ""
	for i, line in enumerate(lines):
		if line == previous_line:
			if check_rest(lines, i) == True:
				return i
		previous_line = line
	return 0

def main():
	with open("input") as file:
		lines = file.read().splitlines()

	result = 0
	pattern = list()
	rows = list()
	for line in lines:
		if line == "":
			print("NEW pattern \n")
			columns = make_columns(rows)
			print(rows)
			print(columns)
			result += find_reflection(rows) * 100 
			result += find_reflection(columns)
			rows.clear()
			continue
		rows.append(line)
	columns = make_columns(rows)
	result += find_reflection(rows) * 100 
	result += find_reflection(columns)
	print(result)



if __name__ == "__main__":
	main()