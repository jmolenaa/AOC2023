class map_range:
	def __init__(self, source_start, source_end, dest_start, dest_end):
		self.source_start = int(source_start)
		self.source_end = int(source_end)
		self.dest_start = int(dest_start)
		self.dest_end = int(dest_end)

class item_range:
	def __init__(self, range_start, range_end):
		self.range_start = int(range_start)
		self.range_end = int(range_end)


def add_range_to_map():
	ranges = list(map(int, line.split()))
	current_map.append(map_range(ranges[1], ranges[1] + ranges[2], ranges[0], ranges[0] + ranges[2]))


def convert_items():


	# part 1
	# converting our current items to the next category based on our list of map ranges
	for i, item in enumerate(itemspart1):
		for map in current_map:
			if item >= map.source_start and item < map.source_end:
				itemspart1[i] = map.dest_start - map.source_start + item
				break


	# part 2
	# converting our current item ranges to the next category based on our list of map ranges
	# based on four cases
	# 1 -	the item range is contained within the map range, conversion happens for the whole range
	# 2 -	the item range start is within the map range, but the end isn't, we create a new range 
	# 		from map range end to the item range end and convert the rest
	# 3 -	the item range starts outside map range, but ends withing, we create a new range from
	# 		item range begin to map range begin and convert the rest
	# 4 -	the item range starts before the map range and ends after the map range, we create 2 new ranges
	# 		item range begin to map range begin and map range end to item range end, then we convert the rest
	for i, item in enumerate(itemspart2):
		for map in current_map:

			if item.range_start >= map.source_start and item.range_start < map.source_end:

				# case 1
				if item.range_end < map.source_end:
					itemspart2[i].range_start = map.dest_start - map.source_start + item.range_start
					itemspart2[i].range_end = map.dest_start - map.source_start + item.range_end
					break

				# case 2
				else:
					itemspart2.insert(i + 1, item_range(map.source_end, itemspart2[i].range_end))
					itemspart2[i].range_start = map.dest_start - map.source_start + item.range_start
					itemspart2[i].range_end = map.dest_end
					break

			# case 3
			elif item.range_end > map.source_start and item.range_end < map.source_end:
				itemspart2.insert(i + 1, item_range(item.range_start, map.source_start))
				itemspart2[i].range_start = map.dest_start
				itemspart2[i].range_end = map.dest_start - map.source_start + item.range_end
				break

			# case 4
			elif item.range_start < map.source_start and item.range_end > map.source_end:
				itemspart2.insert(i + 1, item_range(item.range_start, map.source_start))
				itemspart2.insert(i + 2, item_range(map.source_end, item.range_end))
				itemspart2[i].range_start = map.dest_start
				itemspart2[i].range_end = map.dest_end
				break




lines = open("input").readlines()
seeds = lines[0].split()
del(seeds[0])

itemspart1 = list(map(int, seeds))

itemspart2 = list()
current_map=list()


# converting seeds into ranges for our item list
for i, seed in enumerate(seeds[::2]):
	itemspart2.append(item_range(seed, seed + seeds[i + 1]))



for line in lines[2:]:

	# once we reach a newline we've parsed all the ranges of the current category map, so we convert itemspart2
	if line == "\n":
		convert_items()
		current_map.clear()

	elif line[0].isdigit():
		add_range_to_map()

# another conversion for last category map in input since input doesn't end with newline
convert_items()

resultpart2 = [item.range_start for item in itemspart2]

print("Answer to part1: ", min(itemspart1))
print("Answer to part2: ", min(resultpart2))
