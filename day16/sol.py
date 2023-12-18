def	handle_empty(current_ray, grid, rays, direction_vectors):
	x = current_ray[0] + direction_vectors[current_ray[2]][0]
	y = current_ray[1] + direction_vectors[current_ray[2]][1]
	new_pos = (x, y)
	if new_pos in grid:
		rays.append((x, y, current_ray[2]))

def	handle_backslash(current_ray, grid, rays, direction_vectors):
	# dictionary that connects the current direction with the direction
	# we will be going if encountering a \ mirror
	directions_backwards_slash = {"E" : "S", "W" : "N", "N" : "W", "S" : "E"}

	new_dir = directions_backwards_slash[current_ray[2]]
	x = current_ray[0] + direction_vectors[new_dir][0]
	y = current_ray[1] + direction_vectors[new_dir][1]
	new_pos = (x, y)
	if new_pos in grid:
		rays.append((x, y, new_dir))


def	handle_forwardsslash(current_ray, grid, rays, direction_vectors):
	# dictionary that connects the current direction with the direction
	# we will be going if encountering a / mirror
	directions_forward_slash = {"E" : "N", "W" : "S", "N" : "E", "S" : "W"}

	new_dir = directions_forward_slash[current_ray[2]]
	x = current_ray[0] + direction_vectors[new_dir][0]
	y = current_ray[1] + direction_vectors[new_dir][1]
	new_pos = (x, y)
	if new_pos in grid:
		rays.append((x, y, new_dir))

def	handle_horizontal(current_ray, grid, rays, direction_vectors):

	# if ray encounters a pointy end it just continues in the same direction
	if current_ray[2] == "E" or current_ray[2] == "W":
		x = current_ray[0] + direction_vectors[current_ray[2]][0]
		y = current_ray[1] + direction_vectors[current_ray[2]][1]
		new_pos = (x, y)
		if new_pos in grid:
			rays.append((x, y, current_ray[2]))

	# if it encounters a flat end it will split into east and west direction
	# so we add two rays
	else:
		x = current_ray[0] + direction_vectors["E"][0]
		y = current_ray[1] + direction_vectors["E"][1]
		new_pos = (x, y)
		if new_pos in grid:
			rays.append((x, y, "E"))
		x = current_ray[0] + direction_vectors["W"][0]
		y = current_ray[1] + direction_vectors["W"][1]
		new_pos = (x, y)
		if new_pos in grid:
			rays.append((x, y, "W"))

def	handle_vertical(current_ray, grid, rays, direction_vectors):

	# if ray encounters a pointy end it just continues in the same direction
	if current_ray[2] == "N" or current_ray[2] == "S":
		x = current_ray[0] + direction_vectors[current_ray[2]][0]
		y = current_ray[1] + direction_vectors[current_ray[2]][1]
		new_pos = (x, y)
		if new_pos in grid:
			rays.append((x, y, current_ray[2]))
	
	# if it encounters a flat end it will split into east and west direction
	# so we add two rays
	else:
		x = current_ray[0] + direction_vectors["N"][0]
		y = current_ray[1] + direction_vectors["N"][1]
		new_pos = (x, y)
		if new_pos in grid:
			rays.append((x, y, "N"))
		x = current_ray[0] + direction_vectors["S"][0]
		y = current_ray[1] + direction_vectors["S"][1]
		new_pos = (x, y)
		if new_pos in grid:
			rays.append((x, y, "S"))

def	check_tile(current_ray, grid, rays):

	# dictionary that creates vectors depending on direction we're going
	direction_vectors = {"E" : (1, 0), "W" : (-1, 0), "N" : (0, -1), "S" : (0, 1)}

	current_tile = grid[(current_ray[0], current_ray[1])]

	# analyses our current tile and based on it will add new rays to our current rays list
	if current_tile == ".":
		handle_empty(current_ray, grid, rays, direction_vectors)
	elif current_tile == "\\":
		handle_backslash(current_ray, grid, rays, direction_vectors)
	elif current_tile == "/":
		handle_forwardsslash(current_ray, grid, rays, direction_vectors)
	elif current_tile == "-":
		handle_horizontal(current_ray, grid, rays, direction_vectors)
	elif current_tile == "|":
		handle_vertical(current_ray, grid, rays, direction_vectors)


def	get_energised_tiles_for_ray(initial_ray, grid):

	# print(grid)
	# set that we will be adding coordinates we've visited plus the directions the beam was heading in
	visited = set()

	# a list that keeps track of all the rays we have bouncing around
	# keeps info about the current position and the direction it's heading
	# will be adding more dependign on mirrors encountered
	rays = [initial_ray]

	while rays:

		# gets latest ray
		current_ray = rays.pop()

		# if we already had this ray with particular direction we skip it
		# this avoids loops in the grid
		if current_ray in visited:
			continue

		# adds to visited
		visited.add(current_ray)

		# will analyse what tile the ray is in and add new rays with new directions depending on the tile
		check_tile(current_ray, grid, rays)

	# makes new set and loops through our visited tiles and only saves their coordinates
	# this way we get rid of duplicate coordinates but with different directions
	# the length of this set is equal to tiles energised
	tiles_visited = set()
	for tile in visited:
		tiles_visited.add((tile[0], tile[1]))
	return len(tiles_visited)



def main():
	with open("input") as file:
		lines = file.read().split("\n")


	# creating grid dictionary with coordinates as keys and tile type as value
	grid = dict()
	for i, line in enumerate(lines):
		for j, c in enumerate(line):
			grid[(j, i)] = c

	# gets solution for part1 with initial ray in topleft corner heading east
	part1 = get_energised_tiles_for_ray((0, 0, "E"), grid)

	# gets solution for part2 by looping through all possible entry points
	# first in the y axis from right and left
	# then from the x axis from top and bottom
	part2 = 0
	for y in range(len(lines)):
		new_part2 = get_energised_tiles_for_ray((0, y, "E"), grid)
		if new_part2 > part2:
			part2 = new_part2
		new_part2 = get_energised_tiles_for_ray((len(lines[0]) - 1, y, "W"), grid)
		if new_part2 > part2:
			part2 = new_part2

	for x in range(len(lines[0])):
		new_part2 = get_energised_tiles_for_ray((x, 0, "S"), grid)
		if new_part2 > part2:
			part2 = new_part2
		new_part2 = get_energised_tiles_for_ray((x, len(lines) - 1, "N"), grid)
		if new_part2 > part2:
			part2 = new_part2


	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()