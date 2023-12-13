def	make_columns(rows):
	columns = list()
	for i in range(len(rows[0])):
		columns.append(''.join([x[i] for x in rows]))
	return columns


def	try_fix(line, previous_line):
	smudge_fixed = False
	for char1, char2 in zip(line, previous_line):
		if char1 is not char2 and smudge_fixed == False:
			smudge_fixed = True
		elif char1 is not char2:
			return False
	return True


def	check_rest(lines, i, smudge_fixed):
	for j in range(1, len(lines[i:])):
		if i - 1 - j < 0:
			break
		if lines[i + j] != lines[i - 1 - j]:
			if smudge_fixed == False and try_fix(lines[i + j], lines[i - 1 - j]) == True:
				smudge_fixed = True
			else:
				return False
	return smudge_fixed


def	find_reflection(lines):
	for i in range(1, len(lines)):
		if lines[i] == lines[i - 1] or try_fix(lines[i], lines[i - 1]) == True:
			smudge_fixed = lines[i] != lines[i - 1]
			if check_rest(lines, i, smudge_fixed) == True:
				return i
	return 0


def main():
	with open("input") as file:
		patterns = file.read().split("\n\n")

	result = 0
	for pattern in patterns:
		rows = pattern.split("\n")
		columns = make_columns(rows)
		result += find_reflection(rows) * 100
		result += find_reflection(columns)
	print(result)


if __name__ == "__main__":
	main()