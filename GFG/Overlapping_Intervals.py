class Solution:
    def mergeOverlap(self, arr):
        # Step 1: Sort intervals based on start time first,
        # and end time second (in case start times are same)
        arr.sort(key=lambda x: (x[0], x[1]))

        # This list will store the merged intervals
        output = []

        # Step 2: Traverse each interval one by one
        for u, v in arr:

            # If output is empty, directly add the first interval
            if not output:
                output.append([u, v])

            else:
                # If current interval does NOT overlap
                # with the last interval in output
                if u > output[-1][1]:
                    output.append([u, v])

                else:
                    # Overlapping case:
                    # Merge current interval with the last interval
                    a, b = output.pop()

                    # New merged interval:
                    # start = min of both starts
                    # end   = max of both ends
                    output.append([min(a, u), max(b, v)])

        # Step 3: Return the merged intervals
        return output