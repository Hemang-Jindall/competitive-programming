# Problem: 3Sum
# One sentence: Return three distinct elements from an array whose net sum is zero
# Category: Array
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Loop thrice (brute force)
# Other approach: max(x,y) <= 2*min(x,y)+2 per half.
# Gotcha: second half scores are (c-a, d-b), not (c,d).


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])

                        if triplet not in result:
                            result.append(triplet)

        return result