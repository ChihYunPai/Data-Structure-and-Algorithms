"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""
from collections import defaultdict
class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # building dictionary
        dic = defaultdict(list)
        for i, word in enumerate(words):
            dic[word].append(i)
        
        # initialize for two cases
        if word1 != word2:
            lst1, lst2 = dic[word1], dic[word2]
            i, j, step, m, n, distance = 0, 0, 1, len(lst1), len(lst2), len(words)
        else: # word1 == word2
            lst1, lst2 = dic[word1], dic[word2]
            i, j, step, m, n, distance = 0, 1, 2, len(lst1), len(lst2), len(words)
        
        # go through dic and count
        while i < m and j < n:
            diff = lst1[i] - lst2[j]
            distance = min(distance, abs(diff))
            if diff > 0:
                j += step
            else: # diff < 0
                i += step
        return distance
                