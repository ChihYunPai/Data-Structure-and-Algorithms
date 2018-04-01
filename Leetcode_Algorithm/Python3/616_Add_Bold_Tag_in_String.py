"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str, length in range[1, 1000], s contains 'a'-'z' and '0'-'9'
        :type dict: List[str], dict length <= 100
        :rtype: str
        """
        """
        Time: O(S * sigma(w_i) i = 0 ~ len(dict)-1)
        Space: O(S)
        """
        # step0: input validation
        # assert(0 < len(s) <= 1000 and 0 < len(dict) <= 100)
        # assert(isinstance(s, str))

        # step1: initialization
        table = [False] * len(s)
        
        for string in dict:
            length = len(string)
            for i in range(0, len(s) - length + 1):
                j = i + length - 1
                if string == s[i:j+1]:
                    table[i:j+1] = [True]*length
        string = ""
        prev = False
        for i, char in enumerate(s):
            curr = table[i]
            if (prev, curr) == (False, True):
                string += "<b>" + char
            elif (prev, curr) == (True, False):
                string += "</b>" + char
            else: # (prev, curr) == (False, False) or (True, True)
                string += char
            prev = curr
        if table[-1] == True and string[-4] != "</b>":
            string += "</b>"
            
        return string 
