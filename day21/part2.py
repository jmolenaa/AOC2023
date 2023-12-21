# def	make_garden_grid(lines):
# 	grid = dict()
# 	for i, line in enumerate(lines):
# 		for j, spot in enumerate(line):
# 			grid[(j, i)] = spot

# 	return grid

def main():
	with open("input") as file:
		lines = file.read().split("\n")

	width = len(lines[0])
	length = len(lines)
	# garden = make_garden_grid(lines)
	# print(garden)
	# for key,value in garden.items():
	# 	if value == "S":
	# 		start_position = list(key)
	# 		garden[key] = "."
	# 		break
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			if char == "S":
				next_positions = [(y, x)]
				
	print(next_positions)

	for i in range(64):

		positions = next_positions.copy()
		# print(len(next_positions))
		next_positions.clear()
		while positions:
			pos = positions.pop()
			# print(pos)


			if pos[0] + 1 < length and lines[pos[0] + 1][pos[1]] in ".S":
				if (pos[0] + 1, pos[1]) not in next_positions:
					next_positions.append((pos[0] + 1, pos[1]))
			if pos[0] - 1 >= 0 and lines[pos[0] - 1][pos[1]] in ".S":
				if (pos[0] - 1, pos[1]) not in next_positions:
					next_positions.append((pos[0] - 1, pos[1]))
			if pos[1] + 1 < width and lines[pos[0]][pos[1] + 1] in ".S":
				if (pos[0], pos[1] + 1) not in next_positions:
					next_positions.append((pos[0], pos[1] + 1))
			if pos[1] - 1 >= 0 and lines[pos[0]][pos[1] - 1] in ".S":
				if (pos[0], pos[1] - 1) not in next_positions:
					next_positions.append((pos[0], pos[1] - 1))
			# if (position[0] + 1, position[1]) in garden and garden[position[0] + 1, position[1]] == ".":
			# 	garden[position[0] + 1, position[1]] = 'O'
			# 	next_positions.append([position[0] + 1, position[1]])
			# if (position[0] - 1, position[1]) in garden and garden[position[0] - 1, position[1]] == ".":
			# 	garden[position[0] - 1, position[1]] = 'O'
			# 	next_positions.append([position[0] - 1, position[1]])
			# if (position[0], position[1] + 1) in garden and garden[position[0], position[1] + 1] == ".":
			# 	garden[position[0], position[1] + 1] = 'O'
			# 	next_positions.append([position[0], position[1] + 1])
			# if (position[0], position[1] - 1) in garden and garden[position[0], position[1] - 1] == ".":
			# 	garden[position[0], position[1] - 1] = 'O'
			# 	next_positions.append([position[0], position[1] - 1])


	print(len(next_positions))


		# print(i)

	part1 = 0
	part2 = 0

	# print(f"The answer to part 1 is: {part1}")
	# print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()