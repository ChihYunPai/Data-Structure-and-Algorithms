"""
Implementation of Trie
"""
class Node():
    def __init__(self):
        self.children = {}
        self.isEnd = False
    """
    # IF ENCODING IS NECESSARY
    """
    # def _charToIndex(self, char):
    #     return ord(char) - ord('a')

    # def _indexToChar(self, index):
    #     return chr(index + ord('a'))

    def isFreeNode(self):
        return len(self.children) == 0

    def isLeafNode(self):
        return self.isEnd

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        node = self.root
        i = 0
        while i < len(string):
            if string[i] in node.children:
                node = node.children[string[i]]
                i += 1
            else: break

        while i < len(string):
            node.children[string[i]] = Node()
            node = node.children[string[i]]
            i += 1
        node.isEnd = True

    def search(self, string):
        """
        return True if found the string, else return False
        """
        node = self.root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node != None and node.isEnd

    def prefix(self, string):
        prefix = ""
        node = self.root
        for char in string:
            if char in node.children:
                prefix += char
                node = node.children[char]
            else:
                return prefix
        return prefix
    
    def _display(self, node, string=""):
        if node.isEnd:
            print(string)
        for child in sorted(node.children):
            self._display(node.children[child], string + child)

    def display(self):
        self._display(self.root)

    def _delete(self, node, key, level, length):
        if node:
            if level == length:
                return node.isFreeNode()
            else:
                char = key[level]
                if self._delete(node.children[char], key, level+1, length):
                    del node.children[char]
                    return node.isFreeNode()

    def delete(self, key):
        if len(key) > 0:
            self._delete(self.root, key, 0, len(key))

def test():
    trie = Trie()
    input = "a answer this that there is the my i am are an array about insert"
    testset = "this that there tree"
    for word in input.split():
        trie.insert(word)
    for word in testset.split():
        print(trie.search(word))

    trie.display()
    print('==================')
    print(trie.find('thi'))
    print('==================')
    trie.delete('answer')
    trie.display()

if __name__ == '__main__':
    test()