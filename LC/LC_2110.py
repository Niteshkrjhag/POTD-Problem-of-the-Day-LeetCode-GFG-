"""

1️⃣ Thought Process

🔍 Understanding the problem

We are given a list of daily stock prices.
A smooth descent period is defined as:
	•	One or more contiguous days
	•	Each next day’s price is exactly 1 less than the previous day
	•	A single day is always valid

📌 Key observations
	1.	Every individual day counts as one smooth descent period
→ Minimum answer is len(prices)
	2.	A longer smooth descent period exists only when consecutive prices decrease by exactly 1

prices[i] == prices[i-1] - 1


	3.	Whenever this condition breaks, the current descent streak ends.
	4.	If a descent streak has length k + 1 (k transitions),
the number of additional smooth descent subarrays formed is:

k * (k + 1) / 2



🧠 Why this formula works

For a continuous descent like:

5, 4, 3, 2

Extra smooth descent periods (excluding single days):

[5,4], [4,3], [3,2], [5,4,3], [4,3,2], [5,4,3,2]

Count = 3 + 2 + 1 = 6 = 3 * 4 / 2

⚠️ Edge cases
	•	Array of length 1 → answer is 1
	•	No valid descent anywhere → answer = number of elements
	•	Large input → must be O(n)

⸻

2️⃣ High-Level Pseudocode

Initialize total_periods = length of prices
Initialize descent_length = 0

For i from 1 to n-1:
    If prices[i] == prices[i-1] - 1:
        Increase descent_length
    Else:
        Add (descent_length * (descent_length + 1)) / 2 to total_periods
        Reset descent_length to 0

After loop:
    Add remaining descent streak contribution

Return total_periods


⸻

⏱ Complexity Analysis
	•	Time Complexity: O(n) — single pass through the array
	•	Space Complexity: O(1) — only constant extra variables

⸻
"""

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Every single day is a valid smooth descent period
        total_periods = len(prices)
        
        # Tracks length of current descent streak (number of valid transitions)
        descent_length = 0
        
        for i in range(1, len(prices)):
            # Check if current price forms a smooth descent with previous day
            if prices[i] == prices[i - 1] - 1:
                descent_length += 1
            else:
                # Add contribution of previous descent streak
                total_periods += (descent_length * (descent_length + 1)) // 2
                descent_length = 0
        
        # Add contribution from the last descent streak
        total_periods += (descent_length * (descent_length + 1)) // 2
        
        return total_periods