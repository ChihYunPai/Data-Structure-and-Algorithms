"""
Implementation of AVL Tree
to be continue
"""

class Node(object):
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.height = 1

class AVLTree(object):
	def __init__(self):
		self.root = None

	def _insert(self, key, node):
		if not node:
			return
		elif key < node.key:
			node.left = self._insert(key, node.left)
		elif key > node.key:
			node.right = self._insert(key, node.right)
		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		balance = self.getBalance(node)
		# LL
		if balance > 1 and key < node.left.key:
			return self.rightRotate(node)
		# RR
		if balance < -1 and key > node.right.key:
			return self.leftRotate(node)
		# LR
		if balance > 1 and key > node.left.key:
			node.left = self.leftRotate(node.left)
			return self.rightRotate(node)
		if balance < -1 and key < node.right.key:
			node.right = self.rightRotate(node.right)
			return self.leftRotate(node)
		return node

	def insert(self, key):
		if not self.root:
			self.root = Node(key)
		else:
			self.root = self._insert(key, self.root)

	def leftRotate(self, z):
		y = z.right
		T2 = y .left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):
		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.hegiht = 1 + max(self.getHeights(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeights(y.left), self.getHeight(y.right))

		# Return the new root
		return y

	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	def getBalance(self, root):
		if not root:
			return 0
		return self.getHeight(root.left) - self.getHeight(root.right)

	def _preorder(self, root):
		if root:
			print(root.key, end=" ")
			self._preorder(root.left)
			self._preorder(root.right)

	def preorder(self):
		self._preorder(self.root)

def test():
	tree = AVLTree()
	tree.insert(10)
	tree.insert(20)
	tree.insert(30)
	tree.insert(40)
	tree.insert(50)
	tree.insert(25)

	tree.preorder()

if __name__ == '__main__':
	test()
