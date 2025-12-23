
class Solution:
    def countXInRange(self, arr, queries):

        # Map each distinct element to its continuous index range [start, end]
        value_to_range = {}

        start_index = 0
        previous_value = arr[0]

        # Build ranges for each value (array is assumed sorted)
        for index, value in enumerate(arr):

            # If value continues, do nothing
            if value == previous_value:
                continue

            # Close range for previous value
            end_index = index - 1
            value_to_range[previous_value] = [start_index, end_index]

            # Start new range
            start_index = index
            previous_value = value

        # Close range for last value
        value_to_range[previous_value] = [start_index, index]

        results = []

        # Process each query
        for left, right, target in queries:

            # If target exists in array
            if target in value_to_range:
                range_start, range_end = value_to_range[target]

                # Compute overlap of [left, right] with target range
                count = min(right, range_end) - max(left, range_start) + 1

                # If overlap is valid
                results.append(count if count > 0 else 0)
            else:
                results.append(0)

        return results


'''
2️⃣ What This Code Is Doing (Simple Explanation)
	•	Since arr is sorted, identical values appear in continuous blocks
	•	We store start and end index of each value
	•	For every query [l, r, x]:
	•	We find how much the query range overlaps with x’s stored range
	•	Overlap length gives the count

⸻

⏱ Complexity (Interview-Ready)
	•	Preprocessing: O(n)
	•	Each query: O(1)
	•	Total: O(n + q)
	•	Space: O(n)

'''


from collections import defaultdict
import bisect

class Solution:
    def countXInRange(self, arr, queries):

        value_indices = defaultdict(list)

        # Store indices of each value
        for i, val in enumerate(arr):
            value_indices[val].append(i)

        result = []

        for l, r, x in queries:
            if x not in value_indices:
                result.append(0)
                continue

            indices = value_indices[x]

            # Count indices within [l, r]
            left_pos = bisect.bisect_left(indices, l)
            right_pos = bisect.bisect_right(indices, r)

            result.append(right_pos - left_pos)

        return result


'''

4️⃣ Why This Alternative Is Often Preferred

✔ Works even if array is not strictly continuous
✔ Very easy to explain
✔ Uses standard tools (bisect)
✔ Commonly accepted by interviewers

⸻

🎯 Interview One-Liner Explanation

“Since the array is sorted, I preprocess indices of each value and use binary search to count how many lie inside the query range in logarithmic time.”

⸻

'''


