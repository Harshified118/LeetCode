/**
 * LeetCode #21: Merge Two Sorted Lists
 * Difficulty: Easy
 * Topic: Linked List
 *
 * Time Complexity: O(n + m)
 * Space Complexity: O(1)
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
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  const dummy = new ListNode(-1);
  let tail = dummy;

  let p1 = list1;
  let p2 = list2;

  while (p1 && p2) {
    if (p1.val <= p2.val) {
      tail.next = p1;
      p1 = p1.next;
    } else {
      tail.next = p2;
      p2 = p2.next;
    }
    tail = tail.next;
  }

  tail.next = p1 !== null ? p1 : p2;

  return dummy.next;
};

if (require.main === module) {
  const l1 = ListNode.fromArray([1, 2, 4]);
  const l2 = ListNode.fromArray([1, 3, 4]);
  const merged = mergeTwoLists(l1, l2);
  console.log("=== LeetCode #21: Merge Two Sorted Lists (JS) ===");
  console.log("Merged:", merged ? merged.toArray() : []);
}

module.exports = { ListNode, mergeTwoLists };
