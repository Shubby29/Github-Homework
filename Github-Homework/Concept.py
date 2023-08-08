# Write a function that takes in an input and checks to see if it’s an
# isogram. The function should return True or False.
# An isogram is a word where no letter is repeated.
# Examples include:
# ● "isogram"
# ● "uncopyrightable"
# ● “ambidextrously”

def solve(word):
    for w in word:
        if not w.isalpha():
            return False
        if len(set(w)) != len(w):
            return False
    return True


words = ["isogram", "uncopyrightable", "ambidextrously"]
print(solve(words))

2.2 
import unittest
from main import solve

class SolveTestCase(unittest.TestCase):
    def test_isograms(self):
        words = ["isogram", "uncopyrightable", "ambidextrously"]
        self.assertTrue(solve(words))

    def test_non_isogram(self):
        words = ["Shubby", "assessment", "Task"]
        self.assertFalse(solve(words))

    def test_invalid_word(self):
        words = ["isogram", "789", "ambidextrously"]
        self.assertFalse(solve(words))

if __name__ == '__main__':
    unittest.main()


