from queue import PriorityQueue

def	make_heat_grid(lines):
	grid = dict()
	for i, line in enumerate(lines):
		for j, heat in enumerate(line):
			grid[(j, i)] = int(heat)

	return grid


def	add_new_neighbours_to_queue(dijkstra_points, current_point, heat_grid, minimum_steps, maximum_steps):

	# distribute into variables for readability
	accumulated_heat = current_point[0]
	coordinates = current_point[1]
	dx = current_point[2]
	dy = current_point[3]
	current_steps = current_point[4]
	
	# if we haven't reached the maximum steps one of the potential neighbours
	# is the next block in the same direction, as long as it's still in the grid
	# if both conditions are met we add it to the queue with the added heat from the new block
	if current_steps < maximum_steps and (coordinates[0] + dx, coordinates[1] + dy) in heat_grid:
		new_position = (coordinates[0] + dx, coordinates[1] + dy)
		dijkstra_points.put((accumulated_heat + heat_grid[new_position], new_position, dx, dy, current_steps + 1))
	
	# other potential neighbours are to the left and right
	# for part2 we can only turn if we have moved a minimum amount of steps
	if current_steps >= minimum_steps:

	# to turn a vector (dx, dy) by 90 degrees counterclockwise (left)
	# we multiply the x coordinate by -1 and then swap the x and y value
	# normally this is clockwise, but our grid has y increasing down not up
	# we then calculate our new position, check if it's in the grid
	# and add the neighbout to the queue with the added heat form the new block
		leftdx = dy
		leftdy = -dx
		left_pos = (coordinates[0] + leftdx, coordinates[1] + leftdy)
		if left_pos in heat_grid:
			dijkstra_points.put((accumulated_heat + heat_grid[left_pos], left_pos, leftdx, leftdy, 1))

	# for the right turn we do clockwise rotation which involves
	# multiplication of y by -1 and then swapping the x and y value
	# we then calculate our new position, check if it's in the grid
	# and add the neighbout to the queue with the added heat form the new block
		rightdx = -dy
		rightdy = dx
		right_pos = (coordinates[0] + rightdx, coordinates[1] + rightdy)
		if right_pos in heat_grid:
			dijkstra_points.put((accumulated_heat + heat_grid[right_pos], right_pos, rightdx, rightdy, 1))
		

def	dijkstra(heat_grid, end, minimum_steps, maximum_steps):

	# using priority queue for dijkstra algorithm, making sure we always check the current lowest accumulated heat
	dijkstra_points = PriorityQueue()

	# adding first two points to the queue, the one down form the start and right to the start
	# every point consists of the following information
	# accumulated heat - is just the heat on the first block we moved to for the beginning
	# coordinates of the block
	# dx - which direction we moved in on the x axis
	# dy - which direction we moved in on the y axis
	# current amount of steps
	dijkstra_points.put((heat_grid[(1, 0)], (1, 0), 1, 0, 1))
	dijkstra_points.put((heat_grid[(0, 1)], (0, 1), 0, 1, 1))

	# set of locations we've visited so far, will contain
	# coordinates of block, dx, dy, and steps
	# this is because we might visit the block from a different direction or with different steps left
	visited = set()

	while True:
		# gets point with current lowest accumulated heat form our queue and distributes it into variables
		current_point = dijkstra_points.get()
		accumulated_heat = current_point[0]
		coordinates = current_point[1]
		dx = current_point[2]
		dy = current_point[3]
		current_steps = current_point[4]

		# we've reached the end and so we return the heat we've accumulated
		# due to Dijkstras algorithm and the way the priority queue works this is the lowest heat path
		# we also make sure we've at least taken the minimum amount of steps
		if coordinates == end and current_steps >= minimum_steps:
			return accumulated_heat
		
		# check if we have already visited current block with this direction and steps
		if (coordinates, dx, dy, current_steps) in visited:
			continue

		# will add new neighbours to the priority queue
		add_new_neighbours_to_queue(dijkstra_points, current_point, heat_grid, minimum_steps, maximum_steps)

		# adds current block with direction and steps to the visited set
		visited.add((coordinates, dx, dy, current_steps))


def main():

	with open("input") as file:
		lines = file.read().split("\n")

	# making dictionary with coordinates as keys and heat on coordinate as value
	heat_grid = make_heat_grid(lines)

	# last block
	end = (len(lines[0]) - 1, len(lines) - 1)

	part1 = dijkstra(heat_grid, end, 1, 3)
	part2 = dijkstra(heat_grid, end, 4, 10)
	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")



if __name__ == "__main__":
	main()