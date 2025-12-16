"""

1️⃣ Thought Process (How I reason about it)

Problem understanding
I am given two strings s1 and s2. I need to check whether s2 is a rotation of s1.

Key observations
	•	A rotation does not change length
	•	Any rotation of s1 must appear as a contiguous substring inside s1 + s1
	•	Example:

s1 = geeksforgeeks
s1 + s1 = geeksforgeeksgeeksforgeeks
s2 = forgeeksgeeks   ✔ present



Why this works
	•	Concatenating the string with itself contains all possible rotations
	•	This avoids manually checking left and right rotations
	•	Reduces complex logic into a single substring check

Efficiency
	•	Time Complexity: O(n)
	•	Space Complexity: O(n)

⸻

2️⃣ High-Level Pseudocode

FUNCTION areRotations(s1, s2):

    IF length of s1 ≠ length of s2:
        RETURN False

    concatenated_string = s1 + s1

    IF s2 is substring of concatenated_string:
        RETURN True
    ELSE:
        RETURN False


⸻

🧠 Interview Explanation (first-person, concise)

“I first check if both strings have the same length. Then I concatenate the first string with itself. If the second string is a rotation, it must appear as a substring of this concatenated string. This allows me to check all rotations in linear time.”

⸻
"""

class Solution:
    def areRotations(self, s1, s2):
        # Step 1: If lengths differ, rotation is impossible
        if len(s1) != len(s2):
            return False

        # Step 2: Concatenate s1 with itself
        combined = s1 + s1

        # Step 3: Check if s2 exists as a substring
        if s2 in combined:
            return True

        return False

"""
Brute Force Solution:

class Solution:
    def areRotations(self, s1, s2):

        # Step 1: If lengths are different, s2 cannot be a rotation of s1
        if len(s1) != len(s2):
            return False

        # Store length of the string
        n = len(s1)

        # =========================
        # RIGHT ROTATION CHECK
        # =========================
        # We try all possible starting positions in s2
        # where the first character of s1 could match

        for start in range(n):

            # If the current character in s2 does not match
            # the first character of s1, skip this position
            if s2[start] != s1[0]:
                continue

            # i -> index for s1 (starts from beginning)
            # j -> index for s2 (starts from current 'start')
            i = 0
            j = start

            # Counter to track how many characters matched
            count = 0

            # Compare characters circularly
            while count < n and s1[i] == s2[j]:

                # Move forward in s1 (circularly)
                i = (i + 1) % n

                # Move forward in s2 (circularly)
                j = (j + 1) % n

                # Increase matched characters count
                count += 1

            # If all characters matched, it is a valid rotation
            if count == n:
                return True

        # =========================
        # LEFT ROTATION CHECK
        # =========================
        # Now we check rotation in the reverse direction

        for start in range(n):

            # Match last character of s1 for left rotation
            if s2[start] != s1[n - 1]:
                continue

            # i -> index for s1 (starts from end)
            # j -> index for s2 (starts from current 'start')
            i = n - 1
            j = start

            # Counter for matched characters
            count = 0

            # Compare characters circularly in reverse
            while count < n and s1[i] == s2[j]:

                # Move backward in s1 (circularly)
                i = n - 1 if i == 0 else i - 1

                # Move backward in s2 (circularly)
                j = n - 1 if j == 0 else j - 1

                # Increase matched characters count
                count += 1

            # If all characters matched, it is a valid rotation
            if count == n:
                return True

        # If neither right nor left rotation matched
        return False


🧠 Simple explanation in one line

We try all possible starting points in s2 and compare characters circularly with s1, first moving forward (right rotation) and then backward (left rotation).
"""