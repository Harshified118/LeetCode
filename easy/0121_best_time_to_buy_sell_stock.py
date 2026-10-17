"""
LeetCode #121: Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Array, Dynamic Programming

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Complexity Analysis:
- Time Complexity: O(n) single pass
- Space Complexity: O(1) constant auxiliary space
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
    ]

    print("=== LeetCode #121: Best Time to Buy and Sell Stock ===")
    for prices, expected in test_cases:
        actual = sol.maxProfit(prices)
        print(f"Prices: {prices} -> Max Profit: {actual} (Expected: {expected})")
