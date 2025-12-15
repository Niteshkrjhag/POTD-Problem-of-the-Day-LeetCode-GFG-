"""
Correct mental model:

The ONLY thing that matters:
	•	Seats must be grouped in pairs
	•	Between each pair of seat-pairs, count plants
	•	Each such gap contributes:
    (plant_count + 1) choices
    •	Multiply all such choices

    
High-level pseudocode:

count total seats
if total seats < 2 or odd:
    return 0

ways = 1
seat_count = 0
plant_count = 0

for each character in corridor:
    if character == 'S':
        seat_count += 1

        if seat_count == 3:
            ways = ways * (plant_count + 1)
            plant_count = 0
            seat_count = 1
    else:
        if seat_count == 2:
            plant_count += 1

return ways mod (10^9 + 7)


NOTE: 

-> Every time two seats are completed, the number of plants until the next seat decides how many divider positions are possible.
-> Every divider boundary is independent, and the number of plants between seat-pairs decides how many divider positions are possible, so we multiply choices.
"""

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7

        total_seats = corridor.count("S")

        # Invalid cases
        if total_seats < 2 or total_seats % 2 != 0:
            return 0

        ways = 1
        seat_count = 0
        plant_count = 0

        for ch in corridor:
            if ch == "S":
                seat_count += 1

                # Third seat means we crossed a boundary
                if seat_count == 3:
                    ways = (ways * (plant_count + 1)) % mod
                    plant_count = 0
                    seat_count = 1  # current seat becomes first seat of next group
            else:
                # Count plants only after exactly two seats
                if seat_count == 2:
                    plant_count += 1

        return ways