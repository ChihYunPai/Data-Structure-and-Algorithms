"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].
"""
import collections
import itertools
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = collections.Counter(s)
        if len(counter.keys()) <= 1: return [s]
        middle = tuple(key for key, value in counter.items() if value % 2)
        half = ''.join(key*(value//2) for key, value in counter.items())
        return [''.join(left + middle + left[::-1]) for left in set(itertools.permutations(half))] if len(middle) < 2 else []