


'''

🧠 Logic Used (Simple Explanation)
	•	A rotated sorted array always consists of two sorted parts
	•	The rotation index (pivot) separates these two parts
	•	We find the pivot by locating where the order breaks
	•	Then:
	•	If the array is not rotated → count directly
	•	If rotated → count in both sorted parts
	•	Add all elements that are less than or equal to x

⸻

🪜 Approach (Step-by-Step)
	1.	Detect rotation
	•	Look for the index where arr[i-1] > arr[i]
	2.	Check if array is rotated
	•	If no such index exists → array is sorted
	3.	Count elements ≤ x
	•	Either in whole array (not rotated)
	•	Or separately in left and right sorted parts
	4.	Return total count

⸻

🧾 High-Level Pseudocode

FUNCTION countLessEqual(arr, x):

    SET rotation_index = -1

    FOR i FROM 1 TO n-1:
        IF arr[i-1] > arr[i]:
            rotation_index = i
            BREAK

    count = 0

    IF rotation_index == -1:
        FOR each element in arr:
            IF element <= x:
                count++

    ELSE:
        FOR i FROM 0 TO rotation_index - 1:
            IF arr[i] <= x:
                count++

        FOR i FROM rotation_index TO n - 1:
            IF arr[i] <= x:
                count++

    RETURN count


⸻

⏱ Time & Space Complexity
	•	Time Complexity: O(n)
	•	Space Complexity: O(1)

⸻

🎯 Interview-Ready One-Liner

I first detect the rotation point in the array, then count elements less than or equal to x in each sorted part separately.

'''

class Solution:
    def countLessEqual(self, arr, x):
        # Total number of elements in the array
        n = len(arr)

        # This will store the index where rotation happened
        # If pivot remains -1, it means the array is NOT rotated
        rotation_index = -1

        # ---------------------------------------------------
        # STEP 1: Find the rotation index (pivot)
        # ---------------------------------------------------
        # In a rotated sorted array, there is exactly one place
        # where an element is greater than the next element.
        #
        # Example:
        # [6, 10, 12, 15, 2, 4, 5]
        #            ↑ rotation happens here
        #
        # We scan the array once to find that point.
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                rotation_index = i
                break

        # Variable to store the final count of elements <= x
        count = 0

        # ---------------------------------------------------
        # STEP 2: If array is NOT rotated
        # ---------------------------------------------------
        # If rotation_index is still -1,
        # the array is already sorted.
        if rotation_index == -1:
            for value in arr:
                if value <= x:
                    count += 1

        # ---------------------------------------------------
        # STEP 3: If array IS rotated
        # ---------------------------------------------------
        else:
            # Left sorted part: arr[0 ... rotation_index - 1]
            for i in range(0, rotation_index):
                if arr[i] <= x:
                    count += 1

            # Right sorted part: arr[rotation_index ... n - 1]
            for i in range(rotation_index, n):
                if arr[i] <= x:
                    count += 1

        # Return the total count of elements <= x
        return count



'''
🧠 Logic Used (Simple Explanation)
	•	A rotated sorted array always consists of two sorted subarrays
	•	The pivot is the index of the smallest element
	•	Once the pivot is known:
	•	Left side is sorted
	•	Right side is sorted
	•	In a sorted array, we can count elements ≤ x using binary search
	•	Add counts from both parts

⸻

🪜 Step-by-Step Approach
	1.	Find the pivot
	•	Use binary search to locate the smallest element
	2.	Split the array logically
	•	Left part → sorted
	•	Right part → sorted
	3.	Count elements ≤ x
	•	Use binary search on both sorted parts
	4.	Return the total count

⸻

🧾 High-Level Pseudocode

FUNCTION countLessEqual(arr, x):

    FIND pivot index using binary search

    DEFINE function count_in_sorted_range(start, end):
        USE binary search to find
        last index where arr[index] <= x
        RETURN count of such elements

    count_left  = count_in_sorted_range(0, pivot - 1)
    count_right = count_in_sorted_range(pivot, n - 1)

    RETURN count_left + count_right


⸻

⏱ Time & Space Complexity
	•	Time Complexity: O(log n)
	•	Pivot search → O(log n)
	•	Two binary searches → O(log n)
	•	Space Complexity: O(1)

⸻

🎯 Interview-Ready Summary

I first locate the pivot using binary search, then count elements less than or equal to x in both sorted halves using binary search, achieving logarithmic time complexity.

'''

class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)

        # ---------------------------------------------------
        # STEP 1: Find the pivot (index of smallest element)
        # ---------------------------------------------------
        # The pivot tells us where the array was rotated.
        # In a rotated sorted array, the smallest element
        # divides the array into two sorted parts.
        #
        # We use binary search to find the smallest element
        # in O(log n) time.

        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            # If middle element is greater than the last element,
            # then the smallest element must be on the right side
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                # Otherwise, the smallest element is on the left side
                # including mid
                right = mid

        # At the end, left points to the smallest element
        pivot_index = left

        # ---------------------------------------------------
        # STEP 2: Helper function to count elements <= x
        #         in a sorted subarray using binary search
        # ---------------------------------------------------
        def count_in_sorted_range(start, end):
            # This will store the index of the last element <= x
            last_valid_index = start - 1

            while start <= end:
                mid = (start + end) // 2

                if arr[mid] <= x:
                    last_valid_index = mid
                    start = mid + 1
                else:
                    end = mid - 1

            # Number of elements <= x is:
            # (last_valid_index + 1)
            return last_valid_index + 1

        # ---------------------------------------------------
        # STEP 3: Count elements <= x in both sorted parts
        # ---------------------------------------------------
        # Left part: arr[0 ... pivot_index - 1]
        # Right part: arr[pivot_index ... n - 1]

        count_left_part = count_in_sorted_range(0, pivot_index - 1)
        count_right_part = count_in_sorted_range(pivot_index, n - 1)

        # Total count is sum of both parts
        return count_left_part + count_right_part


