import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # ---------------------------------------------------
        # Step 0: Sort meetings by their original start time
        # ---------------------------------------------------
        meetings.sort()

        # ---------------------------------------------------
        # This heap stores available room numbers
        # Always gives the smallest room number first
        # ---------------------------------------------------
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        # ---------------------------------------------------
        # This heap stores rooms that are currently busy
        # Format: (end_time, room_number)
        # Always gives the room that finishes earliest
        # ---------------------------------------------------
        busy_rooms = []

        # ---------------------------------------------------
        # Count how many meetings each room has handled
        # ---------------------------------------------------
        meeting_count = [0] * n

        # ---------------------------------------------------
        # Process each meeting in order
        # ---------------------------------------------------
        for start_time, end_time in meetings:
            meeting_duration = end_time - start_time

            # ---------------------------------------------------
            # Free up rooms that have finished before this meeting starts
            # ---------------------------------------------------
            while busy_rooms and busy_rooms[0][0] <= start_time:
                finished_time, room_number = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_number)

            # ---------------------------------------------------
            # If at least one room is free
            # ---------------------------------------------------
            if free_rooms:
                room_number = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end_time, room_number))
            else:
                # ---------------------------------------------------
                # No room is free → delay the meeting
                # Use the room that becomes free earliest
                # ---------------------------------------------------
                earliest_end_time, room_number = heapq.heappop(busy_rooms)
                new_end_time = earliest_end_time + meeting_duration
                heapq.heappush(busy_rooms, (new_end_time, room_number))

            # ---------------------------------------------------
            # Count this meeting for the selected room
            # ---------------------------------------------------
            meeting_count[room_number] += 1

        # ---------------------------------------------------
        # Find the room with the maximum number of meetings
        # If tie, return the smallest room number
        # ---------------------------------------------------
        max_meetings = max(meeting_count)

        for room in range(n):
            if meeting_count[room] == max_meetings:
                return room

'''


🧠 Logic Used (Intuition)

This problem is about simulation with priorities.

We must:
	•	Always assign the lowest-numbered free room
	•	If no room is free, delay the meeting
	•	Delayed meetings:
	•	Keep the same duration
	•	Go to the room that frees earliest
	•	Track how many meetings each room handles

To do this efficiently:
	•	We use two priority queues (heaps)

⸻

🪜 Step-by-Step Approach

1️⃣ Sort meetings by start time

This ensures we process meetings in the correct order.

⸻

2️⃣ Maintain two heaps

🟢 Free Rooms Heap
	•	Min-heap of available room numbers
	•	Ensures lowest room number is chosen first

🔴 Busy Rooms Heap
	•	Min-heap of (end_time, room_number)
	•	Ensures we know which room finishes earliest

⸻

3️⃣ For each meeting
	•	Free all rooms that finished before the meeting starts
	•	If a room is free:
	•	Assign the meeting immediately
	•	If no room is free:
	•	Delay the meeting
	•	Assign it to the room that finishes earliest
	•	Increment the room’s meeting count

⸻

4️⃣ Final Answer
	•	Find the room with the maximum number of meetings
	•	If there is a tie → return the smallest room number

⸻

🧾 High-Level Pseudocode

FUNCTION mostBooked(n, meetings):

    sort meetings by start time

    free_rooms = min heap of room numbers [0..n-1]
    busy_rooms = empty min heap
    meeting_count = array of size n initialized to 0

    FOR each meeting (start, end):
        duration = end - start

        WHILE busy_rooms not empty AND earliest_end <= start:
            free that room

        IF free_rooms not empty:
            assign meeting to smallest room
        ELSE:
            delay meeting to earliest finishing room

        increment meeting_count for that room

    RETURN room with maximum meeting_count


⸻

⏱ Time & Space Complexity

⏱ Time Complexity
	•	Sorting meetings: O(m log m)
	•	Heap operations per meeting: O(log n)
	•	Overall: O(m log n)

🧠 Space Complexity
	•	Heaps + count array: O(n)

⸻

🎯 Interview-Ready One-Liner

I simulate meeting scheduling using two priority queues: one for available rooms and one for busy rooms, ensuring correct room assignment and efficient handling of delayed meetings.



# Dry Run Yourself

n = 3
meetings = [
    [1, 4],
    [2, 6],
    [3, 5],
    [4, 7],
    [6, 8]
]
'''
