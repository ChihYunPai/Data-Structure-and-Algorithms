"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        uniqueList = [x for x in counter if counter[x]==1]
        # if all frequency greater than 1: return -1
        if len(uniqueList)==0:
            return -1
        for i in range(len(s)):
            if s[i] in uniqueList:
                return i