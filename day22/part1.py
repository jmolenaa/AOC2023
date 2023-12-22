from collections import defaultdict

def	add_to_bricks_dict(bricks_dict, line, i):
	start, end = line.split("~")
	# start = tuple(start.split(","))
	# print(start, end)
	bricks_dict[i + 1] = (tuple(start.split(",")), tuple(end.split(",")))


def	add_to_coordinate_dict(coordinates_pair, coordinate_dict, block_id):

	x1, y1, z1 = coordinates_pair[0]
	x2, y2, z2 = coordinates_pair[1]
	for i in range(int(x1), int(x2)):
		# coordinate_dict[()]
		print(block_id)

	# print(coordinates_pair)

def main():
	with open("test_case") as file:
		lines = file.read().split("\n")

	bricks_dict = defaultdict(int)
	coordinate_dict = defaultdict(int)
	for i,line in enumerate(lines):
		add_to_bricks_dict(bricks_dict, line, i)
		add_to_coordinate_dict(bricks_dict[i + 1], coordinate_dict, i + 1)
		# print(line)
	for key,value in bricks_dict.items():
		print(key, value)
	part1 = 0
	part2 = 0

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()