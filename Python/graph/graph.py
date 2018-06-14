"""
Python Implementation of Graph
"""
"""
to be continued: 
1. change graph to {Node_X : {(Node_Y: value, edge_weight), (Node_Z: value, edge_weight)...}, ... }
2. methods:
	get_edge_value
	set_edge_value
	find_all_paths
	find_shortest_paths
"""
from collections import defaultdict

class Node():
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value

	def __repr__(self):
		return str(self.key) + ": " + str(self.value)

	def __str__(self):
		return str(self.value)

	def __eq__(self, other):
		if isinstance(other, Node):
			return other.key == self.key and other.value == self.value
		elif isinstance(other, type(self.key)):
			return other == self.key
		else:
			raise ValueError('something wrong here.')

	def __hash__(self):
		return hash(self.value)

	def set_value(self, x):
		assert(type(x) == type(self.value))
		self.value = x

	def get_value(self):
		return self.value


class Graph():
	def __init__(self, graph={}):
		self.graph = defaultdict(set)
		for key, value in graph.items():
			self.graph[key] = set(value)

	def __str__(self):
		string = ""
		for key, value in self.graph.items():
			string += str(key) + ": " + str(value) + "  "
		return string

	def has_node(self, node):
		"""
		return True if the graph has node, else return False
		"""
		return node in self.graph.keys()

	def find_path(self, start, end, path=[]):
		"""
		return path from start to end if found one, else return None
		"""
		path = path + [start]
		if start == end:
			return path
		if start not in self.graph.keys():
			return None
		for node in self.graph[start]:
			if node not in path:
				newpath = self.find_path(node, end, path)
				if newpath: return newpath
		return None

	def find_all_paths(self, start, end, path=[]):
		"""
		return all possible paths from start to end if exist, else return None
		"""
		pass

	def find_shortest_paths(self, start, end, path=[]):
		"""
		return the shortest path if has path from start to end, else return None
		"""
		pass

	def adjacent(self, x, y):
		"""
		return True if there is an edge from the vertices x to y, else return False
		"""
		if x in self.graph.keys():
			if y in self.graph[x]:
				return True
		return False

	def neighbors(self, x):
		"""
		return all vertices y such that there is an edge from the vertices x to y
		"""
		return self.graph[x]

	def add_vertex(self, x): 
		"""
		adds the vertex x, if it is not there
		return True if added, else False
		"""
		if x not in self.graph.keys():
			self.graph[x] = set()
			return True
		return False

	def remove_vertex(self, x):
		"""
		removes the vertex x if it is there
		"""
		if x in self.graph.keys():
			self.graph.pop(x, None)
			for key, value in self.graph.items():
				if x in value:
					value.remove(x)

	def add_edge(self, x, y):
		"""
		adds the edge from the vertices x to y, if it is not there
		return True if added, else if y is not there return False
		"""
		if x not in self.graph.keys():
			raise ValueError('{} is not in graph'.format(x))

		if y not in self.graph[x]:
			self.graph[x].add(y)
			if y not in self.graph.keys():
				self.graph[y] = set()
			return True
		return False

	def remove_edge(self, x, y):
		"""
		adds the edge from the vertices x to y, if it is not there
		return True if removed, else if y is not there return False
		"""
		if x not in self.graph.keys():
			raise ValueError('{} is not in graph'.format(x))

		if y in self.graph[x]:
			self.graph[x].remove(y)
			return True
		return False

	def get_vertex_value(self, x):
		"""
		returns the value associated with the vertex x
		"""
		for node in self.graph.keys():
			if x == node:
				return node.get_value()
		return None

	def set_vertex_value(graph, x, v):
		"""
		set the value associated with the vertex x
		"""
		for node in self.graph.keys():
			if x == node:
				node.set_value(v)
			return True
		return False

	def get_edge_value(graph, x, y):
		"""
		returns the value associated with the edge (x, y)
		"""
		pass

	def set_edge_value(graph, x, y, v):
		"""
		sets the value associated with the edge (x, y) to v
		"""
		pass


# test for class Graph and Node
if __name__ == "__main__":
	n1 = Node('A')
	n2 = Node('B')
	print(n1==n2)
	print(type(n1)==type(n2))


	data = {Node('A'): [Node('B'), Node('C')],
	        Node('B'): [Node('C'), Node('D')],
	             Node('C'): [Node('D')],
	             Node('D'): [Node('C')],
	             Node('E'): [Node('F')],
	             Node('F'): [Node('C')]}


	graph = Graph(data)
	print(graph)
	print(graph.has_node(Node('A')))
	print(graph.has_node('G'))
	print(graph.adjacent(Node('D'), Node('C')))
	print(graph.adjacent('D', 'G'))
	print(graph.neighbors('A'))
	graph.add_vertex(Node('G'))
	print(graph)
	graph.remove_vertex(Node('B'))
	print(graph)
	print(graph.add_edge(Node('A'), Node('B')))
	print(graph)
	print(graph.remove_edge('A', 'B'))
	print(graph)

	print(graph.find_path(Node('A'), Node('D')))

	print(graph.get_vertex_value('A'))
