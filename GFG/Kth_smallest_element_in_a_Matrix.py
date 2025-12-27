import bisect

class Solution:

    def count_less_equal(self, matrix, value):
        # ---------------------------------------------------
        # This function counts how many elements in the matrix
        # are less than or equal to a given value.
        #
        # Each row of the matrix is already sorted.
        # We use binary search (bisect_right) on each row.
        # ---------------------------------------------------
        count = 0
        total_rows = len(matrix)

        for row_index in range(total_rows):
            # bisect_right returns how many elements
            # in this row are <= value
            count += bisect.bisect_right(matrix[row_index], value)

        return count

    def kthSmallest(self, matrix, k):
        # ---------------------------------------------------
        # We apply binary search on the VALUE range,
        # not on the index positions.
        # ---------------------------------------------------

        total_rows = len(matrix)
        total_cols = len(matrix[0])

        # Smallest possible value in the matrix
        left_value = matrix[0][0]

        # Largest possible value in the matrix
        right_value = matrix[total_rows - 1][total_cols - 1]

        answer = None

        # ---------------------------------------------------
        # Binary search over value range
        # ---------------------------------------------------
        while left_value <= right_value:
            mid_value = (left_value + right_value) // 2

            # Count how many elements are <= mid_value
            count = self.count_less_equal(matrix, mid_value)

            # If count is enough, mid_value could be the answer
            if count >= k:
                answer = mid_value
                right_value = mid_value - 1
            else:
                # Otherwise, we need larger values
                left_value = mid_value + 1

        # ---------------------------------------------------
        # 'answer' will hold the k-th smallest value
        # ---------------------------------------------------
        return answer


'''

🧠 Logic Used (Simple Explanation)
	•	The matrix is sorted row-wise and column-wise
	•	Instead of searching positions, we search the answer value
	•	For any guessed value mid:
	•	We count how many numbers in the matrix are ≤ mid
	•	If that count is:
	•	≥ k → the k-th smallest number is ≤ mid
	•	< k → the k-th smallest number is larger than mid
	•	This allows us to apply binary search on values

⸻

🪜 Step-by-Step Approach
	1.	Set search range:
	•	left = smallest element in matrix
	•	right = largest element in matrix
	2.	Pick a middle value mid
	3.	Count how many elements in the matrix are ≤ mid
	4.	If count ≥ k:
	•	Move left to find a smaller possible answer
	5.	Else:
	•	Move right
	6.	Continue until search finishes
	7.	Return the stored answer

⸻

🧾 High-Level Pseudocode

FUNCTION kthSmallest(matrix, k):

    left = smallest element in matrix
    right = largest element in matrix
    answer = null

    WHILE left <= right:
        mid = (left + right) // 2
        count = count_elements_less_equal(matrix, mid)

        IF count >= k:
            answer = mid
            right = mid - 1
        ELSE:
            left = mid + 1

    RETURN answer

FUNCTION count_elements_less_equal(matrix, value):
    count = 0
    FOR each row in matrix:
        count += number of elements <= value (binary search)
    RETURN count


⸻

⏱ Time & Space Complexity
	•	Time Complexity:
	•	Binary search on values → O(log(max - min))
	•	Counting using binary search per row → O(n log n)
	•	Overall: O(n log n log(max - min))
	•	Space Complexity:
	•	O(1) (no extra data structures)

⸻

🎯 Interview-Ready One-Liner

I perform binary search on the value range and count elements less than or equal to mid using binary search on each row to find the k-th smallest element.

⸻
'''
