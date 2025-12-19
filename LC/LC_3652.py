'''
Given Example

values   = [10, 5, 0, 2, 3, 5]
strategy = [-1, 0, 1, -1, 1, -1]
k = 2

We are allowed to modify one contiguous block of length k = 2.

Since the array length is N = 6, the number of possible modifications is:

N - k + 1 = 5

That is why we get 5 possible strategies.

⸻

Why These 5 Strategies Exist

Each strategy corresponds to choosing where the block of length k starts.

For every starting position:
	•	Only 2 positions change
	•	Everything else remains the same

So the strategies are:

1. [ 0,  1,  1, -1,  1, -1]  ← window at index 0
2. [-1,  0,  1, -1,  1, -1]  ← window at index 1
3. [-1,  0,  0,  1,  1, -1]  ← window at index 2
4. [-1,  0,  1,  0,  1, -1]  ← window at index 3
5. [-1,  0,  1, -1,  0,  1]  ← window at index 4

Notice:
	•	Only the window of size k is modified
	•	Outside the window, the strategy is unchanged

⸻

Why We Don’t Actually Build These Strategies

Building each full strategy and recomputing profit would repeat the same work many times.

Instead, we observe:

Every strategy differs from the original in only one small window.

So the total profit can be computed as:

new profit =
    original total profit
  - original profit of the window
  + new profit of the window


⸻

How Prefix Sums Help Here

We precompute two things once:
	1.	Original profit prefix
	•	Lets us know how much profit the original strategy gives in any window
	2.	Sell-only prefix
	•	Lets us know how much profit a window gives if strategy = 1

Now, for each of the 5 windows:
	•	Remove the original window profit
	•	Add the modified window profit
	•	Everything else stays untouched

This lets us evaluate each strategy in constant time.

⸻

Core Idea (In One Sentence)

We don’t loop over strategies themselves — we loop over where the strategy changes, and use prefix sums to update the profit efficiently.

In short:

Intuitive Explanation of the Approach (Short & Clear)

We are given a base strategy and allowed to modify one contiguous block of length k.
For an array of length N, there are exactly N − k + 1 possible positions where this block can start, which gives us N − k + 1 possible strategies.

Instead of explicitly constructing each strategy array, we observe an important fact:

Every modified strategy is identical to the original one except inside the chosen window.

So the total profit of any strategy can be written as:

(total profit of original strategy)
− (profit contributed by the original window)
+ (profit contributed by the modified window)

To compute this efficiently:
	•	We precompute the profit of the original strategy using a prefix sum.
	•	We precompute the profit if we sell every day (strategy = 1) using another prefix sum.

Now, for each possible window:
	•	We remove the original profit from that window.
	•	We add the forced profit from the modified part (only the portion where strategy becomes 1).
	•	Everything outside the window remains unchanged.

This allows us to evaluate each possible strategy in O(1) time, and since there are N − k + 1 windows, the entire solution runs in O(N) time.

⸻

Key Insight (One Line)

We don’t iterate over strategies themselves — we iterate over where the strategy changes, and compute the effect of that change using prefix sums.

'''





class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        # prefixOriginalProfit[i] = profit from day 0 to day i-1
        # using the original strategy
        prefixOriginalProfit = [0]

        # prefixSellProfit[i] = sum of prices from day 0 to day i-1
        # (used when we force strategy = 1, i.e., sell)
        prefixSellProfit = [0]

        # Build prefix sums
        for price, action in zip(prices, strategy):
            prefixOriginalProfit.append(
                prefixOriginalProfit[-1] + price * action
            )
            prefixSellProfit.append(
                prefixSellProfit[-1] + price
            )

        n = len(strategy)

        # Total profit without any modification
        totalProfit = prefixOriginalProfit[-1]

        # Since modification is optional, start with original profit
        maxProfit = totalProfit

        # Try applying the modification on every valid window of size k
        for start in range(n):

            # Ensure window [start, start + k) is inside bounds
            if start + k <= n:

                # Profit contributed by this window in original strategy
                originalWindowProfit = (
                    prefixOriginalProfit[start + k]
                    - prefixOriginalProfit[start]
                )

                # Profit after modification:
                # - first k//2 days -> hold (0 profit)
                # - last  k//2 days -> sell (sum of prices)
                modifiedWindowProfit = (
                    prefixSellProfit[start + k]
                    - prefixSellProfit[start + k // 2]
                )

                # Total profit after replacing this window
                candidateProfit = (
                    totalProfit
                    - originalWindowProfit
                    + modifiedWindowProfit
                )

                # Update answer
                maxProfit = max(maxProfit, candidateProfit)

        return maxProfit