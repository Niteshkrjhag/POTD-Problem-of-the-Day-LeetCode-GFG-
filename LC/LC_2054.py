
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time (then end time, then value)
        events.sort()

        # Memoization dictionary to store DP results
        # Key: (current_index, events_selected)
        # Value: maximum value achievable from this state
        memo = {}

        # Binary search to find the first event
        # whose start time is strictly greater than 'ending'
        def binarySearch(ending):
            left = 0
            right = len(events) - 1

            # IMPORTANT:
            # We initialize result as len(events)
            # This means: "no valid next event found"
            #
            # Why NOT result = -1?
            # Because later we call solve(result, ...)
            # solve(len(events), ...) is safe and returns 0 (base case)
            # solve(-1, ...) would cause invalid recursion and wrong indexing
            result = len(events)

            while left <= right:
                mid = (left + right) // 2

                # If the event at mid starts after current event ends,
                # it is a valid candidate
                if events[mid][0] > ending:
                    result = mid      # store this index
                    right = mid - 1   # try to find an earlier valid event
                else:
                    left = mid + 1    # move right to find a valid start time

            return result

        # Recursive DP function
        def solve(current_index, selected_count):
            # Base case:
            # - already selected 2 events
            # - or no more events left
            if selected_count == 2 or current_index >= len(events):
                return 0

            # Return cached result if already computed
            if (current_index, selected_count) in memo:
                return memo[(current_index, selected_count)]

            # Option 1: skip current event
            skip_value = solve(current_index + 1, selected_count)

            # Option 2: take current event
            # Find the next non-overlapping event using binary search
            next_index = binarySearch(events[current_index][1])
            take_value = events[current_index][2] + solve(next_index, selected_count + 1)

            # Store and return the best of skip or take
            memo[(current_index, selected_count)] = max(skip_value, take_value)
            return memo[(current_index, selected_count)]

        # Start recursion from index 0 with 0 events selected
        return solve(0, 0)


'''

🔑 Key explanation (your main doubt)

❓ Why result = len(events) and NOT -1?

Dry-run reasoning (simple):
	•	If no event starts after ending, then:
	•	binarySearch should return “no valid index”
	•	Returning len(events) means:

solve(len(events), ...)


	•	This immediately hits base case:

idx >= len(events) → return 0


	•	✅ Correct and safe

If you returned -1:
	•	solve(-1, ...) would:
	•	incorrectly access events
	•	break DP logic
	•	cause wrong answers or infinite recursion

👉 len(events) is a sentinel value meaning “no more events”


'''

