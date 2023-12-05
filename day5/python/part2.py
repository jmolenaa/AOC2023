class map:
	def __init__(self, s_ran, d_ran, ran):
		self.s_ran = s_ran
		self.d_ran = d_ran
		self.ran = ran

class thing:
	def __init__(self, beg, end):
		self.beg = beg
		self.end = end


def add_to_map():
	ranges = line.split()
	current_map.append(map(ranges[1], ranges[0], ranges[2]))

def convert_items():
	# change = 0
	for i, item in enumerate(items):
		for m in current_map:
			if int(item) - int(m.s_ran) < int(m.ran) and int(item) - int(m.s_ran) >= 0:
				# print(item, m.s_ran, m.d_ran, m.ran)
				# print("LOL")
				items[i] = int(m.d_ran) + int(item) - int(m.s_ran)
				# print(items[i])
				break

	# return items



lines = open("test_case").readlines()
seeds = lines[0]
seeds = seeds.split()
items = list()
del(seeds[0])
for i, seed in enumerate(seeds):
	print(i)
	if i % 2 == 0:
		items.append(thing(seed, int(seed) + int(seeds[i + 1])))
# for item in items:
# 	print(item.beg, item.end)
# print(items)
# print(len(items))

current_map=list()

for i, line in enumerate(lines):
	if i == 0 or i == 1:
		continue
	elif line == "\n":
		# print("current map")
		# print(items)
		# print(len(current_map))
		# for m in current_map:
		# 	print(m.s_ran, m.d_ran, m.ran)
		convert_items()
		current_map.clear()
	elif line[0].isdigit():
		add_to_map()
		# print("DIGIT" ,line)
	# print(line)
convert_items()

print(items)
print(min(items))