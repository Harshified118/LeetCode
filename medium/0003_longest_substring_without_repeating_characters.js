/**
 * LeetCode #3: Longest Substring Without Repeating Characters
 * Difficulty: Medium
 * Topic: Sliding Window, Hash Map, String
 *
 * Time Complexity: O(n)
 * Space Complexity: O(min(m, n))
 */

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  const map = new Map();
  let maxLength = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    if (map.has(char) && map.get(char) >= left) {
      left = map.get(char) + 1;
    }
    map.set(char, right);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
};

if (require.main === module) {
  const tests = [
    { s: "abcabcbb", expected: 3 },
    { s: "bbbbb", expected: 1 },
    { s: "pwwkew", expected: 3 },
    { s: "", expected: 0 },
  ];

  console.log("=== LeetCode #3: Longest Substring Without Repeating Characters (JS) ===");
  tests.forEach(({ s, expected }) => {
    const res = lengthOfLongestSubstring(s);
    console.log(`"${s}" -> ${res} (Expected: ${expected})`);
  });
}

module.exports = lengthOfLongestSubstring;
