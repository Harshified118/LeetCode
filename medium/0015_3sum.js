/**
 * LeetCode #15: 3Sum
 * Difficulty: Medium
 * Topic: Array, Two Pointers, Sorting
 *
 * Time Complexity: O(n^2)
 * Space Complexity: O(1) auxiliary (excluding output)
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const triplets = [];
  const n = nums.length;

  for (let i = 0; i < n - 2; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = n - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum < 0) {
        left++;
      } else if (sum > 0) {
        right--;
      } else {
        triplets.push([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;

        left++;
        right--;
      }
    }
  }

  return triplets;
};

if (require.main === module) {
  const tests = [
    [-1, 0, 1, 2, -1, -4],
    [0, 1, 1],
    [0, 0, 0],
  ];

  console.log("=== LeetCode #15: 3Sum (JS) ===");
  tests.forEach((nums) => {
    const res = threeSum([...nums]);
    console.log(`Nums: [${nums}] -> ${JSON.stringify(res)}`);
  });
}

module.exports = threeSum;
