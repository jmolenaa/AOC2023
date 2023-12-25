import networkx

def main():
	lines = [line.strip() for line in open("input").readlines()]


	list_of_edges = list()
	for line in lines:
		source_node, dest_nodes = line.split(":")
		dest_nodes = dest_nodes.strip().split(" ")
		for dest_node in dest_nodes:
			list_of_edges.append((source_node, dest_node))
	
	graph = networkx.Graph()
	graph.add_edges_from(list_of_edges, capacity=1)
	nodes = list(graph.nodes)


	print("takes like half a minute")
	for i, node1 in enumerate(nodes):
		for node2 in nodes[i + 1:]:
			minimum_cut, groups = networkx.minimum_cut(graph, node1, node2)
			if minimum_cut == 3:
				part1 = len(groups[0]) * len(groups[1])
				break



	print(f"The answer to part 1 is: {part1}")

if __name__ == "__main__":
	main()