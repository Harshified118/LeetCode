"""
LeetCode #21: Merge Two Sorted Lists
Difficulty: Easy
Topic: Linked List, Recursion

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Complexity Analysis:
- Time Complexity: O(n + m) where n and m are lengths of list1 and list2.
- Space Complexity: O(1) iterative approach uses dummy head and pointers.
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy

        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        # Attach remaining nodes
        tail.next = p1 if p1 is not None else p2

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    l1 = ListNode.from_list([1, 2, 4])
    l2 = ListNode.from_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    print("=== LeetCode #21: Merge Two Sorted Lists ===")
    print("List 1:", [1, 2, 4])
    print("List 2:", [1, 3, 4])
    print("Merged:", merged.to_list() if merged else [])
