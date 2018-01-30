"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ls = list(s)
        res = []
        for i in range(len(s)):
            if i%(2*k) == 0:
                if (len(s)-i+1) >= k:
                    res += ls[i:i+k][::-1]
                else:
                    res += ls[i:][::-1]
            elif i%(2*k)>=k:
                res.append(ls[i])
        return ''.join(res)
                    
            
            