"""
LeetCode #7: Reverse Integer
Difficulty: Medium

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-2^31, 2^31 - 1], then return 0.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

INT_MAX = 2**31 - 1   # 2147483647
INT_MIN = -(2**31)    # -2147483648


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + digit

        reversed_num *= sign

        # Handle 32-bit overflow
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num


# Simpler Pythonic alternative (also acceptable in interviews)
class SolutionPythonic:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1]) * sign
        return result if INT_MIN <= result <= INT_MAX else 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))        # 321
    print(sol.reverse(-123))       # -321
    print(sol.reverse(120))        # 21
    print(sol.reverse(1534236469)) # 0 (overflow)