/**
 * LeetCode #125: Valid Palindrome
 * Difficulty: Easy
 * Topic: Two Pointers, String
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

function isAlphanumeric(char) {
  const code = char.charCodeAt(0);
  return (
    (code >= 48 && code <= 57) || // 0-9
    (code >= 65 && code <= 90) || // A-Z
    (code >= 97 && code <= 122)   // a-z
  );
}

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    while (left < right && !isAlphanumeric(s[left])) {
      left++;
    }
    while (left < right && !isAlphanumeric(s[right])) {
      right--;
    }

    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false;
    }

    left++;
    right--;
  }

  return true;
};

if (require.main === module) {
  const tests = [
    { input: "A man, a plan, a canal: Panama", expected: true },
    { input: "race a car", expected: false },
    { input: " ", expected: true },
  ];

  console.log("=== LeetCode #125: Valid Palindrome (JS) ===");
  tests.forEach(({ input, expected }) => {
    const result = isPalindrome(input);
    console.log(`Input: "${input}" -> Result: ${result} (Expected: ${expected})`);
  });
}

module.exports = isPalindrome;
