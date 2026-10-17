/**
 * LeetCode #20: Valid Parentheses
 * Difficulty: Easy
 * Topic: Stack, String
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const map = { ')': '(', '}': '{', ']': '[' };
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (char in map) {
      const top = stack.length > 0 ? stack.pop() : '#';
      if (top !== map[char]) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0;
};

// Test Runner
if (require.main === module) {
  const tests = [
    { input: "()", expected: true },
    { input: "()[]{}", expected: true },
    { input: "(]", expected: false },
    { input: "([)]", expected: false },
    { input: "{[]}", expected: true },
  ];

  console.log("=== LeetCode #20: Valid Parentheses (JS) ===");
  tests.forEach(({ input, expected }) => {
    const result = isValid(input);
    console.log(`Input: "${input}" | Expected: ${expected} | Got: ${result}`);
  });
}

module.exports = isValid;
