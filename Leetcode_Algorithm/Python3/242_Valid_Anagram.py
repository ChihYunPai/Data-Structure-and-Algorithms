"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or bool(set(s)-set(t))!=0:
            return False
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        for x in counter1:
            if counter1[x]!=counter2[x]:
                return False
        return True