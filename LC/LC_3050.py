
'''

🧠 Logic Used (Simple Explanation)
	•	We want to choose k people such that the total happiness is maximum
	•	Each time we pick someone:
	•	Their happiness reduces by the number of people already picked
	•	To always get the best result:
	•	We must always pick the person with the highest current happiness
	•	A max heap helps us get the largest happiness value efficiently

⸻

🪜 Step-by-Step Approach
	1.	Convert the happiness list into a max heap
	2.	Repeat k times:
	•	Pick the person with the highest happiness
	•	Reduce their happiness based on how many people were already chosen
	•	Add only positive happiness to the total
	3.	Return the total happiness

⸻

🧾 High-Level Pseudocode

FUNCTION maximumHappinessSum(happiness, k):

    CREATE max_heap from happiness values

    total_happiness = 0
    people_chosen = 0

    WHILE people_chosen < k:
        current = extract_max from heap
        remaining = current - people_chosen

        IF remaining > 0:
            total_happiness += remaining

        people_chosen += 1

    RETURN total_happiness


⸻

⏱ Time & Space Complexity
	•	Time Complexity:
	•	Heap creation: O(n)
	•	Each extraction: O(log n)
	•	Total: O(n + k log n)
	•	Space Complexity:
	•	Heap storage: O(n)

⸻

🎯 Interview-Ready One-Liner

I use a max heap to always select the person with the highest remaining happiness, adjusting the value after each selection to maximize the total sum.


'''




import heapq
from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # ---------------------------------------------------
        # We want to always pick the person with the
        # maximum remaining happiness.
        #
        # Python has a MIN heap, so to simulate a MAX heap,
        # we store negative values.
        # ---------------------------------------------------

        max_heap = [-value for value in happiness]

        # Convert the list into a heap
        heapq.heapify(max_heap)

        # This will store the total happiness we collect
        total_happiness = 0

        # This represents how many people have already been chosen
        people_chosen = 0

        # ---------------------------------------------------
        # Pick exactly k people
        # ---------------------------------------------------
        while people_chosen < k:
            # Get the person with maximum current happiness
            # (convert back from negative)
            current_happiness = -heapq.heappop(max_heap)

            # After choosing 'people_chosen' people,
            # each next person loses 'people_chosen' happiness
            remaining_happiness = current_happiness - people_chosen

            # Only add if remaining happiness is positive
            if remaining_happiness > 0:
                total_happiness += remaining_happiness

            # Move to next selection
            people_chosen += 1

        return total_happiness




'''

🧠 Logic Used (Simple Explanation)
	•	We want to choose k people to maximize total happiness
	•	Every time we choose a person:
	•	Their happiness decreases by the number of people already chosen
	•	To get the maximum total:
	•	We should always choose the person with the highest remaining happiness
	•	Sorting the array in descending order ensures:
	•	We always pick the best available person first

⸻

🪜 Step-by-Step Approach
	1.	Sort the happiness array in descending order
	2.	Iterate k times to select k people
	3.	For each selected person:
	•	Reduce their happiness by how many people are already selected
	4.	Stop early if happiness gain becomes zero or negative
	5.	Return the total happiness sum

⸻

🧾 High-Level Pseudocode

FUNCTION maximumHappinessSum(happiness, k):

    SORT happiness in descending order

    total = 0

    FOR i FROM 0 TO k - 1:
        gain = happiness[i] - i

        IF gain <= 0:
            RETURN total

        total = total + gain

    RETURN total


⸻

⏱ Time & Space Complexity
	•	Time Complexity: O(n log n)
	•	Sorting dominates the runtime
	•	Space Complexity: O(1) (in-place sorting)

⸻

🎯 Interview-Ready One-Liner

I sort the happiness values in descending order and greedily select the top k people, reducing happiness after each selection to maximize the total sum.

⸻

'''

from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # ---------------------------------------------------
        # Sort the happiness values in descending order
        # so that we always pick the happiest person first
        # ---------------------------------------------------
        happiness.sort(reverse=True)

        # This will store the final maximum happiness sum
        total_happiness = 0

        # ---------------------------------------------------
        # Select exactly k people
        # ---------------------------------------------------
        for selected_count in range(k):
            # Each time we select a person,
            # their happiness is reduced by the number
            # of people already selected
            current_gain = happiness[selected_count] - selected_count

            # If the gain becomes zero or negative,
            # selecting further people will not increase happiness
            if current_gain <= 0:
                return total_happiness

            # Add the positive happiness gain
            total_happiness += current_gain

        return total_happiness

