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
