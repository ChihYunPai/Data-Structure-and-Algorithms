"""
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
from collections import defaultdict
class WordDistance:
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = defaultdict(list)
        self.len = len(words)
        for i, word in enumerate(words):
            self.dic[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lst1, lst2 = self.dic[word1], self.dic[word2]
        i, j, m, n, distance = 0, 0, len(lst1), len(lst2), self.len
        while i < m and j < n:
            diff = lst1[i] - lst2[j]
            distance = min(distance, abs(diff))
            if diff > 0: # lst1[i] > lst2[j]
                j += 1
            else: # lst1[i] < lst2[j]
                i += 1
        return distance
        
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)