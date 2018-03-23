"""
Python Implementation of n-ary tree
"""
from queue import Queue
from queue import LifoQueue as Stack

class Node():
	def __init__(self, key=None, N=2):
		self.key = key
		# children can be initialized into N None's or []
		self.children = [None]*N

class Tree():
	def __init__(self, N=2):
		self.root = None
		self.N = N

	def insert(self, key):
		if not self.root:
			self.root = Node(key, self.N)
		else:
			queue = Queue()
			queue.put(self.root)
			while not queue.empty():
				node = queue.get()
				for i, child in enumerate(node.children):
					if not child:
						node.children[i] = Node(key, self.N)
						return
					else:
						queue.put(child)

	def search(self, key, opt='bfs'):
		if opt == 'bfs':
			return self.bfs(key)
		elif opt == 'dfs':
			return self.dfs(key)
		else:
			raise ValueError("opt should be 'bfs' or 'dfs'.")

	def display(self, opt='bfs'):
		if opt == 'bfs':
			self._display_bfs()
		elif opt == 'dfs':
			self._display_dfs()

	def _display_bfs(self):
		if not self.root:
			return None
		container = Queue()
		container.put(self.root)
		while not container.empty():
			node = container.get()
			for i, child in enumerate(node.children):
				if child == None:
					continue
				if any(child.children):
					container.put(child)
				print(i, ":", child.key, end=", ")
			print('\n')

	def _display_dfs(self):
		if not self.root:
			return None
		container = Stack()
		container.put(self.root)
		while not container.empty():
			node = container.get()
			for i, child in enumerate(node.children):
				if child == None:
					continue
				if any(child.children):
					container.put(child)
				print(i, ":", child.key, end=", ")
			print('\n')

	def isIn(self, key):
		if not self.root:
			return False
		result = self.search(key)
		return True if result else False

	def dfs(self, key):
		"""
		return node if found
		return None if not found
		"""
		if not self.root:
			return None
		stack = Stack()
		stack.put(self.root)
		while not stack.empty():
			node = stack.get()
			if key == node.key:
				return node
			for child in node.children[::-1]:
				stack.put(child)
		return None

	def bfs(self, key):
		"""
		return node if found
		return None if not found
		"""
		if not self.root:
			return None 
		queue = Queue()
		queue.put(self.root)
		while not queue.empty():
			node = queue.get()
			if key == node.key:
				return node
			for child in node.children:
				queue.put(child)
		return None

	def _maxDepth(self, node):
		if not node:
			return 0
		maxDepth = 0
		for child in node.children:
			if child != None:
				maxDepth = max(maxDepth, self._maxDepth(child))
		return maxDepth + 1

	def maxDepth(self):
		"""
		return max depth of the tree
		"""
		if not self.root:
			return 0
		return self._maxDepth(self.root)

def test():
	tree = Tree(10)
	for key in range(100):
		tree.insert(key)
	print('========BFS========')
	tree.display()
	print('========DFS========')
	tree.display('dfs')
	print('========max depth========')
	print(tree.maxDepth())

if __name__ == '__main__':
	test()