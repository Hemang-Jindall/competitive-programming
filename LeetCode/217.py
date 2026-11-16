# Problem: Given an integer array nums, return true if any value appears at least twice.
# What is this asking me to do in one sentence?
# Detect repetition in a collection.
# What category does this feel like?
# Hashing. Any time the problem is about "have I seen this before", that's a hash set.
# What are the constraints telling me?

# nums.length up to 10⁵ — O(n²) brute force (nested loops) is 10¹⁰ operations, too slow. I need O(n).
# Values range from -10⁹ to 10⁹ — wide range, so I can't use an array as a frequency counter (too much memory). Hash set handles this fine.

# What's my first instinct?
# Walk through the array, keep a set of seen values. The moment I encounter a value already in the set, return true. If I finish the loop, return false.
# Is there another approach?
# Sort the array, then check adjacent elements — O(n log n) time, O(1) extra space. Worse time but better space. Worth knowing both.
# What's the gotcha / edge case?
# Array of length 1 — trivially false, the loop never finds a duplicate. The algorithm handles it naturally, but worth noting.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True