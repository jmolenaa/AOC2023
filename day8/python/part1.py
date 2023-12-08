class Node:
	def __init__(self, val):
		self.l = None
		self.r = None
		self.v = val

	def add_to_node(val, dir):
		new_node = Node(val)
        

class Tree:
	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root

	def add(self, val):
		if not self.root:
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val < node.v:
			if node.l:
				self._add(val, node.l)
			else:
				node.l = Node(val)
		else:
			if node.r:
				self._add(val, node.r)
			else:
				node.r = Node(val)

	def find(self, val):
		if self.root:
			return self._find(val, self.root)

	def _find(self, val, node):
		if val == node.v:
			return node
		elif val < node.v and node.l:
			return self._find(val, node.l)
		elif val > node.v and node.r:
			return self._find(val, node.r)

	def view_tree(self):
		if self.root:
			self._view_tree(self.root)

	def _view_tree(self, node):
		if node:
			self._view_tree(node.l)
			print(node.v, end = " ")
			self._view_tree(node.r)

def make_nodes(lines):

	locations = dict()
    
	for line in lines[2:]:
		node_values = line.split()
		new_node = Node(node_values[0])
		new_node.l = node_values[2][1:4]
		new_node.r = node_values[3][:3]
		locations[node_values[0]] = new_node
		# locations.update({node_values[0], new_node})
		# locations.append([node_values[0], new_node])
	# print(locations)
	return locations

def main():
	lines = open("input").readlines()

	locations = make_nodes(lines)
	instructions = lines[0]
	current_location = locations["AAA"]
	steps = 0
	# print(current_location.v, current_location.l, current_location.r)
	print(instructions)
	while True:
		for char in instructions:
			if current_location.v == "ZZZ":
				break
			if char == "L":
				current_location = locations[current_location.l]
			elif char == "R":
				current_location = locations[current_location.r]
			else:
				break
			steps += 1
		if current_location.v == "ZZZ":
			break
	print(current_location.v)
	print(steps)

if __name__ == "__main__":
	main()