"""
test_solutions.py
Automated validation of all 8 LeetCode solutions in Python.
"""

import unittest
import importlib
import sys
import os

# Add repo root to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

p20 = importlib.import_module("easy.0020_valid_parentheses").Solution()
p21 = importlib.import_module("easy.0021_merge_two_sorted_lists")
p121 = importlib.import_module("easy.0121_best_time_to_buy_sell_stock").Solution()
p125 = importlib.import_module("easy.0125_valid_palindrome").Solution()

p2 = importlib.import_module("medium.0002_add_two_numbers")
p3 = importlib.import_module("medium.0003_longest_substring_without_repeating_characters").Solution()
p15 = importlib.import_module("medium.0015_3sum").Solution()
p49 = importlib.import_module("medium.0049_group_anagrams").Solution()


class TestLeetCodeSolutions(unittest.TestCase):

    def test_0020_valid_parentheses(self):
        self.assertTrue(p20.isValid("()[]{}"))
        self.assertFalse(p20.isValid("(]"))

    def test_0021_merge_two_sorted_lists(self):
        l1 = p21.ListNode.from_list([1, 2, 4])
        l2 = p21.ListNode.from_list([1, 3, 4])
        merged = p21.Solution().mergeTwoLists(l1, l2)
        self.assertEqual(merged.to_list(), [1, 1, 2, 3, 4, 4])

    def test_0121_best_time_to_buy_sell_stock(self):
        self.assertEqual(p121.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(p121.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_0125_valid_palindrome(self):
        self.assertTrue(p125.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(p125.isPalindrome("race a car"))

    def test_0002_add_two_numbers(self):
        l1 = p2.ListNode.from_list([2, 4, 3])
        l2 = p2.ListNode.from_list([5, 6, 4])
        res = p2.Solution().addTwoNumbers(l1, l2)
        self.assertEqual(res.to_list(), [7, 0, 8])

    def test_0003_longest_substring(self):
        self.assertEqual(p3.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(p3.lengthOfLongestSubstring("bbbbb"), 1)

    def test_0015_3sum(self):
        triplets = p15.threeSum([-1, 0, 1, 2, -1, -4])
        self.assertIn([-1, -1, 2], triplets)
        self.assertIn([-1, 0, 1], triplets)

    def test_0049_group_anagrams(self):
        groups = p49.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        sorted_groups = sorted([sorted(g) for g in groups])
        expected = sorted([["ate", "eat", "tea"], ["nat", "tan"], ["bat"]])
        self.assertEqual(sorted_groups, expected)


if __name__ == "__main__":
    unittest.main()
