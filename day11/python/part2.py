def get_distance_columns(x1, x2, empty_columns):
	xmin = min(x1, x2)
	steps = 0
	while xmin < max(x1, x2):
		if xmin in empty_columns:
			steps += 999999
		steps += 1
		xmin += 1
	return steps

def get_distance_rows(y1, y2, empty_rows):
	ymin = min(y1, y2)
	steps = 0
	while ymin < max(y1, y2):
		if ymin in empty_rows:
			steps += 999999
		steps += 1
		ymin += 1
	return steps

def main():
	lines = open("input").readlines()
	galaxies = list()
	empty_rows = list()
	empty_columns = list()
	for i, line in enumerate(lines):
		lines[i] = line.strip()



	inserted = 0

	for i, line in enumerate(lines):
		if line == len(line) * line[0]:
			empty_rows.append(i)
			# print(line)
			# print("hey")

	print(empty_rows)
	# for i, line in enumerate(lines):
	# 	if inserted == 1:
	# 		inserted = 0
	# 		continue
	# 	if line == len(line) * line[0]:
	# 		lines.insert(i, line)
	# 		inserted = 1
	# 		# print(line)
	# 		# print("hey")
	# inserted = 0
	print (len(lines[0]))
	i = 0
	# i = 0
	while i < len(lines[0]):
		# if inserted == 1:
		# 	inserted = 0
		# 	i += 1
		# 	continue
		same = 1
		# print("next", i)
		for j in range(len(lines)):
			# print (lines[0][i], lines[j][i])
			if lines[0][i] != lines[j][i]:
				same = 0
				break
		if same == 1:
			empty_columns.append(i)
			# print("HIIIII")
			# for j in range(len(lines)):
			# 	lines[j] = lines[j][:i] + "." + lines[j][i:]
			# 	inserted = 1
		i += 1
	# while i < len(lines[0]):
	# 	if inserted == 1:
	# 		inserted = 0
	# 		i += 1
	# 		continue
	# 	same = 1
	# 	# print("next", i)
	# 	for j in range(len(lines)):
	# 		# print (lines[0][i], lines[j][i])
	# 		if lines[0][i] != lines[j][i]:
	# 			same = 0
	# 			break
	# 	if same == 1:
	# 		# print("HIIIII")
	# 		for j in range(len(lines)):
	# 			lines[j] = lines[j][:i] + "." + lines[j][i:]
	# 			inserted = 1
	# 	i += 1

	print(empty_columns)
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char == "#":
				galaxies.append([j, i])
	
	# for line in lines:
	# 	print(line)
	# print(galaxies)

	result = 0
	for i, galaxy in enumerate(galaxies):
		j = i + 1
		while j < len(galaxies):
			x1,y1 = galaxy[0], galaxy[1]
			x2,y2 = galaxies[j][0], galaxies[j][1]
			print(x1, y1)
			print(x2, y2)
			stepsx = get_distance_columns(x1, x2, empty_columns)
			stepsy = get_distance_rows(y1, y2, empty_rows)
			print("STEPS", stepsx, stepsy)
			result += stepsx + stepsy

			# result += get_distance_columns(x1, x2, empty_columns)
			# result += get_distance_rows(y1, y2, empty_rows)
			# result += abs(galaxy[0] - galaxies[j][0]) + abs(galaxy[1] - galaxies[j][1])
			j += 1
	print(result)
			



	




if __name__ == "__main__":
	main()