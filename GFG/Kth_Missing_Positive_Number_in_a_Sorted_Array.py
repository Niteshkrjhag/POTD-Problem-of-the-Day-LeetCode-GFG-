
class Solution:
    def kthMissing(self, arr, k):
        # ---------------------------------------------------
        # 'arr' is a sorted array of positive integers
        # We want to find the k-th missing positive number
        # ---------------------------------------------------

        # Binary search boundaries
        left = 0
        right = len(arr) - 1

        # ---------------------------------------------------
        # Binary search to find where the k-th missing number lies
        # ---------------------------------------------------
        while left <= right:
            mid = (left + right) // 2

            # Number of missing elements till index 'mid'
            # Expected value at index mid = mid + 1
            # Actual value = arr[mid]
            missing_count = arr[mid] - (mid + 1)

            # If missing numbers are less than k,
            # the k-th missing number is on the right side
            if missing_count < k:
                left = mid + 1
            else:
                # Otherwise, it lies on the left side
                right = mid - 1

        # ---------------------------------------------------
        # At the end of binary search:
        # 'left' represents how many numbers are present
        # before the k-th missing number
        #
        # So the answer is:
        # k + left
        # ---------------------------------------------------
        return left + k


'''

🧠 Logic Used (Simple Explanation)
	•	In a perfect sequence [1, 2, 3, 4, ...],
	•	the value at index i should be i + 1
	•	If the array contains larger numbers,
	•	some values are missing
	•	The number of missing values up to index i is:

arr[i] - (i + 1)


	•	We use binary search to efficiently find the position
where the k-th missing number should appear

⸻

🪜 Step-by-Step Approach
	1.	Use binary search on the array
	2.	At each middle index:
	•	Calculate how many numbers are missing so far
	3.	If missing numbers < k:
	•	Move right
	4.	Else:
	•	Move left
	5.	After binary search ends:
	•	The k-th missing number is k + left

⸻

🧾 High-Level Pseudocode

FUNCTION kthMissing(arr, k):

    left = 0
    right = length(arr) - 1

    WHILE left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - (mid + 1)

        IF missing < k:
            left = mid + 1
        ELSE:
            right = mid - 1

    RETURN left + k


⸻

⏱ Time & Space Complexity
	•	Time Complexity: O(log n)
	•	Space Complexity: O(1)

⸻

🎯 Interview-Ready One-Liner

I use binary search to count missing numbers at each index and locate the position where the k-th missing number belongs in logarithmic time.



'''
