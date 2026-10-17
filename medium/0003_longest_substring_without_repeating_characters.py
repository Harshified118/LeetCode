"""
LeetCode #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Topic: Sliding Window, Hash Map, String

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Complexity Analysis:
- Time Complexity: O(n) single sliding window traversal with hash map.
- Space Complexity: O(min(m, n)) where n is string length and m is alphabet charset size.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            # If char was seen and is within the current window, shift left boundary
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),     # "b"
        ("pwwkew", 3),    # "wke"
        ("", 0),
        (" ", 1),
        ("au", 2),
    ]

    print("=== LeetCode #3: Longest Substring Without Repeating Characters ===")
    for text, expected in test_cases:
        actual = sol.lengthOfLongestSubstring(text)
        print(f"'{text}' -> Length: {actual} (Expected: {expected})")
