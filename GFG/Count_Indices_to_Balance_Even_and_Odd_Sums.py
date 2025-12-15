"""
1️⃣ Thought Process (How to think about the problem)

Key observation

When you remove an element at index i:
	•	All elements before i keep their indices.
	•	All elements after i shift one position left, so:
	•	Even indices become odd
	•	Odd indices become even

So the parity of elements after the removed index flips.

⸻

Step-by-step idea
	1.	First, compute:
	•	even: sum of elements at even indices (original array)
	•	odd: sum of elements at odd indices (original array)
	2.	While iterating through the array, maintain:
	•	curr_even: sum of even-indexed elements before index i
	•	curr_odd: sum of odd-indexed elements before index i
	3.	For each index i, simulate removal:
	•	Remove arr[i] from even or odd
	•	Elements after i will swap parity:
	•	Remaining even sum becomes even - curr_even
	•	Remaining odd sum becomes odd - curr_odd
	4.	After removal:
	•	New even-index sum:

                            curr_even + (remaining odd)

	•	New odd-index sum:

                            curr_odd + (remaining even)


	5.	If both sums are equal → valid index.

⸻

2️⃣ High-Level Pseudocode

Compute total_even and total_odd sums

Initialize:
    curr_even = 0
    curr_odd = 0
    answer = 0

For each index i from 0 to n-1:
    Remove arr[i] from total_even or total_odd

    new_even_sum = curr_even + (total_odd - curr_odd)
    new_odd_sum  = curr_odd + (total_even - curr_even)

    If new_even_sum == new_odd_sum:
        answer += 1

    Add arr[i] to curr_even or curr_odd (based on index parity)

Return answer


⸻

3️⃣ Explanation of Your Code Logic

Your condition:

if temp_even + curr_odd - curr_even == temp_odd - curr_odd + curr_even:

This is mathematically equivalent to:

new_even_sum == new_odd_sum

Where:
	•	temp_even, temp_odd = sums after removing arr[i]
	•	curr_even, curr_odd = prefix sums before i
	•	Parity swap is handled using addition and subtraction

So your logic is correct and optimized.

⸻

4️⃣ Time and Space Complexity

⏱ Time Complexity
	•	One pass to compute initial sums → O(n)
	•	One pass to check each index → O(n)

✅ Overall Time Complexity: O(n)

⸻

💾 Space Complexity
	•	Uses only a few variables
	•	No extra arrays or data structures

✅ Overall Space Complexity: O(1)

⸻

5️⃣ Final Summary (Interview-ready)

I first calculate the total sums of elements at even and odd indices.
Then, for each index, I simulate removing that element and adjust the sums considering that indices after removal change parity.
If the resulting even and odd sums are equal, I count that index.
The solution runs in linear time with constant extra space.

"""

class Solution:
    def cntWays(self, arr):
        # Step 1: Calculate total sums at even and odd indices
        total_even_sum = 0
        total_odd_sum = 0

        for index, value in enumerate(arr):
            if index % 2 == 0:
                total_even_sum += value
            else:
                total_odd_sum += value

        # Step 2: Initialize prefix sums and answer counter
        prefix_even_sum = 0
        prefix_odd_sum = 0
        valid_indices_count = 0

        # Step 3: Check each index as a removal candidate
        for index, value in enumerate(arr):

            # Remove current element from total sums
            remaining_even_sum = total_even_sum
            remaining_odd_sum = total_odd_sum

            if index % 2 == 0:
                remaining_even_sum -= value
            else:
                remaining_odd_sum -= value

            # After removal, elements after index flip parity
            new_even_sum = prefix_even_sum + (remaining_odd_sum - prefix_odd_sum)
            new_odd_sum = prefix_odd_sum + (remaining_even_sum - prefix_even_sum)

            # Check if sums are equal
            if new_even_sum == new_odd_sum:
                valid_indices_count += 1

            # Update prefix sums for next iteration
            if index % 2 == 0:
                prefix_even_sum += value
            else:
                prefix_odd_sum += value

        return valid_indices_count