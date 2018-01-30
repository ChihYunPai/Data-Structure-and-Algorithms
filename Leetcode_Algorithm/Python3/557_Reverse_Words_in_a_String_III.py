"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

"""
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #split s into a string list
        strList = s.split(" ")
        #for each element in list, reverse character and assign to the current position in the list
        for i in range(0, len(strList)):
            strList[i] = strList[i][::-1]
        #merge string list into a string
        return " ".join(strList)