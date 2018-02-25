"""
Implementation of RB-Tree:

1. colour: True for red, False for black
2. root always black
3. leaf: NIL always black
4. red node can only have black child / children, which implies no red nodes directly connected. Black node's children have no colour constraints.
5. for any path from a node to NIL leaf, the total number of black is the same.
6. length_longest_path <= 2 * length_shortest_path

"""

"""
search: O(log n)
insert: O(log n)
remove: O(log n)
space: O(n)
rotations: O(1)
"""
RED = True
BLACK = False
NIL = "NIL"

class node(object):
	def __init__(self, x, parent=None, colour=False, left=None, right=None):
		self.val = x
		self.colour = colour
		self.left = left
		self.right = right
		self.parent = 


class RBTree:
	def __init__(self):
		self.root = 
		self.NIL = 

	def __len__(self):

	def __str__(self):

	def __leftRotate(self):
		"""
		O(1)
		"""

	def __rightRotate(self):
		"""
		O(1)
		"""

	def search(self, x):
		"""
		O(log n)
		"""

	def insert(self, x):
		"""
		O(log n)
		1. insert x and color it red
		2. recolor and rotate nodes to fix violation

		Four scenarios:
			1. x == root
				- color it BLACK

			2. x.uncle == RED
				- recolor x's parent, grandparent and uncle

			3. x.uncle == BLACK (triangle)
				- rotate x.parent

			4. x.uncle == BLACK (line)
				- rotate x.grandparent
				- recolor parent and grandparent


		"""


	def remove(self, x):
		"""
		O(log n)
		"""