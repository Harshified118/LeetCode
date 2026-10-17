"""
LeetCode #2: Add Two Numbers
Difficulty: Medium
Topic: Linked List, Math

Problem Statement:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Complexity Analysis:
- Time Complexity: O(max(N, M)) where N and M are lengths of l1 and l2.
- Space Complexity: O(max(N, M)) to store the newly created result linked list.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: List[int]) -> Optional["ListNode"]:
        dummy = cls(0)
        curr = dummy
        for v in values:
            curr.next = cls(v)
            curr = curr.next
        return dummy.next

    def to_list(self) -> List[int]:
        res = []
        curr = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        p1, p2 = l1, l2
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if p1: p1 = p1.next
            if p2: p2 = p2.next

        return dummy_head.next


if __name__ == "__main__":
    sol = Solution()
    # (2 -> 4 -> 3) + (5 -> 6 -> 4) = 342 + 465 = 807 -> (7 -> 0 -> 8)
    l1 = ListNode.from_list([2, 4, 3])
    l2 = ListNode.from_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)

    print("=== LeetCode #2: Add Two Numbers ===")
    print("List 1 (reversed):", [2, 4, 3])
    print("List 2 (reversed):", [5, 6, 4])
    print("Sum List        :", result.to_list() if result else [])
