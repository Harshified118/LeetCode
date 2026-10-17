/**
 * test_solutions.js
 * Automated validation of all 8 LeetCode solutions in JavaScript.
 */

const assert = require("assert");

const isValid = require("./easy/0020_valid_parentheses");
const { ListNode, mergeTwoLists } = require("./easy/0021_merge_two_sorted_lists");
const maxProfit = require("./easy/0121_best_time_to_buy_sell_stock");
const isPalindrome = require("./easy/0125_valid_palindrome");

const { ListNode: ListNode2, addTwoNumbers } = require("./medium/0002_add_two_numbers");
const lengthOfLongestSubstring = require("./medium/0003_longest_substring_without_repeating_characters");
const threeSum = require("./medium/0015_3sum");
const groupAnagrams = require("./medium/0049_group_anagrams");

console.log("🧪 Running automated test suite for LeetCode JavaScript solutions...\n");

// Easy 1: Valid Parentheses
assert.strictEqual(isValid("()[]{}"), true);
assert.strictEqual(isValid("(]"), false);
console.log("✔ 0020_valid_parentheses passed");

// Easy 2: Merge Two Sorted Lists
const l1 = ListNode.fromArray([1, 2, 4]);
const l2 = ListNode.fromArray([1, 3, 4]);
assert.deepStrictEqual(mergeTwoLists(l1, l2).toArray(), [1, 1, 2, 3, 4, 4]);
console.log("✔ 0021_merge_two_sorted_lists passed");

// Easy 3: Best Time to Buy and Sell Stock
assert.strictEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5);
assert.strictEqual(maxProfit([7, 6, 4, 3, 1]), 0);
console.log("✔ 0121_best_time_to_buy_sell_stock passed");

// Easy 4: Valid Palindrome
assert.strictEqual(isPalindrome("A man, a plan, a canal: Panama"), true);
assert.strictEqual(isPalindrome("race a car"), false);
console.log("✔ 0125_valid_palindrome passed");

// Medium 1: Add Two Numbers
const m1 = ListNode2.fromArray([2, 4, 3]);
const m2 = ListNode2.fromArray([5, 6, 4]);
assert.deepStrictEqual(addTwoNumbers(m1, m2).toArray(), [7, 0, 8]);
console.log("✔ 0002_add_two_numbers passed");

// Medium 2: Longest Substring Without Repeating Characters
assert.strictEqual(lengthOfLongestSubstring("abcabcbb"), 3);
assert.strictEqual(lengthOfLongestSubstring("bbbbb"), 1);
console.log("✔ 0003_longest_substring_without_repeating_characters passed");

// Medium 3: 3Sum
const triplets = threeSum([-1, 0, 1, 2, -1, -4]);
const hasTriplet1 = triplets.some((t) => JSON.stringify(t) === JSON.stringify([-1, -1, 2]));
const hasTriplet2 = triplets.some((t) => JSON.stringify(t) === JSON.stringify([-1, 0, 1]));
assert.strictEqual(hasTriplet1 && hasTriplet2, true);
console.log("✔ 0015_3sum passed");

// Medium 4: Group Anagrams
const groups = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
const sortedGroups = groups.map((g) => g.sort()).sort();
assert.strictEqual(sortedGroups.length, 3);
console.log("✔ 0049_group_anagrams passed");

console.log("\n✨ ALL 8 LEETCODE JAVASCRIPT SOLUTIONS PASSED VERIFICATION!");
