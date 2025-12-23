# Method 1
import bisect

class Solution:
    def cntInRange(self, arr, queries):
        arr.sort()
        result = []

        for a, b in queries:
            left = bisect.bisect_left(arr, a)
            right = bisect.bisect_right(arr, b)
            result.append(right - left)

        return result
    
'''
⏱ Complexity (Alternative)
	•	Time:
	•	Sort: O(n log n)
	•	Each query: O(log n)
	•	Space: O(1) extra
'''

# Method 2

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

class Solution:
    def cntInRange(self, arr, queries):
        arr.sort()
        result = []

        for a, b in queries:
            left = lower_bound(arr, a)
            right = upper_bound(arr, b)
            result.append(right - left)

        return result

