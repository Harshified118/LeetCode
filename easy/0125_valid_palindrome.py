"""
LeetCode #125: Valid Palindrome
Difficulty: Easy
Topic: Two Pointers, String

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Complexity Analysis:
- Time Complexity: O(n) two-pointer scan
- Space Complexity: O(1) in-place pointer comparison without auxiliary string allocation
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
    ]

    print("=== LeetCode #125: Valid Palindrome ===")
    for text, expected in test_cases:
        actual = sol.isPalindrome(text)
        print(f"'{text}' -> {actual} (Expected: {expected})")
