"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""
class Solution:
    """
    intput: str, str
    output: int
    """
    INT32_MAX = (2**31 - 1)
    INT32_MIN = (-2**31)

    def check_digit_status(self, char):
        if char is " ":
            return 'white_space'
        if char.isdigit():
            return 'digit'
        if char in ['-', '+']:
            return 'sign'
        return 'character'
    
    def myAtoi(self, input_str):
        """
        extract input string
        """
        extracted_string = ""
        start = False
        
        for char in input_str:
            digit_status = self.check_digit_status(char)
            
            if not start:
                if digit_status is 'character':
                    extracted_string = "0"
                    break
                if digit_status is 'white_space':
                    continue
                if digit_status in ['sign', 'digit']:
                    if char is not '+':
                        extracted_string = char
                    start = True
                    continue
            else:
                if digit_status is not 'digit':
                    break
                extracted_string += char
        
        """
        convert the extracted string into digits
        """
        if extracted_string in ["", "+", "-"]:
            return 0
        
        int_number = int(extracted_string)
        if self.INT32_MIN <= int_number <= self.INT32_MAX:
            return int_number
        return self.INT32_MAX if int_number > 0 else self.INT32_MIN