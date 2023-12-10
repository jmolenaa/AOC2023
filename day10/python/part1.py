def lookup_direction(val, dir1):
	if pipes[val][0] == dir1:
		return pipes[val][1]
	return pipes[val][0]

def find_start(lines):
	for i, line in enumerate(lines):
		if line.find("S") != -1:
			return ([i, line.find("S")])

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
	if prev_dir == "up":
		return "down"
	elif prev_dir == "down":
		return "up"
	elif prev_dir == "left":
		return "right"
	elif prev_dir == "right":
		return "left"

def main():
	lines = open("input").readlines()
	for i, line in enumerate(lines):
		lines[i] = line.strip()

	start_position = find_start(lines)
	global pipes
	pipes = {"|": ["up", "down"], "-": ["left", "right"], "F": ["down", "right"], \
		  	"J": ["up", "left"], "L": ["up", "right"], "7": ["left", "down"]}



	
	# print(lookup_dict("|", "up", pipes))
	# for key, value in pipes.items():
		# print(key, value)
		
	# huh = pipe("|", "up", "down")
	# print(huh.outgoing_dir("up"))

	# print(huh.dir1, huh.dir2, huh.val)

	# grid = [["."] * len(lines[0])] * len(lines)
	# for line in grid:
	# 	print(line)
	# print(grid)
	grid = list()
	for line in lines:
		grid.append(['.'] * len(line))
	# for line in grid:
	# 	print(line)
	# grid[0][0] = 'X'
	# for line in grid:
	# 	print(line)
		# grid.append(list(line))
	# print(grid)
	# print(list(lines[0]))
	start_pipe = identify_pipe_type(start_position, lines, pipes)
	current_pipe = start_pipe
	current_pos = start_position
	previous_dir = pipes[start_pipe][0]
	print(current_pos, current_pipe, previous_dir)
	steps = 0
	area = 0
	while True:
		# if steps == 10:
		# 	break


		grid[current_pos[0]][current_pos[1]] = current_pipe
		previous_pos = current_pos
		current_pos = change_pos(current_pos, current_pipe, previous_dir)
		previous_dir = lookup_direction(current_pipe, previous_dir)
		previous_dir = opposite(previous_dir)
		current_pipe = lines[current_pos[0]][current_pos[1]]
		# print(current_pos, current_pipe, previous_dir)
		# print("NEXT")
		steps += 1

		area += current_pos[1] * previous_pos[0] - current_pos[0] * previous_pos[1] 

		if current_pos == start_position:
			break
		# print("lol")
		# break
	print(steps / 2)
	for i, line in enumerate(grid):
		grid[i] = ''.join(line)
	for line in grid:
		print(line)
	counter = 0
	for line in grid:
		inside = 0
		for char in line:
			if char != "." and pipes[char][0] == "up":
				inside = (inside + 1) % 2
			elif char == "." and inside == 1:
				counter += 1
	print(counter)
	# print(grid)
	# print(start_position)



	resultpart1 = 0
	resultpart2 = 0

if __name__ == "__main__":
	main()