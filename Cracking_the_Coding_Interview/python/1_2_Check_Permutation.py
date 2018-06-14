"""
Given two strings, write a method to decide if one is a permutation of the other
"""
import unittest
from collections import Counter

"""
Time: O(n)
Space: O(n)
""" 
def checkPermutation(string1, string2):
    assert(isinstance(string1, str) and isinstance(string2, str))
    if not string1 and not string2: 
        return True
    if len(string1) != len(string2):
        return False
    count1 = Counter(string1)
    count2 = Counter(string2)
    for key1, value1 in count1.items():
        if key1 not in count2 or value1 != count2[key1]:
            return False
    return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = checkPermutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = checkPermutation(*test_strings)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
