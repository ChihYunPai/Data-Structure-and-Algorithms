"""
Write a function to find the longest common prefix string amongst an array of strings.

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        string = ""
        if len(strs) == 0: return string
        minLength = min([len(s) for s in strs])
        for i in range(minLength):
            if all([s[i] == strs[0][i] for s in strs]):
                string += strs[0][i]
            else:
                break
        return string