'''

1️⃣ Key Insight of the Problem (MOST IMPORTANT)

We want:

strs[0] <= strs[1] <= strs[2] <= ... <= strs[n-1]

after deleting some columns.

Crucial observation:

Once two adjacent strings are already confirmed to be in correct lexicographic order,
we do NOT need to compare them further.

So we track which string pairs are already sorted and only worry about the unresolved ones.

⸻

2️⃣ Why Your Approach Fails

Your solution:
	•	Tries to manually track lex_start, lex_end
	•	Mixes row-based logic with column-based deletion
	•	Re-checks rows that are already sorted
	•	Has early returns that break valid cases

Core issue:

You are comparing full rows repeatedly, instead of tracking pairwise order resolution.

This problem is not about checking full lexicographic order at every step — it’s about locking order when possible and skipping unnecessary comparisons.

⸻

3️⃣ Correct Greedy Solution (Accepted Logic)

Idea (simple & powerful)
	•	Process columns left to right
	•	Maintain an array sorted_pairs[i] meaning:

strs[i] <= strs[i+1] is already confirmed


	•	For each column:
	•	If this column breaks lex order for any unresolved pair, delete the column
	•	Otherwise, update which pairs become sorted

⸻

🧠 Why This Works
	•	We only compare unresolved pairs
	•	Once strs[i] < strs[i+1] is confirmed, it stays confirmed forever
	•	Greedy deletion is optimal because:
	•	Earlier columns have higher lexicographic priority

⸻

⏱ Complexity
	•	Time: O(n * m)
	•	Space: O(n)

⸻

Example Walkthrough

strs = ["ca", "bb", "ac"]

	•	Column 0: c > b → delete
	•	Column 1: a < b < c → sorted

Answer = 1

⸻

🎯 Final Interview One-Liner

We process columns left to right and greedily delete a column if it violates lexicographic order for any unresolved adjacent pair, while tracking which string pairs are already sorted.



'''


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # sorted_pairs[i] = True if strs[i] <= strs[i+1] already confirmed
        sorted_pairs = [False] * (n - 1)

        deletions = 0

        for col in range(m):
            delete_column = False

            # Check if this column breaks lex order
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    delete_column = True
                    break

            if delete_column:
                deletions += 1
                continue

            # Update resolved pairs
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

        return deletions