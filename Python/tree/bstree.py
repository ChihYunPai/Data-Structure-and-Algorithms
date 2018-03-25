"""
Implementation of Binary Search Tree
"""

class Node():
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        string = str(self.key)
        if self.left:
            string += ", left: " + str(self.left)
        if self.right:
            string += ", right: " + str(self.right)
        return string

class BSTree():
    def __init__(self):
        self.root = Node()
        self.length = 0

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __del__(self):
        del self.root

    def __len__(self):
        return self._count(self.root)

    def _count(self, node):
        if node == None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

    def count(self):
        node = self.root
        if node is None:
            return 0
        return self._count(node)

    def _search(self, key, node):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(key, node.left)
        # key > node.key
        return self.search(key, node.right)

    def search(self, key):
        if self.root == None:
            return None
        return self._search(key, self.root)
        
    def _insert(self, key, node):
        if key < node.key:
            if node.left == None:
                node.left = Node(key)
                return
            else:
                self._insert(key, node.left)
        else: # if key >= node.key
            if node.right == None:
                node.right = Node(key)
                return
            else:
                self._insert(key, node.right)

    def insert(self, key):
        if self.root.key == None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def find_min(self, node):
        currentNode = node
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def find_max(self, node):
        currentNode = node
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else: # found the node
            if node.left is None: # node only has right child
                temp = node.right
                node = None
                return temp
            elif node.right is None: # node only has left child
                temp = node.left
                node = None
                return temp
            # with two children
            temp = self.find_min(node.right)
            node.key = temp.key # copy value of the min_node in the right subtree to the node
            node.right = self._delete(node.right, temp.key)
        return node

    def delete(self, key):
        node = self.root
        if node is None:
            return node
        self.root = self._delete(self.root, key)

    def _preorder(self, node):
        if node:
            print(node.key)
            self._preorder(node.left)
            self._preorder(node.right)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key)
            self._inorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key)

    def traversal(self, opt='inorder'):
        if self.root == None:
            return None
        if opt == 'inorder':
            self._inorder(self.root)
        elif opt == 'preorder':
            self._preorder(self.root)
        elif opt == 'postorder':
            self._postorder(self.root)
        else:
            raise ValueError("opt: option should be 'inorder', 'preorder' or 'postorder'.")

    def _verify(self, node):
        if node == None:
            return True
        if node.left:
            if node.left >= node.key:
                return False
        if node.right:
            if node.right < node.key:
                return False
        return self._verify(node.left) and self._verify(node.right)
        
    def verifiy(self):
        if self.root == None:
            return True
        self._verify(self.root)


def test():
    # running test for BSTree methods

    tree = BSTree()
    lst = [8, 3, 10, 1, 6, 4, 7, 14, 13]
    for x in lst:
        tree.insert(x)
    print('inorder')
    tree.traversal()
    print('preorder')
    tree.traversal(opt='preorder')
    print('postorder')
    tree.traversal(opt='postorder')

    for x in lst[:]:
        print('=================')
        print('delete ', x)
        tree.delete(x)
        tree.traversal(opt='preorder')
        
if __name__ == '__main__':
    test()


        