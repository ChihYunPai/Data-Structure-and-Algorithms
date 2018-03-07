"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table =     {1: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'], 
                     10: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C'],
                     100: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M'],
                     1000: ['', 'M', 'MM', 'MMM']
                    }
        return table[1000][num//1000] + table[100][num%1000//100] + table[10][num%100//10] + table[1][num%10]