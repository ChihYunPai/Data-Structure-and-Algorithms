"""
Implementation of Splay Tree
to be continued
"""
from bstree import BSTree
from random import shuffle
import time

class SplayTree(BSTree):
	def right_rotate(self, node, parent, gp=None):
		parent.left = node.right
		node.right = parent
		if not gp:
			pass
		elif gp.left == parent:
			gp.left = node
		elif gp.right == parent:
			gp.right = node
		else:
			raise ValueError('something wrong here.')

	def left_rotate(self, node, parent, gp=None):
		parent.right = node.left
		node.left = parent
		if not gp:
			pass
		elif gp.left == parent:
			gp.left = node
		elif gp.right == parent:
			gp.right = node
		else:
			raise ValueError('something wrong here.')

	def find(self, key, node=None, parent=None, gp=None, gg=None):
		if node == None:
			node = self.root
		if node == None:
			return None
		elif key < node.key:
			if not node.left:
				left = self.find(key, node.left, node, p, gp)
				if not left:
					return left
		elif key > node.key:
			if not node.right:
				right = self.find(key, node.left, node, p, gp)
				if not right:
					return right
		elif key == node.key:
			if parent != None:
				if gp == None: # Zig:
					if node == parent.left: # L
						self.right_rotate(node, parent)
					else: # R
						self.left_rotate(node, parent)
				# Zig-Zig
				elif p == gp.left and node == p.left: # LL
					self.right_rotate(node, p, gp)
					self.right_rotate(node, gp, gg)
				elif p == gp.right and node == p.right: # RR
					self.left_rotate(node, p, gp)
					self.left_rotate(node, gp, gg)
				# Zig-Zag
				elif p == gp.right and node == p.left: # RL
					self.right_rotate(node, p, gp)
					self.left_rotate(node, gp, gg)
				elif p == gp.left and node == p.right: # LR
					self.left_rotate(node, p, gp)
					self.right_rotate(node, gp, gg)
			return node
		else:
			raise ValueError('something impossible happens.')
		return None


def test():
	...

if __name__ == '__main__':
	test_splay_tree()


