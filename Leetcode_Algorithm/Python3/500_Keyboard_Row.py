"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def isAllInStr(word, string):
            for i in word:
                if i not in string:
                    return False
            return True
        
        strList = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        wordsList = []
        for i in range(0, len(words)):
            for j in range(0, len(strList)):
                if isAllInStr(words[i].lower(), strList[j]):
                    wordsList.append(words[i])
                    break
        return wordsList
      