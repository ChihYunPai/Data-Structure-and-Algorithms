class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value)

class Tree:
	def __init__(self):
		self.root = None

	def __str__(self):
		pass# self.printTree(     ) ???

	def root(self):
		return self.root

	def add(self, value, node=None):
		if node==None:
			if self.root==None:
				self.root = Node(value)
			else:
				self.add(value, self.root)

		else:
			if value < node.value:
				if node.left==None:
					node.left = Node(value)
				else:
					self.add(value, node.left)
			else:
				if node.right==None:
					node.right = Node(value)
				else:
					self.add(value, node.right)

	def find(self, value, node=None):
		if node==None:
			if self.root==None:
				return None
			else:
				return self.find(value, self.root)
		else:
			if value==node.value:
				return node
			elif value<node.value and node.left!=None:
				return self.find(value, node.left)
			elif value>node.value and node.right!=None:
				return self.find(value, node.right)
			

	def delete(self):
		self.root = None

	def print(self, node=None):
		if node==None:
			if self.root!=None:
				self.print(self.root)
			else:
				print("empty tree.")
		else:
			if node.left!=None:
				self.print(node.left)
			print(str(node.value) + ' ')
			if node.right!=None:
				self.print(node.right)
