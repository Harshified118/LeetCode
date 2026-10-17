"""
LeetCode #49: Group Anagrams
Difficulty: Medium
Topic: Array, Hash Table, String, Sorting

Problem Statement:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Complexity Analysis:
- Time Complexity: O(N * K log K) using sorted tuple keys, where N is len(strs) and K is max string length.
- Space Complexity: O(N * K) to store the grouped anagram lists in hash map.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort characters to form canonical key
            key = "".join(sorted(s))
            anagram_map[key].append(s)

        return list(anagram_map.values())


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
    ]

    print("=== LeetCode #49: Group Anagrams ===")
    for words in test_cases:
        actual = sol.groupAnagrams(words)
        print(f"Words: {words} -> Groups: {actual}")
