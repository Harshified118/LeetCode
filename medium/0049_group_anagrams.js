/**
 * LeetCode #49: Group Anagrams
 * Difficulty: Medium
 * Topic: Array, Hash Table, String, Sorting
 *
 * Time Complexity: O(N * K log K)
 * Space Complexity: O(N * K)
 */

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const map = new Map();

  for (const s of strs) {
    const key = s.split("").sort().join("");
    if (!map.has(key)) {
      map.set(key, []);
    }
    map.get(key).push(s);
  }

  return Array.from(map.values());
};

if (require.main === module) {
  const tests = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [""],
    ["a"],
  ];

  console.log("=== LeetCode #49: Group Anagrams (JS) ===");
  tests.forEach((words) => {
    const res = groupAnagrams(words);
    console.log(`Words: [${words.join(", ")}] -> ${JSON.stringify(res)}`);
  });
}

module.exports = groupAnagrams;
