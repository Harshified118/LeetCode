/**
 * LeetCode #2: Add Two Numbers
 * Difficulty: Medium
 * Topic: Linked List, Math
 *
 * Time Complexity: O(max(N, M))
 * Space Complexity: O(max(N, M))
 */

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

ListNode.fromArray = function (arr) {
  const dummy = new ListNode(0);
  let curr = dummy;
  for (const v of arr) {
    curr.next = new ListNode(v);
    curr = curr.next;
  }
  return dummy.next;
};

ListNode.prototype.toArray = function () {
  const res = [];
  let curr = this;
  while (curr) {
    res.push(curr.val);
    curr = curr.next;
  }
  return res;
};

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  const dummyHead = new ListNode(0);
  let current = dummyHead;
  let carry = 0;

  let p1 = l1;
  let p2 = l2;

  while (p1 !== null || p2 !== null || carry !== 0) {
    const val1 = p1 !== null ? p1.val : 0;
    const val2 = p2 !== null ? p2.val : 0;

    const sum = val1 + val2 + carry;
    carry = Math.floor(sum / 10);
    current.next = new ListNode(sum % 10);
    current = current.next;

    if (p1 !== null) p1 = p1.next;
    if (p2 !== null) p2 = p2.next;
  }

  return dummyHead.next;
};

if (require.main === module) {
  const l1 = ListNode.fromArray([2, 4, 3]);
  const l2 = ListNode.fromArray([5, 6, 4]);
  const sum = addTwoNumbers(l1, l2);
  console.log("=== LeetCode #2: Add Two Numbers (JS) ===");
  console.log("Sum:", sum ? sum.toArray() : []); // [7, 0, 8]
}

module.exports = { ListNode, addTwoNumbers };
