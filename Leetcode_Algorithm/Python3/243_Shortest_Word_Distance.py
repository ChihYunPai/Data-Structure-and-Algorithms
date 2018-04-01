"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        Time: O(n)
        Space: O(1)
        """
        indices = {}
        distance = len(words)
        for i, word in enumerate(words):
            if word == word1:
                if word2 in dic:
                    distance = min(distance, i - dic[word2])
                dic[word1] = i
            elif word == word2:
                if word1 in dic:
                    distance = min(distance, i - dic[word1])
                dic[word2] = i
        return distance