/**
 * LeetCode #121: Best Time to Buy and Sell Stock
 * Difficulty: Easy
 * Topic: Array, Dynamic Programming
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    const currentPrice = prices[i];
    if (currentPrice < minPrice) {
      minPrice = currentPrice;
    } else if (currentPrice - minPrice > maxProfit) {
      maxProfit = currentPrice - minPrice;
    }
  }

  return maxProfit;
};

if (require.main === module) {
  const tests = [
    { prices: [7, 1, 5, 3, 6, 4], expected: 5 },
    { prices: [7, 6, 4, 3, 1], expected: 0 },
    { prices: [2, 4, 1], expected: 2 },
  ];

  console.log("=== LeetCode #121: Best Time to Buy and Sell Stock (JS) ===");
  tests.forEach(({ prices, expected }) => {
    const result = maxProfit(prices);
    console.log(`Prices: [${prices.join(", ")}] -> Profit: ${result} (Expected: ${expected})`);
  });
}

module.exports = maxProfit;
