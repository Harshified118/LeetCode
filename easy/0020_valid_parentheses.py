"""
LeetCode #20: Valid Parentheses
Difficulty: Easy
Topic: Stack, String

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Complexity Analysis:
- Time Complexity: O(n) where n is the length of s (each character is pushed and popped at most once).
- Space Complexity: O(n) in the worst case (e.g. "(((((" where all characters are pushed to stack).
"""

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                # Pop the top element if stack is non-empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # Open bracket, push onto stack
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("[", False),
    ]

    print("=== LeetCode #20: Valid Parentheses ===")
    for text, expected in test_cases:
        actual = sol.isValid(text)
        status = "PASS" if actual == expected else "FAIL"
        print(f"Input: {text!r:<10} | Expected: {expected!s:<5} | Got: {actual!s:<5} [{status}]")
