"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

"""
from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.squares = []
        self.n = 0
        self.dic = defaultdict(list)
        
    def build(self, square):
        if len(square) == self.n:
            self.squares.append(square)
            return
        for j in range(len(square[0])-1, len(square)-1, -1):
            prefix = ''
            for i in range(0, len(square)):
                prefix += square[i][j]
            if prefix not in self.dic:
                return
        for word in self.dic[prefix]:
            self.build(square + [word])
        
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words: return []
        if not words[0]: return []
        self.n = len(words[0])
        self.squares = []
        k = len(words[0])
        self.dic = defaultdict(list)
        for word in words:
            for i in range(1, k+1):
                self.dic[word[:i]].append(word)
        for word in words:
            self.build([word])
        return self.squares