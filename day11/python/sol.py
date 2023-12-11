# gets distance by creating a set of coordinates between the first and second coordinate
# then creates a set of coordinates that repeat in that set and the empty row/column set
# uses the amount of coordinates in our new set witht the expansion rate to add the proper amount of steps
# + the abs value between coord1 and coord2
def get_distance_in_axis(coord1, coord2, empty_axis, expansion):
	coord_visited = set(range(min(coord1, coord2), max(coord1, coord2)))
	empty_lines = coord_visited & empty_axis
	steps = len(empty_lines) * expansion + abs(coord1 - coord2)
	return steps

def main():

	lines = [line.strip() for line in open("input").readlines()]

	# making a set of the x coordinates of the empty rows
	empty_rows = set()
	for i, line in enumerate(lines):
		if line == len(line) * line[0]:
			empty_rows.add(i)


	# making a set of the y coordinates of empty columns
	empty_columns = set()
	for i, char in enumerate(lines[0]):
		if all(char == lines[j][i] for j in range(len(lines))):
			empty_columns.add(i)


	# making a list of the coordinates of all the galaxies
	galaxies = list()
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char == "#":
				galaxies.append([j, i])


	# looping through the galaxies and their pairs without repeating pairs
	resultpart1, resultpart2 = 0, 0
	for i, galaxy in enumerate(galaxies):
		for galaxy_pair in galaxies[i + 1:]: # i + 1 makes sure we dont repeat pairs
			resultpart1 += get_distance_in_axis(galaxy[0], galaxy_pair[0], empty_columns, 1)
			resultpart1 += get_distance_in_axis(galaxy[1], galaxy_pair[1], empty_rows, 1)
			# 999999 because one row is part of the absolute value between coord1 and 2
			resultpart2 += get_distance_in_axis(galaxy[0], galaxy_pair[0], empty_columns, 999999)
			resultpart2 += get_distance_in_axis(galaxy[1], galaxy_pair[1], empty_rows, 999999)


	print(f"The answer to part 1 is: {resultpart1}")
	print(f"The answer to part 2 is: {resultpart2}")





if __name__ == "__main__":
	main()