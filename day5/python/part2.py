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


def add_to_map():
	ranges = line.split()
	current_map.append(map_range(ranges[1], int(ranges[1]) + int(ranges[2]), ranges[0], int(ranges[0]) + int(ranges[2])))

def convert_items():
	for i, item in enumerate(items):
		for map in current_map:

			if item.range_start >= map.source_start and item.range_start < map.source_end:
				if item.range_end < map.source_end:
					items[i].range_start = map.dest_start - map.source_start + item.range_start
					items[i].range_end = map.dest_start - map.source_start + item.range_end
					break
				else:
					items.insert(i + 1, item_range(map.source_end, items[i].range_end))
					items[i].range_start = map.dest_start - map.source_start + item.range_start
					items[i].range_end = map.dest_end
					break


			elif item.range_end > map.source_start and item.range_end < map.source_end:
				items.insert(i + 1, item_range(item.range_start, map.source_start))
				items[i].range_start = map.dest_start
				items[i].range_end = map.dest_start - map.source_start + item.range_end
				break


			elif item.range_start < map.source_start and item.range_end > map.source_end:
				items.insert(i + 1, item_range(item.range_start, map.source_start))
				items.insert(i + 2, item_range(map.source_end, item.range_end))
				items[i].range_start = map.dest_start
				items[i].range_end = map.dest_end
				break


lines = open("input").readlines()
seeds = lines[0].split()
del(seeds[0])

items = list()
current_map=list()

for i, seed in enumerate(seeds):
	if i % 2 == 0:
		items.append(item_range(seed, seed + seeds[i + 1]))


for i, line in enumerate(lines):
	if i == 0 or i == 1:
		continue
	elif line == "\n":
		convert_items()
		current_map.clear()
	elif line[0].isdigit():
		add_to_map()
convert_items()

result = list()
for item in items:
	result.append(item.range_start)
print(min(result))