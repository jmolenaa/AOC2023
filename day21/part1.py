import time

def	make_garden_grid(lines):
	grid = dict()
	for i, line in enumerate(lines):
		for j, spot in enumerate(line):
			grid[(j, i)] = spot

	return grid
def main():
	with open("input") as file:
		lines = file.read().split("\n")

	garden = make_garden_grid(lines)
	# print(garden)
	for key,value in garden.items():
		if value == "S":
			start_position = list(key)
			garden[key] = "."
			break

	next_positions = [start_position]
	for i in range(1000):
		positions = next_positions.copy()
		# print(len(next_positions))
		# print(next_positions)

		# print(i)
		next_positions.clear()
		while positions:
			position = positions.pop()
			garden[position[0], position[1]] = '.'
			# print(position)
			if (position[0] + 1, position[1]) in garden and garden[position[0] + 1, position[1]] == ".":
				# if (position[0] + 1, position[1]) not in next_positions:
				garden[position[0] + 1, position[1]] = 'O'
				next_positions.append([position[0] + 1, position[1]])
			if (position[0] - 1, position[1]) in garden and garden[position[0] - 1, position[1]] == ".":
				# if (position[0] - 1, position[1]) not in next_positions:
				garden[position[0] - 1, position[1]] = 'O'
				next_positions.append([position[0] - 1, position[1]])
			if (position[0], position[1] + 1) in garden and garden[position[0], position[1] + 1] == ".":
				garden[position[0], position[1] + 1] = 'O'
				# if (position[0], position[1] + 1) not in next_positions:
				next_positions.append([position[0], position[1] + 1])
			if (position[0], position[1] - 1) in garden and garden[position[0], position[1] - 1] == ".":
				garden[position[0], position[1] - 1] = 'O'
				# if (position[0], position[1] - 1) not in next_positions:
				next_positions.append([position[0], position[1] - 1])


	print(len(next_positions))


		# print(i)

	part1 = 0
	part2 = 0

	# print(f"The answer to part 1 is: {part1}")
	# print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	start = time.time()
	main()
	end = time.time()
	print(end - start)