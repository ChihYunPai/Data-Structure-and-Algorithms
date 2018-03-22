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
rotations: O(log n)
space: O(n)
"""
RED = True
BLACK = False
NIL = "NIL"

class node(object):
	def __init__(sefl, key):
		self.key = key
		self.color = RED
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):
		return str(self.key)

	def __repr__(self):
		return str(self.key)

class RBTree:
	def __init__(self, create_node=rbnode):
		self.nil = create_node(key=None)
		self.root = self.nil
		self.create_node = create_node

	def search(self, key, x=None):
		"""
		search the subtree of x, (or root if x is not given) 
		return self.nil if not found
		"""
		if x == None:
			x = self.root
		while x != self.nil and key != x.key:
			if key < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def min(self, x=None):
		if x == None:
			x = self.root
		while x.left != self.nil:
			x = x.left
		return x

	def max(self, x=None):
		if x == None:
			x = self.root
		while x.right != self.nil:
			x = x.right
		return x

	def _left_rotate(self, x):
		y = x.right
		x.right = y.left
		y.left.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	def _right_rotate(self, x):
		y = x.left
		x.left = y.right
		y.right.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x = x.parent.right:
			x.parent.right = y
		else: 
			x.parent.left = y
		y.right = x
		x.parent = y

	def insert_key(self, key):
		self.insert_node(self.create_node(key=key))

	def insert_node(self, z):
		"""
		insert z and color it red
		"""
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		z.left = self.nil
		z.right = self.nil
		z.color = RED
		self._insert_fixup(z)

	def _insert_fixup(self, z):
		"""
		recolor and rotate nodes to fix violation

		Four cases:
			1. z == root
				- color it BLACK

			2. z.uncle == RED
				- recolor z's parent, grandparent and uncle

			3. z.uncle == BLACK (triangle)
				- rotate z.parent

			4. z.uncle == BLACK (line)
				- rotate z.grandparent
				- recolor parent and grandparent
		"""
		while z.parent.color == RED:
			if z.parent == z.parent.parent.left: # left parent
				y = z.parent.parent.right # y = z's uncle
				if y.color == RED: # (case 2) z.uncle == RED
					# recolor z's parent, grandparent and uncle
					z.parent.color = BLACK
					z.parent.parent.color = RED
					y.color = BLACK
					z = z.parent.parent
				else:
					if z == z.parent.left: # (case 3) z.uncle == BLACK (triangle), rotate z.parent
						z = z.parent
						self._right_rotate(z)
					else: # (case 4) z.uncle == BLACK (line), rotate z.grandparent, recolor parent and grandparent
						z.parent.color = BLACK        
						z.parent.parent.color = RED
						self._left_rotate(z.parent.parent)
		self.root.color = BLACK

	def check_invariants(self):
		def is_rb_node(node):
			NO_GOOD = (0, False)
			# check has left and right or neither
			if (node.left and not node.right) or (node.right and not node.left):
				return NO_GOOD
			# check leaves are black
			if not node.left and not node.right and node.color:
				return NO_GOOD
			# if node is red, check children are black
			if node.color and node.left and node.right:
				if node.left.color or node.right.color:
					return NO_GOOD
			# descend tree adn check black counts are balanced
			if node.left and node.right:
				# check children's parents are correct
				if self.nil != node.left and node != node.left.parent:
					return NO_GOOD
				if self.nil != node.right and node != node.right.parent:
					return NO_GOOD
				# check children are ok
				left_counts, left_ok = is_rb_node(node.left)
				if not left_ok:
					return NO_GOOD
				right_counts, right_ok = is_rb_node(node.right)
				if not right_ok:
					return NO_GOOD

				# check children's counts are ok
				if left_counts != right_counts:
					return NO_GOOD
				return left_counts, True
			else:
				return 0, True

			num_black, is_ok = is_rb_node(self.root)
			return is_ok and not self.root.color




