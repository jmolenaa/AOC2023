from collections import defaultdict

def	add_to_bricks_dict(bricks_dict, line, i):
	start, end = line.split("~")
	bricks_dict[i + 1] = (tuple(start.split(",")), tuple(end.split(",")))


def	add_to_coordinate_dict(coordinates_pair, coordinate_dict, block_id):

	x1, y1, z1 = coordinates_pair[0]
	x2, y2, z2 = coordinates_pair[1]
	for x in range(int(x1), int(x2) + 1):
		for y in range(int(y1), int(y2) + 1):
			for z in range(int(z1), int(z2) + 1):
				coordinate_dict[(x, y, z)] = block_id

def	get_z(entry):
	return int(entry[1][0][2])


def	update_dicts(fallen, block_id, coordinate_dict, bricks_dict):
	if fallen == 0:
		return
	x1, y1, z1 = bricks_dict[block_id][0]
	x2, y2, z2 = bricks_dict[block_id][1]
	bricks_dict[block_id] = ((x1, y1, int(z1) - fallen), (x2, y2, int(z2) - fallen))
	copied_dict = dict(coordinate_dict)
	keys_to_remove = list()
	for key, value in copied_dict.items():
		if value == block_id and fallen != 0:
			coordinate_dict[(int(key[0]), int(key[1]), int(key[2]) - int(fallen))] = block_id
			del coordinate_dict[key]


def	drop_block(coordinates_pair, block_id, coordinate_dict, bricks_dict):
	x1, y1, z1 = coordinates_pair[0]
	x2, y2, z2 = coordinates_pair[1]
	lowest_z = 1

	for x in range(int(x1), int(x2) + 1):
		for y in range(int(y1), int(y2) + 1):
			for z in range(int(z1), 0, -1):
				if (x, y, z) in coordinate_dict and coordinate_dict[(x, y, z)] != block_id:
					if lowest_z <= z:
						lowest_z = z + 1
					break
	update_dicts(int(z1) - lowest_z, block_id, coordinate_dict, bricks_dict)


def	add_to_supporting_dict(coordinates_pair, key, coordinate_dict, supporting_dict):
	x1, y1, z1 = coordinates_pair[0]
	x2, y2, z2 = coordinates_pair[1]
	supporting_dict[key] = set()
	for x in range(int(x1), int(x2) + 1):
		for y in range(int(y1), int(y2) + 1):
			for z in range(int(z1), int(z2) + 1):
				if (x, y, int(z) - 1) in coordinate_dict and coordinate_dict[(x, y, int(z) - 1)] != key:
					supporting_dict[key].add(coordinate_dict[(x, y, int(z) - 1)])


def	add_to_supported_dict(coordinates_pair, key, coordinate_dict, supported_dict):
	x1, y1, z1 = coordinates_pair[0]
	x2, y2, z2 = coordinates_pair[1]
	supported_dict[key] = set()
	for x in range(int(x1), int(x2) + 1):
		for y in range(int(y1), int(y2) + 1):
			for z in range(int(z1), int(z2) + 1):
				if (x, y, int(z) + 1) in coordinate_dict and coordinate_dict[(x, y, int(z) + 1)] != key:
					supported_dict[key].add(coordinate_dict[(x, y, int(z) + 1)])


def	count_fallen_blocks(block_id, supported_dict, supporting_dict):
	falling_blocks = {block_id}
	blocks_to_check = [block_id]
	while blocks_to_check:
		current_block = blocks_to_check.pop()
		for block in supported_dict[current_block]:
			if supporting_dict[block].issubset(falling_blocks):
				falling_blocks.add(block)
				blocks_to_check.append(block)

	return len(falling_blocks) - 1


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	bricks_dict = defaultdict(int)
	coordinate_dict = defaultdict(int)
	for i,line in enumerate(lines):
		add_to_bricks_dict(bricks_dict, line, i)
		add_to_coordinate_dict(bricks_dict[i + 1], coordinate_dict, i + 1)
	bricks_dict = dict(sorted(bricks_dict.items(), key= get_z))
	

	for key, value in bricks_dict.items():
		drop_block(value, key, coordinate_dict, bricks_dict)


	supporting_dict = dict()
	for key, value in bricks_dict.items():
		add_to_supporting_dict(value, key, coordinate_dict, supporting_dict)


	supported_dict = dict()
	for key, value in bricks_dict.items():
		add_to_supported_dict(value, key, coordinate_dict, supported_dict)

	total_bricks = len(bricks_dict)


	block_we_cant_disintegrate = set()
	for key, value in supporting_dict.items():
		if len(value) == 1:
			block_we_cant_disintegrate.add(list(value)[0])

	part1 = total_bricks - len(block_we_cant_disintegrate)

	part2 = 0
	for key, value in supported_dict.items():
		part2 += count_fallen_blocks(key, supported_dict, supporting_dict)



	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()