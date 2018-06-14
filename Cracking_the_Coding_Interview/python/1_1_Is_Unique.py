"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

import unittest
"""
With other Data Structres
Time: O(n)
Space: O(n)
n: length of string
"""
from collections import Counter

def isUnique(string):
    if not string:
        return True
    count = Counter(string)
    for char in count.values():
        if char > 1:
            return False
    return True


"""
Without other Data Structres
Time: O(n)
Space: O(n)
n: length of string
"""
def isUnique(string):
    if not string :
        return True
    count = set()
    for char in string:
        if char in count:
            return False
        count.add(char)
    return True

class Test(unittest.TestCase):
    true_data = ['abcdefghijklmnopqrstuvwxyz', '1b2n3m4,6l7!@#$%^&*(', '']
    false_data = ['11234', ';alskdfj qpwoeiur ', '  ']

    def test_unique(self):
        for test_string in self.true_data:
            self.assertTrue(isUnique(test_string))
        for test_string in self.false_data:
            self.assertFalse(isUnique(test_string))

if __name__ == "__main__":
    unittest.main()