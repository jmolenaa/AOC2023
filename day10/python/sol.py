def lookup_direction(val, dir1):
	if pipes[val][0] == dir1:
		return pipes[val][1]
	return pipes[val][0]

def find_start(lines):
	for i, line in enumerate(lines):
		if "S" in line:
			return ([i, line.find("S")])

# we look around the start position and find the pipes that connect to the start
# we have extra checks so we don't go out of bounds
def identify_pipe_type(start_position, lines, pipes):
	dir = list()
	if start_position[0] > 0:
		if "|F7".find(lines[start_position[0] - 1][start_position[1]]) != -1:
			dir.append("up")
	if start_position[0] < len(lines):
		if "|JL".find(lines[start_position[0] + 1][start_position[1]]) != -1:
			dir.append("down")
	if start_position[1] > 0:
		if "-FL".find(lines[start_position[0]][start_position[1] - 1]) != -1:
			dir.append("left")
	if start_position[1] < len(lines[0]):
		if "-7J".find(lines[start_position[0]][start_position[1] + 1]) != -1:
			dir.append("right")
	for key, value in pipes.items():
		if set(value) == set(dir):
			return key

def change_pos(cur_pos, cur_pipe, prev_dir):
	new_direction = lookup_direction(cur_pipe, prev_dir)
	if new_direction == "right":
		return ([cur_pos[0], cur_pos[1] + 1])
	elif new_direction == "left":
		return ([cur_pos[0], cur_pos[1] - 1])
	elif new_direction == "up":
		return ([cur_pos[0] - 1, cur_pos[1]])
	elif new_direction == "down":
		return ([cur_pos[0] + 1, cur_pos[1]])

def opposite(prev_dir):
	directions = {"up": "down", "down": "up", "left": "right", "right": "left"}
	return directions[prev_dir]

def main():
	lines = [line.strip() for line in open("input").readlines()]

	# finds coordinates of start position
	start_position = find_start(lines)

	# dictionary of pipes with the directions they face as values
	global pipes
	pipes = {"|": ["up", "down"], "-": ["left", "right"], "F": ["down", "right"], \
		  	"J": ["up", "left"], "L": ["up", "right"], "7": ["left", "down"]}

	# make empty grid where we can put our map with just the loop pipes
	grid = [['.'] * len(line) for line in lines]

	# identifies the pipe we start with and sets up starting values for loop
	current_pipe = identify_pipe_type(start_position, lines, pipes)
	current_pos = start_position
	previous_dir = pipes[current_pipe][0]
	steps = 0


	while True:

		# making grid with only loop pipes
		grid[current_pos[0]][current_pos[1]] = current_pipe
		current_pos = change_pos(current_pos, current_pipe, previous_dir)

		# we look at the direction we left the pipe in and grav the opposite for the next loop
		previous_dir = opposite(lookup_direction(current_pipe, previous_dir))
		current_pipe = lines[current_pos[0]][current_pos[1]]
		steps += 1

		# if we reach start again we finished the pipe loop
		if current_pos == start_position:
			break


	# changes our lists inside grid ot strings for faster access
	for i, line in enumerate(grid):
		grid[i] = ''.join(line)
		
	# for line in grid:
	# 	print(line)


	# loop through the grid and find all inside points
	# if we encounter a pipe that goes up that means we are now inside the loop
	# if we encounter another one we are outside etc.
	# we only count points when we are inside
	inside_points = 0
	for line in grid:
		inside = 0
		for char in line:
			if char != "." and pipes[char][0] == "up":
				inside = (inside + 1) % 2
			elif char == "." and inside == 1:
				inside_points += 1


	print(f"The answer to part 1 is: {int(steps / 2)}")
	print(f"The answer ot part 2 is: {inside_points}")

if __name__ == "__main__":
	main()