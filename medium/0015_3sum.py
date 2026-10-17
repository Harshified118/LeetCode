"""
LeetCode #15: 3Sum
Difficulty: Medium
Topic: Array, Two Pointers, Sorting

Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Complexity Analysis:
- Time Complexity: O(n^2) where n is len(nums). Sorting takes O(n log n) and nested two-pointer loop takes O(n^2).
- Space Complexity: O(1) or O(n) depending on sorting implementation (excluding output list).
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)

        for i in range(n - 2):
            # If current element is > 0, remaining sum cannot be 0 since array is sorted
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return triplets


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]

    print("=== LeetCode #15: 3Sum ===")
    for nums, expected in test_cases:
        actual = sol.threeSum(list(nums))
        print(f"Nums: {nums} -> Triplets: {actual} (Expected: {expected})")
